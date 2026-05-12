# Paper reading list

30 min/day budget. **Skim** = first pass (abstract, intro, figures,
conclusion). **Deep** = full read with notes + a one-paragraph summary
back in this file. Mark `[x]` when done and add a one-line takeaway.

Andrew Ng's three-pass method: skim → critical read → reimplement
mentally. Use pass-1 (skim) for most papers; reserve pass-2 (deep) for
the foundational ones marked below.

## §1 — Week 1: Classical ML

- [ ] **Random Search for Hyper-Parameter Optimization** — Bergstra &
  Bengio, 2012. *skim*. Why random often beats grid.
  https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf
- [ ] **A Few Useful Things to Know about Machine Learning** — Pedro
  Domingos, 2012. *skim*. Excellent intuition primer; reads like a
  blog.
  https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf

## §2 — Week 2: Classical ML depth

- [ ] **Random Forests** — Breiman, 2001. *skim*. The bagging argument.
  https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf
- [ ] **XGBoost: A Scalable Tree Boosting System** — Chen & Guestrin,
  2016. *skim*. Why gradient boosting won tabular ML.
  https://arxiv.org/abs/1603.02754
- [ ] **SMOTE: Synthetic Minority Over-sampling Technique** — Chawla et
  al., 2002. *skim*. Class-imbalance canonical reference.
  https://arxiv.org/abs/1106.1813

## §3 — Week 3: NN + vision refresher

- [ ] **ImageNet Classification with Deep CNNs (AlexNet)** —
  Krizhevsky, Sutskever, Hinton, 2012. *skim*. The paper that started
  the deep-learning era.
  https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- [ ] **Deep Residual Learning for Image Recognition (ResNet)** — He
  et al., 2015. *skim*. Residual connections — universally used.
  https://arxiv.org/abs/1512.03385
- [ ] **Batch Normalization** — Ioffe & Szegedy, 2015. *skim*.
  https://arxiv.org/abs/1502.03167

## §4 — Week 4: Transformers

- [ ] **Attention Is All You Need** — Vaswani et al., 2017. **DEEP
  READ**. Foundation of everything LLM. Reimplement attention from
  scratch alongside the paper.
  https://arxiv.org/abs/1706.03762
- [ ] **BERT** — Devlin et al., 2018. *skim*. Encoder-only transformers
  + masked LM pretraining.
  https://arxiv.org/abs/1810.04805
- [ ] **An Image Is Worth 16x16 Words (ViT)** — Dosovitskiy et al.,
  2020. *skim*. Transformers for vision; useful crossover.
  https://arxiv.org/abs/2010.11929
- [ ] **Language Models are Few-Shot Learners (GPT-3)** — Brown et al.,
  2020. *skim*. In-context learning emerged here.
  https://arxiv.org/abs/2005.14165

## §5 — Week 5: LLM application engineering

- [ ] **Chain-of-Thought Prompting** — Wei et al., 2022. *skim*. CoT.
  https://arxiv.org/abs/2201.11903
- [ ] **ReAct: Synergizing Reasoning and Acting in Language Models** —
  Yao et al., 2022. *skim*. Foundational for tool-using agents.
  https://arxiv.org/abs/2210.03629
- [ ] **LoRA: Low-Rank Adaptation of Large Language Models** — Hu et
  al., 2021. *skim*. Parameter-efficient fine-tuning.
  https://arxiv.org/abs/2106.09685
- [ ] **Self-Consistency Improves CoT Reasoning** — Wang et al., 2022.
  *skim*. Ensemble of CoT samples.
  https://arxiv.org/abs/2203.11171

## §6 — Week 6: RAG

- [ ] **Retrieval-Augmented Generation for Knowledge-Intensive NLP** —
  Lewis et al., 2020. **DEEP READ**. The RAG paper.
  https://arxiv.org/abs/2005.11401
- [ ] **Dense Passage Retrieval (DPR)** — Karpukhin et al., 2020.
  *skim*. Dense embedding retrieval.
  https://arxiv.org/abs/2004.04906
- [ ] **ColBERTv2: Effective and Efficient Retrieval via Lightweight
  Late Interaction** — Santhanam et al., 2021. *skim*. Late-interaction
  reranking.
  https://arxiv.org/abs/2112.01488
- [ ] **RAGAS: Automated Evaluation of Retrieval Augmented Generation**
  — Es et al., 2023. *skim*. The metrics you'll actually compute.
  https://arxiv.org/abs/2309.15217

## §7 — Week 7: Vision (depth / stereo)

- [ ] **PSMNet: Pyramid Stereo Matching Network** — Chang & Chen, 2018.
  *skim*. Classic deep stereo baseline.
  https://arxiv.org/abs/1803.08669
- [ ] **RAFT-Stereo** — Lipson et al., 2021. *skim*. Modern recurrent
  refinement for stereo.
  https://arxiv.org/abs/2109.07547
- [ ] **MiDaS: Towards Robust Monocular Depth Estimation** — Ranftl et
  al., 2019. *skim*. The widely-deployed monocular baseline.
  https://arxiv.org/abs/1907.01341
- [ ] **DPT: Vision Transformers for Dense Prediction** — Ranftl et
  al., 2021. *skim*. ViT applied to depth.
  https://arxiv.org/abs/2103.13413
- [ ] **Depth Anything v2** — Yang et al., 2024. **DEEP READ**.
  Current state-of-the-art monocular depth; relevant to your project.
  https://arxiv.org/abs/2406.09414

## §8 — Week 8: RL + agents + system design

- [ ] **Playing Atari with Deep RL (DQN)** — Mnih et al., 2013.
  *skim*. The DQN paper.
  https://arxiv.org/abs/1312.5602
- [ ] **Proximal Policy Optimization (PPO)** — Schulman et al., 2017.
  *skim*. Modern policy-gradient workhorse.
  https://arxiv.org/abs/1707.06347
- [ ] **Toolformer: Language Models Can Teach Themselves to Use Tools**
  — Schick et al., 2023. *skim*. Tool-use precursor.
  https://arxiv.org/abs/2302.04761

## Bonus / recent (read if time allows)

- [ ] **DeepSeek-V3 / R1 Technical Reports** — DeepSeek, 2024–25.
  Architecture + RL post-training. Useful 2025–26 context.
- [ ] **Self-Rewarding Language Models** — Yuan et al., 2024.
  https://arxiv.org/abs/2401.10020
- [ ] **Mixture of Experts (Switch Transformer)** — Fedus et al., 2021.
  https://arxiv.org/abs/2101.03961

## Notes / takeaways log

> Add one line per paper as you finish. This becomes a research signal
> on its own — recruiters reading this file see how you think.

- _(empty — add entries as you go)_
