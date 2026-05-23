# 5-week ML/DL plan (CampusX-first)

Plan reset date: 2026-05-25.

This repo is my ML/DL/AI dictionary and notebook of concepts. From this point:
- `campusx-course/` is the active learning track.
- Existing top-level concept folders stay as legacy/reference code.
- I can move selected ideas from `campusx-course/` into generalized folders for
  experimentation.

## Weekly outline

### Wk 1 (2026-05-25 to 2026-05-31) - PyTorch rundown + organize progress

Goal: categorize and clean up current PyTorch progress only.

Scope:
- Review and organize existing PyTorch notebooks/code.
- Normalize naming, sectioning, and notes where needed.
- Add short summaries of what each notebook demonstrates.
- No major new concept target this week beyond the PyTorch rundown.

Suggested deliverables:
- `campusx-course/wk-1-pytorch-rundown/README.md`
- `campusx-course/wk-1-pytorch-rundown/notes.md`
- Links to relevant legacy notebooks in `nn/`.

### Wk 2 (2026-06-01 to 2026-06-07) - CampusX foundations + ANN

Goal: start and progress through the early CampusX deep learning modules.

Scope:
- Deep learning basics and neural network foundations.
- Perceptron -> MLP -> forward pass/backprop fundamentals.
- ANN practical examples and core regularization ideas.

Suggested deliverables:
- `campusx-course/wk-2-foundations-ann/`
- Notes + runnable notebook(s) summarizing core ANN learnings.

### Wk 3 (2026-06-08 to 2026-06-14) - CampusX optimization + CNN

Goal: complete optimizer/initialization/normalization blocks and move into CNNs.

Scope:
- Optimization methods and training stability techniques.
- CNN fundamentals, architecture intuition, and practical projects.

Suggested deliverables:
- `campusx-course/wk-3-optimization-cnn/`
- CNN notes and at least one end-to-end classification notebook.

### Wk 4 (2026-06-15 to 2026-06-21) - CampusX RNN/LSTM/GRU

Goal: complete sequence modeling foundations from the course.

Scope:
- RNN basics and BPTT intuition.
- LSTM/GRU variants and practical modeling patterns.

Suggested deliverables:
- `campusx-course/wk-4-rnn-lstm-gru/`
- Sequence-model notes + runnable experiment notebook(s).

### Wk 5 (2026-06-22 to 2026-06-28) - CampusX attention + transformers

Goal: finish the CampusX course with attention and transformer modules.

Scope:
- Attention mechanisms and self-attention details.
- Transformer encoder/decoder architecture and inference understanding.

Suggested deliverables:
- `campusx-course/wk-5-attention-transformers/`
- Consolidated transformer notes + one walkthrough notebook.

## Wk 2-5 day-wise video targets (CampusX playlist)

Target: complete all 84 videos across 28 days (2026-06-01 to 2026-06-28).

| Day | Date | Target videos/day | Playlist index target |
|---:|---|---:|---|
| 1 | 2026-06-01 | 3 | 01-03 |
| 2 | 2026-06-02 | 2 | 04-05 |
| 3 | 2026-06-03 | 5 | 06-10 |
| 4 | 2026-06-04 | 3 | 11-13 |
| 5 | 2026-06-05 | 2 | 14-15 |
| 6 | 2026-06-06 | 3 | 16-18 |
| 7 | 2026-06-07 | 5 | 19-23 |
| 8 | 2026-06-08 | 4 | 24-27 |
| 9 | 2026-06-09 | 3 | 28-30 |
| 10 | 2026-06-10 | 4 | 31-34 |
| 11 | 2026-06-11 | 4 | 35-38 |
| 12 | 2026-06-12 | 3 | 39-41 |
| 13 | 2026-06-13 | 5 | 42-46 |
| 14 | 2026-06-14 | 4 | 47-50 |
| 15 | 2026-06-15 | 5 | 51-55 |
| 16 | 2026-06-16 | 3 | 56-58 |
| 17 | 2026-06-17 | 3 | 59-61 |
| 18 | 2026-06-18 | 2 | 62-63 |
| 19 | 2026-06-19 | 2 | 64-65 |
| 20 | 2026-06-20 | 2 | 66-67 |
| 21 | 2026-06-21 | 2 | 68-69 |
| 22 | 2026-06-22 | 2 | 70-71 |
| 23 | 2026-06-23 | 2 | 72-73 |
| 24 | 2026-06-24 | 2 | 74-75 |
| 25 | 2026-06-25 | 2 | 76-77 |
| 26 | 2026-06-26 | 2 | 78-79 |
| 27 | 2026-06-27 | 2 | 80-81 |
| 28 | 2026-06-28 | 3 | 82-84 |

Notes:
- Keep video order as-is from the playlist.
- If a day slips, carry overflow to the next day but keep index continuity.
- Wk 1 remains PyTorch-only (no fixed CampusX playlist quota).

## Working structure

Primary active path:

```text
campusx-course/
  wk-1-pytorch-rundown/
  wk-2-foundations-ann/
  wk-3-optimization-cnn/
  wk-4-rnn-lstm-gru/
  wk-5-attention-transformers/
```

Legacy/reference remains in existing folders (`nn/`, `cv/`, `sequence/`,
`transformers/`, etc.).

## Weekly operating rule

- Keep active edits in `campusx-course/` first.
- Pull selected course ideas into generalized folders only when needed for
  experiments or cleaner concept indexing.
- Keep short README notes for each week so progress remains reviewable.
