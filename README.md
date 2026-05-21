# ML Concepts

From-scratch implementations of core machine learning ideas. Each top-level
folder is one concept area: code, short notes, and tests live together.

## Layout

```
ml/
├── common/           # shared utilities and notes
├── cv/               # CNNs and transfer learning
├── datasets/         # datasets used in notebooks
├── linear-models/    # linear & logistic regression, ridge/lasso, perceptron
├── metrics/          # confusion matrix, precision/recall/F1, etc.
├── model-selection/  # train/test split, k-fold CV, grid/random search
├── nn/               # tensors, autograd, optimizers, training pipeline
├── prep/             # study plan, papers, interview checklist
├── sequence/         # RNNs and next-word prediction
├── transformers/     # attention, encoder/decoder blocks
└── trees/            # decision trees, random forests, gradient boosting
```

Each concept folder keeps code, short notes, and notebooks together. Some
folders are notebook-first (e.g., [nn/](nn/), [metrics/](metrics/)), while
others include small scripts or helpers.

Add a new concept folder anytime — there's no central registry.

## Plan

The current 8-week study plan lives in [prep/PLAN.md](prep/PLAN.md), with
paper tracking in [prep/papers.md](prep/papers.md). This repo is also the
portfolio, so each week aims to ship a reviewed, documented artifact.

## Setup

This project uses [uv](https://github.com/astral-sh/uv).

```bash
# install uv (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# core deps (numpy, scipy, sklearn, matplotlib, jupyter)
uv sync

# add a framework when you need it
uv sync --extra torch
uv sync --extra jax
uv sync --extra tf

# everything
uv sync --all-extras

# add packages
uv add pandas
uv add torch

# add dev-only packages
uv add --dev pytest

# remove packages
uv remove pandas

# run commands in the env
uv run python linear-models/numpy_impl.py
uv run jupyter lab
```
Run a script: `uv run python linear-models/numpy_impl.py`
Open notebooks: `uv run jupyter lab`
