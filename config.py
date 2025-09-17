import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
