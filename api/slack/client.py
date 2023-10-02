from slack_sdk import WebClient
from slack.models import Token

# We will eventually incorporate the ability to handle multiple teams
INSTANCE = WebClient(token=Token.objects.get().token)