# Model selection

Splitting data and searching hyperparameters. Mirrors `sklearn.model_selection`.

## What lives here

**Splitters** — produce train/val (or train/val/test) index sets:
- `train_test_split` — single random holdout
- `kfold` — k disjoint folds, each used as val once
- `stratified_kfold` — k-fold that preserves class proportions per fold
- `leave_one_out` — k = n; one sample held out per run

**Hyperparameter search** — wrap a model + a splitter to score
configurations:
- `grid_search_cv` — exhaustive over a grid
- `random_search_cv` — sample N configurations from distributions

## Cross-cutting notes

- Splitters return *indices*, not data. The search/eval layer applies them.
- Score with metrics from `../metrics/`. Keep concerns separate: a splitter
  doesn't know what a "good" model is; a metric doesn't know how data was
  split.
- For classification on imbalanced data, prefer stratified splitters.
