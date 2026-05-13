# InfinitiBit Mid-Level AI Engineer Interview Self-Assessment Checklist

Target interview: **July 2026, InfinitiBit GmbH (Munich / Dhaka)** — banking, automotive, audit, energy verticals; flagship product is **GraphBit** (Rust + Python agentic framework). Question pool is curated from real 2025-2026 interview reports (Adil Shamim's "100+ Real Interviews" compilation, Alexey Grigorev's `ai-engineering-field-guide`, LockedinAI Top 50, DataCamp RAG / Agentic AI / MLOps / LLM banks, Devinterview-io XGBoost/LightGBM, recent Medium and Glassdoor write-ups).

Difficulty tags: `[basic]` answerable by end of weeks 1-2 · `[mid]` weeks 3-6 · `[hard]` weeks 7-8 polish.

---

## 1. Classical ML & Statistics (15)

**Study tips:** Financial/audit interviews still lean hard on tabular ML — XGBoost/LightGBM almost always comes up. Don't just memorize formulas; be ready to *defend choices* (why log-loss over accuracy, why ROC-AUC misleads on imbalanced data, when calibration matters). Commonly missed: the difference between probability calibration and discrimination, and why scale_pos_weight is not the same as resampling.

- [ ] Explain the bias-variance tradeoff and show how it manifests in a learning curve. `[basic]`
- [ ] Compare L1, L2, and ElasticNet regularization — when does each zero out coefficients vs. shrink them? `[basic]`
- [ ] Walk through k-fold, stratified k-fold, and time-series CV. When does each break? `[basic]`
- [ ] Define precision, recall, F1, and explain when F1 misleads you. `[basic]`
- [ ] When is ROC-AUC misleading and PR-AUC preferred? `[mid]`
- [ ] Derive logistic regression's loss function and explain why it's convex. `[mid]`
- [ ] How do XGBoost and LightGBM differ in tree growth (level-wise vs leaf-wise) and what are the practical consequences? `[mid]`
- [ ] Explain `scale_pos_weight` in XGBoost and how it differs from SMOTE or undersampling. `[mid]`
- [ ] How would you handle a fraud-detection dataset with 0.1% positives? List at least four strategies. `[mid]`
- [ ] What is probability calibration? When would you use Platt scaling vs isotonic regression? `[mid]`
- [ ] Explain SHAP vs LIME — what does each actually compute, and where does each fail? `[mid]`
- [ ] Why are gradient-boosted trees usually preferred over neural networks for tabular data? `[mid]`
- [ ] How would you diagnose whether a model is overfitting, underfitting, or has a data leak? `[mid]`
- [ ] Explain bootstrapping and how it underlies bagging and confidence intervals. `[hard]`
- [ ] You have two models with identical AUC but different Brier scores — which do you ship for a credit-risk product, and why? `[hard]`

## 2. Data Preprocessing & Feature Engineering (10)

**Study tips:** Leakage is the #1 thing interviewers probe — they will deliberately describe a workflow with subtle leakage and ask you to find it. Master `sklearn.Pipeline` + `ColumnTransformer` end to end; being able to write one on a whiteboard separates seniors from juniors. Often missed: target encoding's leakage trap and the right place to fit scalers (inside the CV loop, not before it).

- [ ] When do you impute with mean vs median vs a learned model, and when is `MissingIndicator` worth adding? `[basic]`
- [ ] Compare one-hot, ordinal, target, and frequency encoding for high-cardinality categoricals. `[basic]`
- [ ] When is StandardScaler wrong and you should use RobustScaler or QuantileTransformer instead? `[basic]`
- [ ] Write a `Pipeline` + `ColumnTransformer` that scales numerics, one-hot encodes categoricals, and feeds a classifier — what bug does this prevent? `[mid]`
- [ ] Define train-test contamination and give three concrete ways it sneaks in. `[mid]`
- [ ] Why must target encoding be done inside the CV fold? Show how it leaks if done before splitting. `[mid]`
- [ ] How do you engineer features for a time series without leaking the future? `[mid]`
- [ ] You have 200 features, mostly correlated. Walk through your feature-selection strategy. `[mid]`
- [ ] How would you detect distribution shift between training and serving data? `[mid]`
- [ ] When is feature engineering pointless and you should let the model learn representations? `[hard]`

