# Metrics

Scoring functions for predictions. Mirrors `sklearn.metrics`.

## What lives here

**Classification:**
- `confusion_matrix` — TP/FP/FN/TN counts; foundation for the rest
- `accuracy`, `precision`, `recall`, `f1` — derived from the confusion matrix
- `roc_auc` — threshold-free ranking quality
- `log_loss` — probabilistic loss for calibrated outputs

**Regression:**
- `mse`, `rmse`, `mae`
- `r2` — fraction of variance explained

## Cross-cutting notes

- A metric is a pure function of `(y_true, y_pred)` (or `y_score` for
  threshold-free metrics). It doesn't know about models or splits.
- For multiclass, decide upfront: macro vs. micro vs. weighted averaging.
  They answer different questions.
- Cross-check every from-scratch implementation against the sklearn
  equivalent on a small fixture.
