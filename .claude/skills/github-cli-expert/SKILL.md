---
name: github-cli-pair-programmer
description: >
  Use this skill whenever the user wants to review, approve, merge, or manage pull requests
  using the GitHub CLI (gh). Triggers on: "review my PR", "check my PRs", "approve this PR",
  "merge the PR", "look at my pull request", "act as my pair programmer", "give feedback on
  my PR", "what's in this diff", "list open PRs", "add a comment to the PR", or any mention
  of gh CLI usage for code review or PR workflows. Always use this skill when the user is
  working on GitHub PRs from the terminal or Claude Code — even if they don't say "gh" explicitly.
  This skill makes you an active pair programmer: you read diffs, reason about code quality,
  and take concrete gh CLI actions on behalf of the user.
---

# GitHub CLI Pair Programmer

You are the user's pair programmer. Your job is to use `gh` CLI to inspect, review, comment on,
approve, and merge their pull requests — and to think critically about the code like a senior
engineer would.

---

## 0. Auth Check (always run first)

```bash
gh auth status
```

If not authenticated: `gh auth login` (browser flow). Confirm the correct account/org is active.

---

## 1. Core PR Workflow

### List open PRs
```bash
gh pr list                          # PRs in current repo
gh pr list --author @me             # only mine
gh pr list --state all              # open + closed + merged
gh pr list --json number,title,headRefName,author,createdAt | jq .
```

### View a PR
```bash
gh pr view <number>                 # summary: title, body, status, checks
gh pr view <number> --json title,body,additions,deletions,files | jq .
gh pr checks <number>               # CI status
```

### Read the diff (critical for review)
```bash
gh pr diff <number>                             # full unified diff
gh pr diff <number> --name-only                 # just changed file names
gh pr diff <number> | head -200                 # first 200 lines
```

> **Pair programmer tip:** Always read the full diff before commenting or approving. Use
> `gh pr diff` and reason about: correctness, edge cases, test coverage, readability, and
> whether the PR matches its stated purpose.

---

## 2. Reviewing a PR (Step by Step)

1. **Fetch the diff and understand the change:**
   ```bash
   gh pr diff <number>
   ```

2. **Check CI:**
   ```bash
   gh pr checks <number>
   ```

3. **Read the PR description:**
   ```bash
   gh pr view <number>
   ```

4. **Write your review:**

   Leave inline file comment:
   ```bash
   gh pr review <number> --comment --body "Your review text here"
   ```

   Request changes:
   ```bash
   gh pr review <number> --request-changes --body "Please fix X before merging."
   ```

   Approve:
   ```bash
   gh pr review <number> --approve --body "LGTM! Ship it."
   ```

   > Note: GitHub does not allow self-approval. If the user authored the PR, you cannot approve
   > it on their behalf via their token — use a bot account or team member token.

5. **Add a standalone comment (not a formal review):**
   ```bash
   gh pr comment <number> --body "Quick note: consider also handling the nil case in line 42."
   ```

---

## 3. Merging a PR

```bash
# Default (merge commit)
gh pr merge <number>

# Squash and merge (preferred for feature branches)
gh pr merge <number> --squash

# Rebase and merge
gh pr merge <number> --rebase

# Auto-merge once all checks pass
gh pr merge <number> --auto --squash

# Delete branch after merge
gh pr merge <number> --squash --delete-branch
```

> **Pair programmer tip:** Don't merge if CI is red. Check `gh pr checks <number>` first.
> Prefer `--squash` for feature branches to keep history clean.

---

## 4. Checking Out a PR Locally

```bash
gh pr checkout <number>             # switches to the PR branch locally
```

Use this when you need to run the code, inspect it more deeply, or run tests before approving.

---

## 5. Editing and Managing PRs

```bash
gh pr edit <number> --title "New title"
gh pr edit <number> --body "Updated description"
gh pr edit <number> --add-label "needs-review"
gh pr edit <number> --add-reviewer username
gh pr edit <number> --base main             # change target base branch

gh pr ready <number>                        # mark draft PR as ready for review
gh pr close <number>                        # close without merging
gh pr reopen <number>
gh pr update-branch <number>               # merge latest base into PR branch
```

---

## 6. Pair Programmer Review Protocol

When the user says "review my PR" or "act as my pair programmer":

1. Run `gh pr list` to find the relevant PR (ask if ambiguous).
2. Run `gh pr diff <number>` — read the full diff.
3. Run `gh pr checks <number>` — note any CI failures.
4. Run `gh pr view <number>` — read the description and context.
5. Reason about the code:
   - Does the implementation match the PR's stated goal?
   - Are there bugs, edge cases, or off-by-one errors?
   - Is error handling present and correct?
   - Are there missing tests?
   - Is the code readable and well-named?
   - Any security or performance concerns?
6. Post your findings:
   - Use `gh pr review <number> --comment` for general feedback.
   - Use `gh pr review <number> --request-changes` if there are blockers.
   - Use `gh pr review <number> --approve` if it's good to merge.
7. If the user says "merge it" and CI is green, run `gh pr merge <number> --squash --delete-branch`.

---

## 7. Useful Utility Commands

```bash
gh pr status                        # PRs involving you (created, review requested, mentioned)
gh pr view <number> --web           # open PR in browser

# Filter PRs
gh pr list --label "bug"
gh pr list --assignee @me

# JSON output for scripting
gh pr view <number> --json number,title,state,mergeable,reviewDecision | jq .
```

---

## 8. Issues (supporting context)

```bash
gh issue list
gh issue view <number>
gh issue comment <number> --body "Related to PR #X"
gh issue close <number>
```

---

## 9. Repo & Auth Utilities

```bash
gh repo view                        # current repo info
gh auth status                      # who's logged in
gh auth switch                      # switch between accounts
gh api rate_limit                   # check API rate limits
```

---

## 10. Flags Quick Reference

| Flag | Command | Meaning |
|------|---------|---------|
| `--approve` | `gh pr review` | Approve the PR |
| `--request-changes` | `gh pr review` | Block merge, request fixes |
| `--comment` | `gh pr review` | Leave review comment (no decision) |
| `--body` | review/comment | Body text of comment or review |
| `--squash` | `gh pr merge` | Squash commits on merge |
| `--rebase` | `gh pr merge` | Rebase merge |
| `--auto` | `gh pr merge` | Auto-merge when checks pass |
| `--delete-branch` | `gh pr merge` | Delete branch after merge |
| `--name-only` | `gh pr diff` | Only show changed file names |
| `--json` | most commands | Output as JSON (pipe to `jq`) |

---

## 11. Common Pitfalls

- **Can't approve own PR:** GitHub blocks self-approval. Use a separate reviewer account.
- **Merge blocked by required reviews:** Check `gh pr view --json reviewDecision`. You may need another human reviewer.
- **Merge blocked by failing checks:** Always run `gh pr checks <number>` first.
- **Wrong repo context:** Run `gh repo view` to confirm you're in the right repo.
- **PR not found by number:** Make sure you're inside the correct local git repo directory.