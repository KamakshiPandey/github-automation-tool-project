# GitHub Automation Tool

A Python-based automation tool that streamlines repository management by integrating CI/CD workflows, pull request labeling, Slack notifications, and stale PR/issue reminders. Designed to enhance productivity and demonstrate DevOps best practices.

## Features

- **CI/CD Workflows**  
  Automatically run tests and send results to Slack for every commit or pull request.

- **Auto PR Labeling & Reviewer Assignment**  
  Labels pull requests based on their title and assigns reviewers automatically.

- **Stale PR/Issue Reminder Bot**  
  Detects PRs or issues that have been inactive for a set number of days and sends reminders to contributors via Slack.

- **Secure Secret Management**  
  Integrates GitHub secrets (e.g., API tokens) without exposing them in commits.

## Tech Stack

- **Language:** Python  
- **DevOps Tools:** GitHub Actions (CI/CD automation), Git (version control), Slack API (notifications), GitHub API (automation for PRs and issues), Python-dotenv (secure environment variable management)

