# ML Concepts

This repository is my ML/DL/AI dictionary: conceptual code, notes, and
experiments in one place.

Current direction:
- `campusx-course/` contains all active course tracking, notes, and code.
- Existing top-level concept folders remain as legacy/reference code.
- I may pull ideas from `campusx-course/` into the generalized structure for
	experiments.

## Layout

```
ml/
├── campusx-course/    # active CampusX deep learning course work
├── common/           # shared utilities and notes
├── cv/               # legacy/reference CV work
├── datasets/         # datasets used in notebooks
├── linear-models/    # legacy/reference linear model work
├── metrics/          # legacy/reference metrics work
├── model-selection/  # legacy/reference model selection work
├── nn/               # legacy/reference neural network work
├── prep/             # study plan, papers, interview checklist
├── sequence/         # legacy/reference sequence model work
├── transformers/     # legacy/reference transformer work
└── trees/            # legacy/reference tree-based model work
```

The generalized folders are still useful for concept-first exploration. The
new course-first workflow lives under `campusx-course/`.

## Plan

The current plan lives in [prep/PLAN.md](prep/PLAN.md). It is now a 5-week
track:
- Wk 1: PyTorch rundown + organizing current progress.
- Wk 2-5: complete the CampusX deep learning course.

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

# install PyTorch CUDA wheels into the active environment
# use this when you want the NVIDIA CUDA 13.0 build of torch + torchvision
uv pip install --upgrade torch torchvision --index-url https://download.pytorch.org/whl/cu130

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

### PyTorch CUDA 13.0

If you need the CUDA 13.0 build of PyTorch, install the wheel set directly from
the PyTorch index after activating your environment:

```bash
uv pip install --upgrade torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

If you want to remove an existing CPU-only or mismatched install first:

```bash
uv pip uninstall torch torchvision
uv pip install --upgrade torch torchvision --index-url https://download.pytorch.org/whl/cu130
```