## 3. Neural Network Fundamentals (15)

**Study tips:** Expect to derive backprop on a 2-layer net by hand and explain *why* batch-norm helps (the answer is no longer "internal covariate shift" — be ready for that). PyTorch idioms are tested in code rounds: `nn.Module`, `register_buffer`, `state_dict`, autograd graph, `.detach()` vs `.no_grad()`. Often missed: initialization math (Xavier vs Kaiming) and what actually goes wrong with vanishing gradients in deep ReLU nets.

- [ ] Derive backpropagation for a 2-layer MLP with sigmoid activation. `[basic]`
- [ ] Compare SGD, SGD-momentum, RMSprop, and Adam — when does Adam fail? `[basic]`
- [ ] What does dropout actually do at train vs inference time? `[basic]`
- [ ] Explain batch normalization, layer normalization, and group normalization — when do you pick which? `[mid]`
- [ ] What is weight decay, and how does it differ from L2 regularization in Adam (decoupled weight decay / AdamW)? `[mid]`
- [ ] Compare Xavier and Kaiming initialization — when does each apply? `[mid]`
- [ ] What causes vanishing and exploding gradients, and how do residual connections fix it? `[mid]`
- [ ] Implement a forward + backward pass of a single linear layer in NumPy. `[mid]`
- [ ] Explain `torch.autograd` — what is a leaf tensor, what does `retain_graph=True` do? `[mid]`
- [ ] Difference between `model.eval()`, `torch.no_grad()`, and `torch.inference_mode()`. `[mid]`
- [ ] What is gradient checkpointing and when is it worth the compute trade? `[mid]`
- [ ] You train a CNN and loss goes to NaN at epoch 3. Walk through the debug. `[mid]`
- [ ] Compare cross-entropy, focal loss, and label smoothing — when does each help? `[mid]`
- [ ] Why is mixed-precision (fp16/bf16) training faster and what numerical traps does it introduce? `[hard]`
- [ ] You have batch size 2 on an RTX 3050 and want to act like batch 32 — describe gradient accumulation and its caveats with batch norm. `[hard]`

## 4. Transformers & Attention (15)

**Study tips:** Be ready to *write* scaled dot-product attention in PyTorch from memory in 10 minutes — this is a 2026 staple. Know the math (why divide by sqrt(d_k)) and the engineering (KV cache, why decoder-only dominates). Often missed: the difference between absolute, learned, and rotary (RoPE) positional encodings, and why GQA/MQA matter for inference cost.

- [ ] Write scaled dot-product attention from memory in PyTorch. `[basic]`
- [ ] Why divide by sqrt(d_k) in attention? What happens without it? `[basic]`
- [ ] Explain multi-head attention — why multiple heads instead of one larger one? `[basic]`
- [ ] Compare absolute, learned, sinusoidal, and rotary (RoPE) positional encodings. `[mid]`
- [ ] What is the KV cache and why is LLM inference memory-bound because of it? `[mid]`
- [ ] Encoder-only vs decoder-only vs encoder-decoder — give one task best suited to each. `[mid]`
- [ ] Why has the field converged on decoder-only architectures even for non-generation tasks? `[mid]`
- [ ] Compare BPE, WordPiece, SentencePiece, and character-level tokenization. `[mid]`
- [ ] What goes wrong when you apply a general-purpose tokenizer to code, math, or Bengali text? `[mid]`
- [ ] Explain top-k, top-p (nucleus), temperature, and beam search sampling. When set temperature=0? `[mid]`
- [ ] Implement greedy decoding and top-p sampling in PyTorch. `[mid]`
- [ ] What is Grouped-Query Attention (GQA) and Multi-Query Attention (MQA), and why do they matter at inference? `[hard]`
- [ ] Explain FlashAttention at a high level — what does it fuse and why is it faster? `[hard]`
- [ ] What is speculative decoding and why does it speed up generation? `[hard]`
- [ ] Walk through Mixture-of-Experts — routing, load-balancing loss, why it improves throughput per parameter. `[hard]`

