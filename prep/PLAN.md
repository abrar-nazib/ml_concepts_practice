# 8-week ML/AI engineering study plan

Plan start: 2026-05-12. Target interview window: July 2026.
Target role profile: mid-level AI Engineer, research-leaning (LLM core + CV
side projects on depth/stereo/env-awareness; RL on the periphery).

This repo doubles as the portfolio. Every week ships at least one
PR-reviewed, README-documented artifact that can be linked to from a CV.

## Daily structure (~3 hours)

| Block | Duration | What |
|-------|---------:|------|
| Paper / theory | 30 min | Read or skim from [`papers.md`](papers.md). One pass per day. |
| Deep work | 2 hrs | Implementation, the day's PR-ready artifact. |
| Review / writeup | 30 min | Open or review a PR; update concept README; note what tripped you up. |

6 days/week (Sun off, or whichever day works). Saturday is "integration
day" — no new concept, only polish, walkthrough notebooks, README cleanup.

## Workflow (hybrid PR cycle)

- **Mon / Wed / Fri** — *you write*. Open a feature branch
  `feat/<area>-<concept>`. Open a PR with a "why" description. I review
  as senior peer, leave inline comments + suggested changes. You iterate.
  Merge with a squash commit.
- **Tue / Thu** — *I write*. PR for you to review. You leave comments,
  ask questions, request changes. I iterate. You merge.
- **Sat** — integration day. Polish the week's work into a notebook
  walkthrough; cross-link READMEs; tag a milestone.

Branch naming: `feat/<top-level-folder>-<short-desc>`. Examples:
- `feat/model-selection-kfold-from-scratch`
- `feat/metrics-confusion-matrix`
- `feat/rag-citations-eval`

PR title format: `feat(<area>): <one-line>`. Examples:
- `feat(model-selection): k-fold cross-validation from scratch`
- `feat(rag): retriever + reranker with RAGAS eval harness`

## 8-week curriculum

Priorities, highest → lowest leverage for this interview:
RAG → agents → classical ML → vision/depth → transformer internals
→ RL primer → LeetCode/behavioral. Plan order is *pedagogical*, not
priority — foundations first so later weeks compound.

### Week 1 — Classical ML foundations (Days 1–3)

- Topics: KFold, StratifiedKFold, GridSearchCV, RandomizedSearchCV,
  train/val/test discipline, confusion matrix, precision / recall / F1,
  ROC-AUC, calibration.
- Daily papers (skim level, 30 min each): see [`papers.md`](papers.md) §1.
- **Day 3 ship** — `notebooks/heart_disease_walkthrough.ipynb`: one
  integration notebook that ties together your kfold / grid-search /
  random-search / metrics work into a single end-to-end pipeline on the
  heart-disease dataset. Read top-to-bottom as: load → split → CV →
  tuning → metrics → markdown takeaway. This is the Wk 1 portfolio
  piece — without it, your 4 demo notebooks read as exercises, not a
  project.

### Week 2 — Classical ML sprint (Day 4 only, ~1 day)

Compressed from 6 days to 1 — from-scratch implementations dropped
(Bourke's PyTorch training loop covers the same intuition, and modern
AI-eng interviews skew preprocessing + ensemble methods over numpy
gradient descent).

- Topics covered through one integrated notebook: XGBoost + LightGBM,
  `Pipeline` + `ColumnTransformer`, missing values, categorical
  encoding, scaling, class imbalance (class weights vs SMOTE vs
  threshold tuning), calibration.
- Daily papers: [`papers.md`](papers.md) §2.
- **Day 4 ship** — `trees/xgb_lightgbm_imbalanced.ipynb`: one notebook,
  one imbalanced tabular dataset (credit-card fraud or churn), full
  preprocessing Pipeline, both XGBoost and LightGBM with proper
  StratifiedKFold, class-weight + SMOTE comparison, calibration plot.
  This is the second tabular portfolio piece — gives you the talking
  points "I used SMOTE alongside class weights, calibrated with
  isotonic regression because the fraud cost matrix was asymmetric."

