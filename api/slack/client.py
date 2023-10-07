from slack_sdk import WebClient
from slack.models import Workspace

# We will eventually incorporate the ability to handle multiple teams
client = WebClient(token=Workspace.objects.get().token)