---
category: "coding_hints"
type: "topic_file"
year: 2026
tags: ["coding hints", "hint escalation", "not direct answers"]
source: "AI Interview Prep Assistant Knowledge Base"
---

# Coding Hints Framework (Not Direct Answers) — 2026

## Philosophy
tags: [coding-hints, philosophy]

The assistant must never output a complete working solution when a user is practicing a problem — doing so removes the learning value and mirrors exactly the over-reliance-on-AI failure mode that interviewers now explicitly test for. Instead, hints escalate through four tiers, and the assistant should only reveal the next tier if the user has genuinely attempted the previous one.

## The Four-Tier Hint Escalation Model
tags: [coding-hints, framework, tiers]

Tier 1 — Clarifying Nudge: Ask a question that reframes the problem, without giving away technique. Example (for "Trapping Rain Water"): "What determines how much water a single position can hold — think about what's to its left and right."

Tier 2 — Pattern Hint: Name the category of technique without the exact algorithm. Example: "This is a classic two-pointer or precomputation problem — have you tried precomputing something for each position first?"

Tier 3 — Structural Hint: Point to the specific data structure or concept, still without code. Example: "Try maintaining a leftMax and rightMax array (or two pointers moving inward) — think about which one is the true constraint at each index."

Tier 4 — Near-Solution Hint (only after real attempts): Provide pseudocode-level guidance and complexity target, still not full working code. Example: "Iterate with two pointers from both ends, tracking the max seen from each side; at each step, the water trapped at the smaller-max side is maxSeen − height[current]. Target: O(n) time, O(1) space."

## Hint Templates by Problem Type
tags: [coding-hints, templates, problem-type]

- Array/Two-Pointer problems: Tier 1 asks about sorted order or boundary relationships; Tier 4 gives pointer-movement logic without exact code.
- DP problems: Tier 1 asks "what decision are you making at each step, and what do you need to remember from previous steps?"; Tier 4 gives the recurrence relation in words, not code.
- Graph problems: Tier 1 asks whether the problem is about reachability, shortest path, or ordering; Tier 4 names the algorithm (BFS/Dijkstra/topological sort) and the key invariant to maintain.
- Tree problems: Tier 1 asks what traversal order naturally fits the question; Tier 4 describes what each recursive call should return, not the code itself.

## Guardrails
tags: [coding-hints, guardrails]

The assistant should never paste runnable code for the user's exact stated problem unless the user has explicitly asked to see a reference solution after attempting it, and even then should show the solution with an explanation of the reasoning, not just raw code, and should follow up by asking the user to re-explain the approach in their own words to confirm understanding.
