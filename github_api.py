# import requests
# from config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME

# BASE_URL = "https://api.github.com"

# def create_pull_request(branch, base="main", title="Auto PR", body="Automated PR"):
#     url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
#     headers = {"Authorization": f"token {GITHUB_TOKEN}"}
#     payload = {"title": title, "body": body, "head": branch, "base": base}

#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code == 201:
#         return response.json()
#     else:
#         raise Exception(f"Failed to create PR: {response.status_code}, {response.text}")


# def merge_pull_request(pr_number):
#     url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/merge"
#     headers = {"Authorization": f"token {GITHUB_TOKEN}"}
#     payload = {"merge_method": "squash"}

#     response = requests.put(url, json=payload, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Failed to merge PR: {response.status_code}, {response.text}")
# import requests
# from config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME

# BASE_URL = "https://api.github.com"
# HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"}

# # -----------------------------
# # Pull Request Functions
# # -----------------------------
# def create_pull_request(branch, base="main", title="Auto PR", body="Automated PR"):
#     url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
#     payload = {"title": title, "body": body, "head": branch, "base": base}
#     response = requests.post(url, json=payload, headers=HEADERS)
#     if response.status_code == 201:
#         return response.json()
#     raise Exception(f"Failed to create PR: {response.status_code}, {response.text}")

# def merge_pull_request(pr_number):
#     url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/merge"
#     payload = {"merge_method": "squash"}  # merge, squash, rebase
#     response = requests.put(url, json=payload, headers=HEADERS)
#     if response.status_code == 200:
#         return response.json()
#     raise Exception(f"Failed to merge PR: {response.status_code}, {response.text}")

# # -----------------------------
# # Branch Management Functions
# # -----------------------------
# def branch_exists(branch_name):
#     url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/branches/{branch_name}"
#     response = requests.get(url, headers=HEADERS)
#     return response.status_code == 200  # True if branch exists

# def create_branch(branch_name, base_branch="main"):
#     # Get SHA of base branch
#     url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/git/ref/heads/{base_branch}"
#     response = requests.get(url, headers=HEADERS)
#     if response.status_code != 200:
#         raise Exception(f"Base branch '{base_branch}' not found: {response.status_code}")
#     base_sha = response.json()["object"]["sha"]

#     # Create new branch
#     url_create = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/git/refs"
#     payload = {"ref": f"refs/heads/{branch_name}", "sha": base_sha}
#     response_create = requests.post(url_create, json=payload, headers=HEADERS)
#     if response_create.status_code == 201:
#         return response_create.json()
#     raise Exception(f"Failed to create branch '{branch_name}': {response_create.status_code}, {response_create.text}")
import requests
from config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME

BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# -----------------------------
# Pull Request Functions
# -----------------------------
def create_pull_request(branch, base="main", title="Auto PR", body="Automated PR"):
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    payload = {"title": title, "body": body, "head": branch, "base": base}
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 201:
        return response.json()
    raise Exception(f"Failed to create PR: {response.status_code}, {response.text}")

def merge_pull_request(pr_number):
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/merge"
    payload = {"merge_method": "squash"}  # merge, squash, rebase
    response = requests.put(url, json=payload, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"Failed to merge PR: {response.status_code}, {response.text}")

# -----------------------------
# Branch Management Functions
# -----------------------------
def branch_exists(branch_name):
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/branches/{branch_name}"
    response = requests.get(url, headers=HEADERS)
    return response.status_code == 200  # True if branch exists

def create_branch(branch_name, base_branch="main"):
    # Get SHA of base branch
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/git/ref/heads/{base_branch}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Base branch '{base_branch}' not found: {response.status_code}")
    base_sha = response.json()["object"]["sha"]

    # Create new branch
    url_create = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/git/refs"
    payload = {"ref": f"refs/heads/{branch_name}", "sha": base_sha}
    response_create = requests.post(url_create, json=payload, headers=HEADERS)
    if response_create.status_code == 201:
        return response_create.json()
    raise Exception(
        f"Failed to create branch '{branch_name}': {response_create.status_code}, {response_create.text}"
    )

# -----------------------------
# Commit Monitoring Functions
# -----------------------------
def get_latest_commits(branch="main", per_page=5):
    """
    Fetch the latest commits from a branch with diff summary (additions, deletions).
    """
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/commits"
    params = {"sha": branch, "per_page": per_page}
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch commits: {response.status_code}, {response.text}")

    commits = []
    for commit in response.json():
        sha = commit["sha"]
        message = commit["commit"]["message"]
        author = commit["commit"]["author"]["name"]

        # Get commit details for stats
        detail_url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/commits/{sha}"
        detail_resp = requests.get(detail_url, headers=HEADERS)
        stats = detail_resp.json().get("stats", {})

        commits.append({
            "sha": sha,
            "message": message,
            "author": author,
            "additions": stats.get("additions", 0),
            "deletions": stats.get("deletions", 0),
        })
    return commits