## 5. LLM Application Engineering — RAG, Agents, Fine-tuning (20)

**Study tips:** This is the dominant section for InfinitiBit since GraphBit is an agent framework. Expect ~75% of LLM questions to be RAG + agents. Memorize a *production-ready agent architecture diagram* and a *RAG failure-mode taxonomy* (bad chunking, embedding domain mismatch, retriever recall vs reader precision, lost-in-the-middle, citation hallucination). Often missed: when *not* to use agents (most "agent" problems are deterministic workflows), and the cost math of multi-step tool calls.

- [ ] Explain the full RAG pipeline: ingest, chunk, embed, store, retrieve, rerank, generate. `[basic]`
- [ ] Decide: fine-tuning vs prompt engineering vs RAG — give the decision tree. `[basic]`
- [ ] Compare BM25, dense retrieval, and hybrid search. When does hybrid win? `[basic]`
- [ ] What is a reranker and why add one on top of vector retrieval? `[mid]`
- [ ] Walk through chunking strategies: fixed-size, recursive, semantic, late chunking, parent-document. Pros and cons. `[mid]`
- [ ] How do you pick an embedding model? What benchmarks (MTEB) do you trust and which do you not? `[mid]`
- [ ] Compare pgvector, Qdrant, Pinecone, Weaviate, and Chroma — when does each win? `[mid]`
- [ ] Explain RAGAS metrics (faithfulness, answer relevance, context precision/recall) and where they each break. `[mid]`
- [ ] How do you defend against prompt injection in a tool-using agent? `[mid]`
- [ ] Compare CoT, self-consistency, ReAct, and Reflexion prompting. When is plain CoT enough? `[mid]`
- [ ] Explain LoRA: which matrices get adapters, rank trade-off, how merging works at inference. `[mid]`
- [ ] Compare LoRA, QLoRA, full fine-tuning, and adapters by VRAM, quality, and serving cost. `[mid]`
- [ ] Design tool/function schemas that minimize hallucinated arguments. What do good schemas look like? `[mid]`
- [ ] How do you handle a financial PDF where page 1 says "all amounts in thousands" and the agent must respect that across all pages? `[mid]`
- [ ] What memory types does an agent need (short-term, long-term, episodic, semantic, procedural) and how do you keep long-term memory from polluting? `[mid]`
- [ ] When is an agentic architecture the WRONG solution — give two concrete examples. `[hard]`
- [ ] Design a multi-turn RAG system that maintains conversation context without blowing up the context window. `[hard]`
- [ ] Scale a RAG system from 10K to 10M documents — what changes in indexing, retrieval, and reranking? `[hard]`
- [ ] How do you implement deterministic tracing and replay for a non-deterministic LLM agent? `[hard]`
- [ ] Your RAG chatbot returns relevant documents but users still don't find answers. Walk through diagnosis. `[hard]`

## 6. Computer Vision — incl. Depth & Stereo (10)

**Study tips:** Automotive vertical at InfinitiBit makes stereo/depth a real possibility. Know the classical pipeline (rectification → matching cost → cost aggregation → disparity → refinement) so you can place RAFT-Stereo and MiDaS within it. Often missed: monocular depth is *relative/scale-shift-invariant* unless you fine-tune for metric depth, and the cost-volume idea behind modern stereo nets.