### Week 3 — Neural networks (PyTorch foundation via Bourke) — starts Day 5

- **Spine**: Daniel Bourke's *Learn PyTorch for Deep Learning*
  ([YouTube, 25h](https://www.youtube.com/watch?v=V_xro1bcAuA),
  [companion site](https://learnpytorch.io)). Code along, don't just
  watch. Skip §0–12 (intro philosophy) and 1.5× speed §13–28 (tensor
  basics ≈ numpy you already know). Normal speed for everything
  involving an actual training loop / optimizer step / loss curve.
  - Bourke Ch 0 (fundamentals, ~4h) — tensors, GPU, device-agnostic code.
  - Bourke Ch 1 (workflow, ~4h) — training loop, save/load, the
    canonical PyTorch lifecycle.
  - Bourke Ch 2 (classification NN, ~5.5h) — first real classifier in
    PyTorch.
- Topics covered alongside the course: `nn.Module`, autograd, SGD /
  Adam, dropout, batchnorm, logits → probs → labels, train/test loop
  patterns.
- Drop the "MLP from scratch in numpy" target — Bourke's training-loop
  walkthrough is more interview-relevant time spent.
- Daily papers: [`papers.md`](papers.md) §3.
- Ship: **PyTorch classification project on a real dataset** (your
  choice — keep the heart dataset for continuity, or pick a new one).
  Train/val curves logged, README explaining what you actually learned
  from Bourke vs. what you added on top.

### Week 4 — Transformers + ViT

- Topics: scaled dot-product attention, multi-head attention,
  positional encodings, layer norm, residual streams, KV cache,
  tokenization (BPE/WordPiece/SentencePiece), decoding (temperature,
  top-k, top-p, beam search). ViT for the vision crossover.
- Daily papers: [`papers.md`](papers.md) §4. **Attention Is All You Need
  is a deep read this week, not a skim.**
- Ship: **tiny char-level transformer** trained on a small corpus
  (Shakespeare-style), plus a notebook walking through one full
  forward pass of attention with shapes annotated.

### Week 5 — LLM application engineering + RAG primer

- Topics: Anthropic / OpenAI SDKs, system prompts, structured outputs,
  tool calling / function calling, prompt caching, CoT / ReAct /
  self-consistency, fine-tuning vs prompting vs RAG decision matrix,
  LoRA / QLoRA at concept level. Light RAG intro (embeddings, naive
  retrieval) to set up week 6.
- Daily papers: [`papers.md`](papers.md) §5.
- Ship: **CLI tool-using assistant** with prompt caching enabled and
  at least 2 tools.

### Week 6 — RAG flagship + agents intro

- Topics: embeddings (closed + open), vector DBs (pick one: pgvector or
  Qdrant), chunking strategies (fixed / sentence / semantic / sliding /
  late), hybrid retrieval (BM25 + dense + cross-encoder rerank), RAGAS
  evaluation (faithfulness, answer relevancy, context precision/recall),
  citations, prompt-injection defense. Agent intro: tool-call loops,
  determinism, retries.
- Daily papers: [`papers.md`](papers.md) §6.
- Ship: **RAG-with-citations + eval harness** over a real document
  collection. This is the flagship portfolio piece — point of pride,
  generous README, architecture diagram, eval numbers.

### Week 7 — Vision: depth estimation + stereo

- Plays to your existing CV background. Goal: a clean refresher that
  produces a strong portfolio piece in your area of strength.
- **Front-load**: Bourke Ch 3 (computer vision, ~5.5h) at 1.5× speed —
  CNNs, TorchVision, DataLoaders, end-to-end CV training loops. Skip
  §92–95 (CV intro/what-is-CNN philosophy). Bourke Ch 4 (custom
  datasets) is optional; you'll absorb that material naturally while
  building the depth project.
- Topics: classical stereo (rectification, block matching, semi-global
  matching), modern deep stereo (RAFT-Stereo, IGEV), monocular depth
  (MiDaS, DPT, Depth Anything v2), environmental awareness use cases.
- Daily papers: [`papers.md`](papers.md) §7.
- Ship: **depth estimation comparison project** — pick a real stereo
  pair (KITTI / Middlebury / your own), run a classical method and a
  deep method, compare error metrics, write up trade-offs. Bonus: small
  env-awareness demo (e.g. obstacle map from depth).

### Week 8 — RL primer + system design + interview polish

- RL primer (concept-level, one toy implementation): MDPs, value iter,
  Q-learning, REINFORCE (policy gradient), PPO at concept level.
  Implement REINFORCE on CartPole; that's enough for interview signal.
- AI system design rehearsal: walk through "RAG at 1M users", "real-time
  LLM inference under cost ceiling", "deterministic agent at scale".
- LeetCode Medium drills: trees, graphs, hash maps, sliding window,
  trie/DFS. ~30 min/day.
- Behavioral: rehearse 3 stories — one classical ML, one LLM/RAG, one
  failure-and-recovery. Use STAR format.
- Daily papers: [`papers.md`](papers.md) §8 (lighter — focus shifts to
  practice).
- Ship: **cleaned up portfolio**. Every concept folder has a
  professional README. Top-level README is a recruiter's first 30
  seconds — make it count.

## Research signals to thread through every week

InfinitiBit hires mid-levels for research-leaning work. So even on
classical ML weeks, demonstrate:

- **Ablations** — vary one knob, plot the effect, write the conclusion.
- **Eval rigor** — never report a single number; always report a
  distribution (k-fold mean ± std) or a confidence interval.
- **Reproducibility** — fix seeds, log versions, write a one-line repro
  command at the top of every notebook.
- **Reading habit visibility** — a `prep/papers.md` log of what you've
  read with one-line takeaways is itself a research signal. Recruiters
  reading the repo will see it.
- **Writing** — a clean README explaining *why* and *what was learned*
  is the difference between a tutorial and research-mindset work.

## Milestones (end-of-week checklist)

- [ ] Wk 1 — `heart_disease_walkthrough.ipynb` integration shipped, 4+ component PRs merged
- [ ] Wk 2 (1-day sprint) — `trees/xgb_lightgbm_imbalanced.ipynb` shipped, paper log started
- [ ] Wk 3 — MLP + CNN in PyTorch shipped
- [ ] Wk 4 — tiny transformer shipped + attention walkthrough notebook
- [ ] Wk 5 — tool-using CLI assistant shipped
- [ ] Wk 6 — **RAG-with-citations flagship shipped** (the headline piece)
- [ ] Wk 7 — depth estimation project shipped (the CV headline piece)
- [ ] Wk 8 — RL toy + cleaned portfolio + rehearsed behavioral stories

## Things that can derail this — watch for them

- **Pivoting weekly.** Wk 1–2 are *locked* as of Day 2 settle:
  integration notebook (Day 3) + XGB/LightGBM imbalanced notebook
  (Day 4) + Bourke from Day 5. No more reshuffling until Bourke is
  done or you hit a real blocker.
- **Perfectionism on early weeks.** Don't implement classical
  algorithms from scratch. Wk 1–2 are foundations; the high-leverage
  weeks are 5–7. Cut early if you're behind.
- **Tutorial trap.** Following a tutorial step-by-step doesn't build
  the research signal. Always end a session with something you wrote
  that the tutorial didn't show.
- **Paper overload.** 30 min/day is the budget. If a paper needs 2
  hours, skim today, deep-read on Saturday.
- **Putting off the flagship.** The RAG project in week 6 is the most
  important artifact. Don't compress it to make room for week-1 polish.
