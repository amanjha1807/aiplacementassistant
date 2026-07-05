# AI Interview Preparation Assistant — RAG Corpus (2026)

This corpus replaces the single monolithic PDF with **one Markdown file per company** plus **separate topic files**, each carrying YAML frontmatter metadata and internal `##` headers. This structure is designed to solve PDF-chunking problems: no multi-column layout, no page-break artifacts, no OCR ambiguity — just clean UTF-8 Markdown that any text splitter (LangChain `MarkdownHeaderTextSplitter`, LlamaIndex `MarkdownNodeParser`, etc.) can chunk deterministically.

## Folder Structure

```
rag_corpus/
├── companies/
│   ├── service_based/        (9 files — TCS, Infosys, Wipro, Accenture, Cognizant,
│   │                           HCLTech, Capgemini, Tech Mahindra, LTIMindtree)
│   └── product_based/        (22 files — Google, Microsoft, Amazon, Meta, Apple,
│                               Netflix, Flipkart, Swiggy, Zomato, Paytm, PhonePe,
│                               Razorpay, CRED, Meesho, Salesforce, Atlassian, Adobe,
│                               Freshworks, Zoho, ServiceNow, Uber, Ola)
├── topics/
│   ├── dsa.md
│   ├── system_design.md
│   ├── hr.md
│   ├── projects.md               (resume/project-based interview questions)
│   ├── coding_hints.md
│   ├── voice_interaction.md
│   ├── learning_roadmaps.md
│   └── industry_trends_2026.md
└── README.md
```

31 company files + 8 topic files = 39 source documents.

## File Format (every file)

```markdown
---
company: "Google"            # (company files only)
type: "Product-based"        # or "Service-based" / "topic_file"
category: "company_experience"  # or dsa / system_design / hr / projects / etc.
tags: ["Google", "product-based", "FAANG", "big tech"]
year: 2026
source: "AI Interview Prep Assistant Knowledge Base"
---

# Title

## Section Header
Self-contained paragraph(s) for this section...

## Next Section Header
...
```

Every `##` section is written to be a complete, self-contained thought (150–350 words) — it should make sense on its own if returned as a single retrieved chunk, without depending on the previous section for context.

## Recommended Ingestion Pipeline

1. **Load** — read each `.md` file's YAML frontmatter separately from the body (e.g., `python-frontmatter` in Python, or `gray-matter` in JS).
2. **Chunk** — split the body on `##` headers (`MarkdownHeaderTextSplitter` with `headers_to_split_on=[("#", "h1"), ("##", "h2")]`). Each resulting chunk should land naturally in the 150–400 token range given how these files are written; only split further if a section runs unusually long.
3. **Attach metadata** — merge the file-level frontmatter (company, type, category, year, tags) into every chunk's metadata, plus the `h1`/`h2` header text LangChain/LlamaIndex adds automatically. This is what enables filtered retrieval like "only DSA chunks tagged Amazon" or "only 2026-tagged trend chunks."
4. **Embed** — embed the chunk text only (not the YAML frontmatter) to avoid polluting the embedding with metadata noise; keep frontmatter purely as a metadata sidecar.
5. **Index** — store in your vector DB with metadata fields: `company`, `type`, `category`, `year`, `tags`.

## Example: LangChain-style loading snippet

```python
import frontmatter
from langchain.text_splitter import MarkdownHeaderTextSplitter

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[("#", "h1"), ("##", "h2")]
)

def load_file(path):
    post = frontmatter.load(path)
    chunks = splitter.split_text(post.content)
    for chunk in chunks:
        chunk.metadata.update(post.metadata)   # merge YAML frontmatter into chunk metadata
    return chunks
```

## Extending the Corpus

To add a new company, copy any file under `companies/service_based/` or `companies/product_based/` as a template and keep the same six `##` sections (`Overview`, `Hiring Process`, `Interview Rounds`, `2026 Updates`, `Sample Candidate Experience`, `Preparation Tips`) so it merges into the same retrieval schema. To add a new DSA/HR/System Design entry, add a new `##` subsection to the relevant topic file following the existing `tags: [...]` inline convention.

## Why This Replaces the Single PDF

- No layout/column/table artifacts that break PDF text extraction.
- Deterministic chunk boundaries (`##` headers) instead of relying on page breaks or font-size heuristics.
- Per-file and per-chunk metadata for filtered retrieval (e.g., "TCS only," "DSA only," "2026-tagged only").
- Each company or topic can be updated independently without regenerating one giant document.