- [ ] Explain convolution, stride, padding, dilation, and receptive field. `[basic]`
- [ ] Why are residual connections in ResNet necessary for depths > 30? `[basic]`
- [ ] Walk through transfer learning on ImageNet — what do you freeze and what do you fine-tune? `[basic]`
- [ ] Compare ViT and CNN — what does each see, and where does ViT struggle on small datasets? `[mid]`
- [ ] Design an augmentation pipeline for a small (5K image) automotive classification dataset. `[mid]`
- [ ] Monocular vs stereo depth — what is each fundamentally able to recover (scale, metric, relative)? `[mid]`
- [ ] Walk through classical block matching and Semi-Global Matching (SGM) for stereo. `[mid]`
- [ ] How does RAFT-Stereo replace cost aggregation with iterative recurrent updates? `[hard]`
- [ ] Compare MiDaS, DPT, and Depth Anything — training data, output type, zero-shot behavior. `[hard]`
- [ ] You want metric depth for an autonomous-car perception stack. Stereo rig vs monocular foundation model vs LiDAR fusion — defend a choice. `[hard]`

## 7. MLOps, Deployment & Observability (15)

**Study tips:** Banking and audit verticals at InfinitiBit mean monitoring/governance questions are likely. Know the difference between data drift, concept drift, and label drift, and how each is detected. For LLM serving, vLLM vs TGI vs Triton vs SGLang is a 2026 favorite. Often missed: continuous batching is what makes vLLM fast (not just paged attention), and prompt caching is a *first-class cost lever*, not an afterthought.

- [ ] Containerize a FastAPI + PyTorch model with Docker — what goes in the image, what stays out? `[basic]`
- [ ] Walk through MLflow's four components (tracking, projects, models, registry). `[basic]`
- [ ] Batch vs real-time inference — when do you pick each, and what does "near-real-time" actually mean? `[basic]`
- [ ] Design a CI pipeline that runs unit tests, model evals, and only promotes if AUC drops < 1%. `[mid]`
- [ ] Define data drift, concept drift, and label drift. How do you detect each in production? `[mid]`
- [ ] When do you need a feature store (e.g., Feast) and when is it overkill? `[mid]`
- [ ] Compare vLLM, TGI, Triton, and SGLang for serving LLMs. `[mid]`
- [ ] What is continuous batching and why does vLLM throughput beat naive batching? `[mid]`
- [ ] Explain Anthropic / OpenAI prompt caching — where do cache breakpoints go and what's the cost model? `[mid]`
- [ ] Design an A/B test for a new prompt in production — what's your stopping rule? `[mid]`
- [ ] How do you do canary deploys for an LLM-backed product where outputs are non-deterministic? `[mid]`
- [ ] What does Langfuse (or LangSmith / Arize Phoenix) give you that plain logging doesn't? `[mid]`
- [ ] Your LLM API bill is 3x last month. Walk through cost diagnosis and at least five mitigations. `[hard]`
- [ ] Design end-to-end observability for an agent: traces, spans, evals, alerts. `[hard]`
- [ ] How do you build a golden eval set and keep it from going stale as the product evolves? `[hard]`

## 8. Python / Coding (10)

**Study tips:** AI companies still ask LeetCode-style problems but with an ML/AI twist — LRU cache (because every LLM serving stack has one), Trie (because of tokenizers), graph traversal (because of agent DAGs). Know `asyncio` because batching LLM calls in production is async-first. Often missed: the GIL doesn't block I/O, so async + threads work fine for API calls; only CPU-bound work needs multiprocessing.

- [ ] Explain the GIL — what does it block and what does it not? `[basic]`
- [ ] Difference between `list`, `tuple`, `set`, `dict` time complexities. `[basic]`
- [ ] Write a generator that streams a file line-by-line and yields parsed JSON. `[basic]`
- [ ] Implement cosine similarity in NumPy without `np.linalg.norm`. `[basic]`
- [ ] Implement an LRU cache with O(1) get and put. `[mid]`
- [ ] Build a Trie and add a method `starts_with(prefix)`. `[mid]`
- [ ] Write an `async` function that calls an LLM API for 100 prompts with a concurrency limit of 10. `[mid]`
- [ ] Explain Python's reference counting and when garbage collection actually runs. `[mid]`
- [ ] Implement topological sort for an agent's tool-dependency DAG. `[mid]`
- [ ] Implement a token-bucket rate limiter for an LLM API client. `[hard]`

