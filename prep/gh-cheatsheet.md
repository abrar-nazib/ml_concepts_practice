# `gh` cheat sheet

GitHub CLI commands organized by the workflow you'll actually use during
the PR cycle. Not exhaustive — focused on this repo's day-to-day.

Most commands take `--web` to open the equivalent page in a browser
instead. Use it when CLI output isn't enough (inline review comments,
visual diffs, etc.).

---

## Auth and basics

```bash
gh auth status                         # current login + scopes
gh auth refresh -s <scope>             # add scopes (e.g. workflow, gist)
gh api user --jq '.login'              # confirm which user you are
gh config get git_protocol             # should print "ssh"
```

---

## Repo

```bash
gh repo view                           # info about current repo (terminal)
gh repo view --web                     # open in browser
gh repo view <owner>/<name>            # info about any repo
gh repo clone <owner>/<name>           # clone (uses your default protocol)
gh repo fork                           # fork the current repo
gh repo create <name> --public         # create new repo (--private, --internal)
gh repo set-default                    # set default for ambiguous commands
```

---

## Pull requests — create

```bash
# interactive: gh prompts for title/body
gh pr create

# one-shot
gh pr create \
  --title "feat(model-selection): grid search CV from scratch" \
  --body "Implements ParameterGrid + nested k-fold loop. Cross-checked against sklearn on heart dataset (matches to 4 decimal places)."

# from a template file
gh pr create --title "..." --body-file .github/PULL_REQUEST_TEMPLATE.md

# draft PR (work-in-progress; cannot be merged until marked ready)
gh pr create --draft --title "..." --body "..."

# set reviewer / assignee / labels at creation
gh pr create --reviewer abrar-nazib --assignee @me --label "wk-1,classical-ml"

# fill from commits (no editor) — handy after a clean commit history
gh pr create --fill
```

