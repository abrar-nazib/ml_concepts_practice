# ML Concepts

From-scratch implementations of core machine learning ideas. Each top-level
folder is one concept area: code, short notes, and tests live together.

## Layout

```
ml/
├── linear-models/   # linear & logistic regression, ridge/lasso, perceptron
├── trees/           # decision trees, random forests, gradient boosting
├── nn/              # MLPs, autograd, optimizers, regularization
├── transformers/    # attention, encoder/decoder blocks, mini-GPT
└── common/          # shared utilities (data, plotting, metrics)
```

Each concept folder follows the same shape:

```
<concept>/
├── README.md        # the idea, math, references
├── numpy_impl.py    # from-scratch reference implementation
├── torch_impl.py    # idiomatic framework version (when relevant)
└── tests/           # sanity checks vs. sklearn / closed-form solutions
```

Add a new concept folder anytime — there's no central registry.

## Setup

This project uses [uv](https://github.com/astral-sh/uv).

```bash
# core deps (numpy, scipy, sklearn, matplotlib, jupyter)
uv sync

# add a framework when you need it
uv sync --extra torch
uv sync --extra jax
uv sync --extra tf

# everything
uv sync --all-extras
```

Run a script: `uv run python linear-models/numpy_impl.py`
Open notebooks: `uv run jupyter lab`
