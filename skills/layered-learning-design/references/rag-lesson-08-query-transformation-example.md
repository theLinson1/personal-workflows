# RAG Lesson 08 Query Transformation Example

> Portable handoff note (2026-09-22): This is a historical teaching example. The external course files, scripts, reports, commands, and observations described below are not bundled here and were not rerun during packaging. Use its instructional structure; verify or obtain the original artifacts before claiming the commands run or results hold in the current workspace.

This reference shows how Lesson 08 Query Transformation fits the layered learning design method for an engineering RAG topic.

## Contents

1. Lesson role
2. Previous capability
3. Current bottleneck
4. Capability increment
5. Teaching fixture
6. Hands-on task and report validation
7. Concept-to-code mapping
8. Production transfer bridge
9. Next lesson transition

## Lesson Role

Lesson 08 teaches what happens before retrieval.

The learner has already seen retrieval and post-retrieval improvements. Lesson 08 introduces query transformation as the primary capability increment for a new bottleneck: raw user queries can be too vague for retrieval.

## Previous Capability

The learner already understands:

- Chunking.
- BM25.
- Embedding retrieval at a conceptual level.
- Fusion.
- Reranking.
- Contextual compression.

The previous concrete capability is represented by:

- `projects/agent-lab/scripts/rerank_contextual_compression.py`

That lesson assumes the query already expresses enough intent.

## Current Bottleneck

The raw query is:

```text
users say they have no access after deploy
```

The query is clear enough for a human support engineer. It is too vague for simple retrieval.

The retrieval problem is expression mismatch:

- The query uses support-ticket words.
- The target evidence uses domain words.
- Raw retrieval prefers deployment and access symptom sections.
- The target auth section is not in top-k.

## Capability Increment

Lesson 08 introduces query transformation.

The capability increment is not a production query pipeline. It is the ability to compare how retrieval input changes retrieval results under controlled conditions:

- Same corpus.
- Same chunking.
- Same search function.
- Different retrieval input.
- Reported target rank before and after transformation.

The lesson compares three variants:

- Query rewrite.
- Multi-query.
- HyDE-style hypothetical document.

These variants belong in one lesson because they share the same prerequisite knowledge, capability goal, corpus, search function, and target-rank report.

The query trace is the common evidence artifact. Query drift is treated as a boundary and diagnostic risk, not as a separate capability increment.

## Teaching Fixture

The fixture is:

```text
projects/agent-lab/data/samples/lesson-08/api-auth-playbook.md
```

Label: `teaching fixture`.

It contains deliberately confusable sections:

- Static Asset Access After Deploy.
- Login Page Copy And Support Tickets.
- FastAPI OAuth2 Bearer Token Validation.
- Admin Role Authorization.
- Deployment Proxy Headers.

The answer-bearing target is:

```text
FastAPI OAuth2 Bearer Token Validation
```

This fixture proves:

- Raw support-ticket wording can retrieve the wrong section.
- Domain terms can change target rank.
- Query trace makes transformation inspectable.

This fixture cannot prove:

- A production LLM rewriter is reliable.
- A production embedding model improves recall.
- Query transformation is safe for every vague query.
- Query drift is solved.
- Latency and cost are acceptable.

It simplifies production reality:

- No LLM.
- No embedding API.
- No vector database.
- No production query classifier.
- No online traffic.
- Hardcoded transformations.

## Hands-On Task

The learner runs:

```powershell
python projects\agent-lab\scripts\query_transformation.py
```

The learner opens:

```text
projects/agent-lab/reports/query-transformation.md
```

The learner answers:

- Why did raw retrieval choose Static Asset Access After Deploy?
- Why did query rewrite move the target section to rank 1?
- How does multi-query differ from one long query?
- Why is the HyDE document not evidence?
- Where could query drift occur?

## Report Validation

The report is:

```text
projects/agent-lab/reports/query-transformation.md
```

The validation fields are:

- `raw_target_rank`.
- `rewritten_target_rank`.
- `multi_query_target_rank`.
- `hyde_target_rank`.
- `query_drift_risk`.
- `Query Trace`.

The source reference recorded the following historical report result (not verified by this handoff):

- `raw_target_rank`: `not-in-top-k`.
- `rewritten_target_rank`: `1`.
- `multi_query_target_rank`: `1`.
- `hyde_target_rank`: `1`.
- `teaching_fixture`: `true`.
- `generated_by_llm`: `false`.
- `external_embedding_model`: `false`.

The validation standard is:

- The target rank improves after transformed retrieval input.
- The trace shows raw query, rewritten query, multi-query variants, and HyDE document.
- The learner can explain why transformation helped and where it may drift.

## Concept-To-Code Mapping

### Files

- Lesson text: `lessons/08-query-transformation/lesson.md`.
- Fixture: `projects/agent-lab/data/samples/lesson-08/api-auth-playbook.md`.
- Script: `projects/agent-lab/scripts/query_transformation.py`.
- Report: `projects/agent-lab/reports/query-transformation.md`.

### Data Structures

- `TransformCase`: stores the teaching case.
- `SearchResult`: stores one search result and matched terms.
- `MultiQueryResult`: stores RRF-fused multi-query results.

### Fields

- `case_id`: stable case label.
- `raw_query`: original vague query.
- `rewritten_query`: hardcoded rewrite.
- `multi_queries`: hardcoded query variants.
- `hyde_document`: hardcoded hypothetical document.
- `target_heading_contains`: target section label.
- `lesson`: explanation of the bad case.
- `rank`, `score`, `rrf_score`, `matched_terms`, `variant_ranks`: validation fields.

### Functions

- `load_fixture_chunks`: loads the teaching fixture.
- `tokenize`: normalizes terms.
- `search`: retrieves chunks for one query expression.
- `multi_query_search`: runs each variant and fuses results with RRF.
- `target_rank`: finds the target section rank.
- `query_trace`: records raw query and transformed expressions.
- `build_report`: produces the before/after report.
- `main`: writes the report.

### Commands

```powershell
python projects\agent-lab\scripts\query_transformation.py
```

### Report

- `projects/agent-lab/reports/query-transformation.md`.

### Metrics

- `raw_target_rank`.
- `rewritten_target_rank`.
- `multi_query_target_rank`.
- `hyde_target_rank`.
- `query_variant_count`.
- `rrf_k_for_multi_query`.
- `top_k`.
- `per_query_top_k`.

### Trace

- Raw query.
- Rewritten query.
- Multi-query variants.
- HyDE document.

## Production Transfer Bridge

The production-shaped bridge is:

- Query transformation is a retrieval pre-processing stage.
- The raw path must be preserved.
- Transformed paths need trace.
- Clarifying question is a valid outcome when intent is unclear.
- Offline eval must check recall, MRR, target rank delta, drift rate, latency, and cost.
- Online rollout must track helpfulness, fallback rate, handoff rate, cache hit rate, and rollback path.

Production options include:

- Standalone question rewrite.
- Multi-query retrieval.
- HyDE.
- Query decomposition.
- Metadata and filter extraction.
- Raw plus transformed dual-path retrieval.
- Drift guard.
- Clarifying question fallback.

Use `pseudocode` when showing production pipelines unless the real production code exists in the repo.

## Next Lesson Transition

Lesson 08 proves that changing retrieval input can improve a constructed bad case.

The next bottleneck is evaluation:

```text
How do we prove retrieval changes improve the system across cases?
```

This leads to Lesson 09 Retrieval Eval Harness.
