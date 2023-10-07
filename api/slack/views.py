from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from slack.client import client
from slack.models import User, Workspace
from team.models import Dancer
from unidecode import unidecode

# Create your views here.
class SlackViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()

    @action(detail=True, methods=['post'])
    def generate_users(self, request, pk=None):
        '''
        This function is used to generate a list of new Users based on their names in Slack.
        It matches these users to dancers based on their names.
        '''

        workspace = Workspace.objects.get(pk=pk)

        # Get the list of users from Slack
        slack_users = client.users_list()
        
        print(slack_users["members"])

        for user in slack_users["members"]:
            print(user["real_name"])
            # Skip over bots, Slackbot, deleted users
            if user["is_bot"] or user["real_name"] == "Slackbot" or user["deleted"]:
                continue

            id  = user["id"]
            real_name = user["real_name"]

            decoded_name = unidecode(real_name).lower()

            #If the dancer already exists, just add the user
            if Dancer.objects.filter(name=decoded_name).exists():
                dancer = Dancer.objects.get(name=decoded_name)
                user = User(dancer=dancer, slack_id=id)
                user.save()

            #Otherwise, create the dancer and add the user
            else:
                dancer = Dancer(
                    name=decoded_name, 
                    team=workspace.season.team
                )

                dancer.save()
                user = User(dancer=dancer, slack_id=id, workspace=workspace)
                user.save()

        return HttpResponse({"message": "Success"})
        