Common flags:
- `--base main` — set base branch (default = repo's default branch)
- `--head <branch>` — set head branch (default = current branch)
- `--web` — open the browser PR form instead

---

## Pull requests — list and find

```bash
gh pr list                             # open PRs in this repo
gh pr list --state all                 # incl. closed/merged
gh pr list --author @me                # your PRs
gh pr list --assignee @me              # PRs assigned to you
gh pr list --label wk-1                # filter by label
gh pr list --search "is:open is:pr review-requested:@me"
gh pr status                           # PRs that need your attention
```

`--json` + `--jq` for scripting:

```bash
gh pr list --json number,title,headRefName,author \
  --jq '.[] | "\(.number) \(.headRefName) — \(.title)"'
```

---

## Pull requests — read

```bash
gh pr view                             # current branch's PR
gh pr view 7                           # PR #7
gh pr view 7 --web                     # open in browser
gh pr view 7 --comments                # show conversation thread
gh pr diff 7                           # unified diff
gh pr diff 7 --name-only               # files changed
gh pr checks 7                         # CI check statuses
```

---

## Pull requests — check out and run locally

```bash
gh pr checkout 7                       # creates local branch tracking PR #7
# now run/test it locally
uv run python -m pytest model-selection/grid-search/tests/
# when done reviewing, go back
git checkout main
```

If you also want to update the PR (e.g. fix something during review):

```bash
gh pr checkout 7
# ...edit, commit...
git push                               # pushes to the PR's branch
```

---

## Pull requests — review

The CLI handles **PR-level** reviews well. For **inline file comments**,
fall back to the web UI — easier to point at exact lines.

```bash
# leave a comment without approving/blocking
gh pr review 7 --comment --body "Looks good overall; a few notes inline (see web)."

# approve
gh pr review 7 --approve --body "LGTM. Solid eval coverage."

# request changes (blocks merge)
gh pr review 7 --request-changes --body "Please add a test for the empty-fold edge case."

# review body from a file (handy for longer feedback)
gh pr review 7 --approve --body-file /tmp/review-notes.md
```

For inline comments:

```bash
gh pr view 7 --web                     # open in browser, leave inline comments
```

---

## Pull requests — merge and close

```bash
# merge strategies: --squash, --merge, --rebase
gh pr merge 7 --squash --delete-branch        # preferred for feature PRs
gh pr merge 7 --merge                          # preserves all commits
gh pr merge 7 --rebase --delete-branch         # linear history, no merge commit

# auto-merge when checks pass (great for slow CI)
gh pr merge 7 --squash --auto

# close without merging
gh pr close 7 --comment "Superseded by #9"

# reopen
gh pr reopen 7
```

---

## Issues (lighter, for tracking topics)

```bash
gh issue create --title "Wk 3: schedule MLP-from-scratch deep-dive"
gh issue list --assignee @me
gh issue view 12
gh issue close 12
gh issue comment 12 --body "Done, see PR #18"

# convert issue → PR (when work is ready)
# (no direct CLI; reference issue in PR body with "Closes #12" — auto-closes on merge)
```

---

## Workflow for the hybrid PR cycle

### When **you** write (Mon/Wed/Fri)

```bash
git checkout main && git pull
git checkout -b feature/<area>-<concept>
# ...work, commit small...
git push -u origin feature/<area>-<concept>
gh pr create --title "feat(<area>): <one-line>" \
             --body "Why: ...\nWhat: ...\nNotes: ..." \
             --label "wk-N"
# share PR URL → I review
# after my review, iterate, then:
gh pr merge --squash --delete-branch        # when approved
```

### When **I** write (Tue/Thu) — your review cycle

```bash
gh pr list --author <my-account>           # find the PR
gh pr view <n> --comments                  # read description + thread
gh pr diff <n>                              # CLI diff
gh pr checkout <n>                          # run it locally if curious
uv run jupyter lab                          # poke around
gh pr view <n> --web                        # leave inline comments
# back in terminal — final review verdict:
gh pr review <n> --approve --body "Approved. One nit in the web inline."
# or
gh pr review <n> --request-changes --body "Need: add a smoke test before merging."
# once green:
gh pr merge <n> --squash --delete-branch
```

---

## Useful flags and power moves

```bash
# Pipe any list command's JSON through jq for custom formats
gh pr list --json number,title --jq '.[] | "#\(.number) \(.title)"'

# Browse anything in the web UI
gh pr view --web
gh repo view --web
gh issue view 12 --web

# Aliases — save common commands as shorthand
gh alias set co "pr checkout"
gh alias set v "pr view --web"
# then: gh co 7   /   gh v 7

# Search across all of GitHub from CLI
gh search repos "graphbit"
gh search prs --author abrar-nazib --state merged

# Inspect a workflow run
gh run list                                 # CI runs in this repo
gh run view <run-id>
gh run watch                                # tail the latest run
```

---

## Common slip-ups

- **`gh pr create` from `main`** — must be on a feature branch. If you
  forget, `git checkout -b feature/...` and re-run.
- **No upstream when pushing first time** — use `git push -u origin <branch>`
  so subsequent `git push` works without args. `gh pr create` also pushes
  automatically if you forgot.
- **`--web` ignores your `--body`** — opens the form pre-filled, but you
  type the body in the browser.
- **Squash merge eats commit history** — fine for feature PRs (we want
  clean history on `main`), bad for PRs that need bisect granularity.
  Use `--merge` if granular history matters.
- **`gh pr merge` without `--delete-branch`** leaves dead branches on the
  remote. Always pair them.

---

## What to do once per repo

```bash
# set default branch for ambiguous commands
gh repo set-default <owner>/<name>

# (optional) create useful labels for the PR cycle
gh label create wk-1 --color "0075ca"
gh label create wk-2 --color "0075ca"
# ...etc.
gh label create flagship --color "d93f0b" --description "Headline portfolio piece"
gh label create from-scratch --color "5319e7" --description "Numpy / no-framework impl"
```
