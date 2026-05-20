---
name: gh-cli
user-invocable: true
description: "Use when: working with GitHub CLI (gh), PR review workflows, gh pr view/diff/review/comment, or needing a quick gh cheatsheet. Includes rules: review PRs via GitHub commit/PR diffs, and start PR comments with identity header."
---

# GitHub CLI Cheatsheet and Review Rules

## Identity and Comment Format

- Start PR comments with: "GitHub Copilot (GPT-5.2-Codex):" on the first line.
- Use clean markdown (blank lines between paragraphs, bullets for lists).

## Review Rules

- Always review via GitHub PR and commit diffs, not local repo diffs.
- Prefer commit-level diffs for review context; then check full PR diff.

## Quick PR Workflow

- List recent PRs:
  - gh pr list --limit 5
- View PR details (JSON fields):
  - gh pr view 123 --json title,body,author,headRefName,baseRefName,url,commits
- View PR diff:
  - gh pr diff 123
- View PR in browser:
  - gh pr view 123 --web
- Comment on PR:
  - gh pr comment 123 --body "GitHub Copilot (GPT-5.2-Codex): ..."
- Review PR (approve/comment/request changes):
  - gh pr review 123 --approve -b "..."
  - gh pr review 123 --comment -b "..."
  - gh pr review 123 --request-changes -b "..."

## Commit-Level Diffs (GitHub API)

- Fetch a commit diff from GitHub:
  - gh api -H "Accept: application/vnd.github.v3.diff" /repos/{owner}/{repo}/commits/{sha}

## Common Pitfalls

- You cannot request changes on your own PR. Use --comment instead.
- If review comments look broken, edit the last comment:
  - gh pr comment 123 --edit-last --body "GitHub Copilot (GPT-5.2-Codex): ..."

## Useful PR JSON Fields

- title, body, author, url, commits, files, labels, state, reviewDecision

## Notes

- Use --json + --jq for structured output.
- Use --web when a visual diff is easier to parse.
