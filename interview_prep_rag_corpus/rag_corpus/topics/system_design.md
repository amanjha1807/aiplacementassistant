---
category: "system_design"
type: "topic_file"
year: 2026
tags: ["system design", "LLD", "HLD", "architecture", "AI systems"]
source: "AI Interview Prep Assistant Knowledge Base"
---

# System Design Question Bank — 2026

## Low-Level Design (LLD)
tags: [system-design, lld, oop, design-patterns]

Core focus: OOP principles, SOLID, design patterns, class diagrams, extensibility.

1. Design a parking lot system (classes, extensibility for new vehicle types).
2. Design a library management system.
3. Design an elevator/lift control system.
4. Design a rate limiter (token bucket / sliding window counter) at the class level.
5. Design a movie ticket booking system with seat-locking logic.
6. Design a chess game (board representation, move validation, turn management).
7. Design a logging framework with pluggable output destinations.

Concepts interviewers probe: single responsibility, open-closed principle, composition over inheritance, interface segregation, and how the design handles a plausible future requirement change. Companies that weight LLD heavily: Salesforce, Atlassian, Razorpay, Zoho.

## High-Level Design (HLD)
tags: [system-design, hld, scalability, distributed-systems]

Core focus: scalability, availability, consistency trade-offs, data partitioning, caching, load balancing.

1. Design a URL shortener (like Bit.ly) — asked almost everywhere as a baseline HLD question.
2. Design a news feed system (like Instagram/Facebook feed) — fan-out on write vs read trade-offs.
3. Design WhatsApp/a chat application — message delivery guarantees, online-status, group chat scaling.
4. Design Uber/Ola — driver-rider matching, geo-indexing, surge pricing.
5. Design Netflix/a video streaming service — CDN usage, adaptive bitrate, recommendation pipeline at a high level.
6. Design a distributed rate limiter for an API gateway.
7. Design an e-commerce checkout and inventory system — handling flash-sale concurrency (Flipkart Big Billion Days-style scenario).
8. Design a notification system (push, SMS, email) at scale.
9. Design a distributed cache (like Redis) — eviction policies, consistency.
10. Design a search autocomplete system — Trie-based backend combined with ranking.

## 2026-Specific System Design Questions (AI/LLM Systems)
tags: [system-design, ai-systems, rag, llm, vector-database, 2026]

This category has become common at both product-based companies (as a direct AI-systems question) and increasingly at service-based companies for AI-delivery roles.

1. Design a Retrieval-Augmented Generation (RAG) pipeline for a customer-support chatbot — cover document ingestion, chunking strategy, embedding generation, vector storage, retrieval, and re-ranking before the LLM call.
2. Design a vector database at a high level — indexing strategy (HNSW/IVF), approximate nearest neighbor trade-offs, metadata filtering.
3. Design an LLM inference-serving system — batching requests, GPU utilization, latency vs throughput trade-offs, caching repeated prompts.
4. Design an AI agent orchestration system that can call multiple tools/APIs reliably — cover retries, tool-call validation, and guarding against infinite loops.
5. Design a content-moderation pipeline that combines a fast classical filter with an LLM-based second pass for ambiguous cases.
6. Design a system to detect and rate-limit abuse of a public LLM-powered API (prompt injection defenses, cost control per user).

## System Design Answer Structure Checklist
tags: [system-design, guidance, framework]

A well-structured system design answer moves through: (1) clarify requirements and scale (users, QPS, data volume), (2) define the high-level API/entities, (3) propose a high-level architecture diagram in words, (4) deep-dive into the 1–2 hardest components, (5) discuss trade-offs explicitly (consistency vs availability, latency vs cost), and (6) mention bottlenecks and how you'd address them at 10x scale.
