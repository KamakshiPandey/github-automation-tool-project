from github_api import get_latest_commits
from notifier import notify_slack, notify_discord

def notify_commits():
    try:
        commits = get_latest_commits(branch="main", per_page=3)  # Last 3 commits
        for c in commits:
            msg = (
                f"📝 *New Commit*\n"
                f"👤 Author: {c['author']}\n"
                f"💬 Message: {c['message']}\n"
                f"➕ Additions: {c['additions']}, ➖ Deletions: {c['deletions']}\n"
                f"🔗 https://github.com/<your-username>/<your-repo>/commit/{c['sha']}"
            )
            notify_slack(msg)
            notify_discord(msg)
    except Exception as e:
        notify_slack(f"❌ Failed to fetch commits: {e}")
        notify_discord(f"❌ Failed to fetch commits: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    notify_commits()