## 9. AI System Design (10)

**Study tips:** Expect at least one open-ended system design round. Always start by clarifying scale, latency SLO, cost ceiling, and freshness. Sketch the diagram (ingest → retrieve → rerank → generate → guardrail → observe), then go deep on one bottleneck the interviewer picks. Often missed: explicit failure modes and graceful degradation (what does the system return when the LLM is down?).

- [ ] Design a RAG system for a bank's customer-support chatbot serving 1M users/day. `[mid]`
- [ ] Design a real-time LLM inference service with a hard $X / month cost ceiling. `[mid]`
- [ ] Design a semantic search system over 10M legal/audit documents with citations. `[mid]`
- [ ] Design a fraud-detection pipeline mixing GBM scoring with an LLM rationale generator. `[mid]`
- [ ] Design a personalized recommendation system for an e-commerce catalog with cold-start. `[mid]`
- [ ] Design an agentic workflow that ingests an audit PDF, extracts findings, and drafts a remediation plan with human review. `[hard]`
- [ ] Design a hybrid retrieval system combining BM25 and dense vectors at billion-document scale. `[hard]`
- [ ] Design an LLM-powered SQL assistant where wrong answers are unacceptable. How do you make it safe? `[hard]`
- [ ] Design a multi-tenant agent platform (à la GraphBit) — isolation, billing, observability, secrets. `[hard]`
- [ ] Your p99 latency went from 800ms to 4s overnight on a RAG service. Walk through diagnosis. `[hard]`

## 10. Behavioral / Project Walkthrough (STAR) (10)

**Study tips:** Prepare 3-4 STAR stories that cover: (a) a technically hard project you owned end-to-end, (b) a cost/latency optimization, (c) a hallucination/eval story, (d) a cross-functional conflict. Senior interviewers probe with "is the eval framework real or vibes-based?" — have a real answer. Often missed: STAR's Result should include a *number* (latency dropped X%, cost cut Y%, accuracy up Z points).

- [ ] Walk me through an AI project you built end-to-end — business problem, role, decisions, result. `[basic]`
- [ ] Tell me about a time you reduced LLM cost or latency in production — include the metric. `[basic]`
- [ ] Describe a challenging prompt-engineering or RAG-tuning problem and what you tried before it worked. `[mid]`
- [ ] Tell me about a time you reduced hallucinations in a production LLM app. `[mid]`
- [ ] Describe a time you disagreed with a teammate or stakeholder on a model choice. How did it resolve? `[mid]`
- [ ] Tell me about a project where your AI solution failed — what did you learn? `[mid]`
- [ ] How do you stay current with the AI field given how fast it moves? `[mid]`
- [ ] Describe a time you explained a complex ML/LLM concept to a non-technical stakeholder. `[mid]`
- [ ] Tell me about a safety-first decision you made on an AI project. `[hard]`
- [ ] Why InfinitiBit and why now? What about GraphBit and the agentic-framework space draws you? `[hard]`

---

## How to use this checklist

- Tick a box only when you can answer the question out loud, unprompted, in under 3 minutes.
- Revisit unchecked items every Sunday — don't let a section go cold for more than 10 days.
- Weekly targets against the 8-week plan: **Wk 2: 25%** (basics across all sections) · **Wk 4: 50%** · **Wk 6: 75%** · **Wk 7: 90%** · **Wk 8: 100% + mock interviews on weak sections.**
- For sections 5 (LLM/RAG/Agents) and 9 (System Design) — InfinitiBit's core ground — aim 1 week ahead of the schedule above.
