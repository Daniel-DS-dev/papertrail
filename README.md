# papertrail
Turn photographed documents into a queryable knowledge base — OCR → structured extraction → RAG Q&amp;A, with a measured eval harness


## Status

**Phase 0 complete** — project skeleton, FastAPI scaffold with health endpoint, tests passing, uv-managed environment with src layout.

Currently working on: **Phase 1 — OCR pipeline** (PaddleOCR vs docTR bake-off on the SROIE receipt dataset).

## Roadmap

- [x] **Phase 0 — Skeleton:** repo structure, FastAPI app, pytest, uv + src layout
- [ ] **Phase 1 — OCR spine:** engine bake-off, text + bounding-box extraction, `POST /documents`
- [ ] **Phase 2 — Structured extraction:** local LLM (Ollama) → Pydantic schema, MLflow-tracked accuracy eval on SROIE
- [ ] **Phase 3 — RAG:** chunking, embeddings + Qdrant, retrieval, cited Q&A, retrieval eval (hit@3 / MRR)
- [ ] **Phase 4 — Ops:** docker-compose full stack, Kubernetes manifests, Prometheus metrics + Grafana dashboard, CI
- [ ] **Phase 5 — Results:** eval results table, architecture diagram, demo