import requests
from config import SLACK_WEBHOOK, DISCORD_WEBHOOK

def notify_slack(message):
    if SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK, json={"text": message})

def notify_discord(message):
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": message})
