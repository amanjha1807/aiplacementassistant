---
category: "dsa"
type: "topic_file"
year: 2026
tags: ["DSA", "data structures", "algorithms", "coding interview"]
source: "AI Interview Prep Assistant Knowledge Base"
---

# DSA (Data Structures & Algorithms) Question Bank — 2026

## Overview
Questions below are grouped by topic. Each topic section lists core concepts, a representative question set spanning Easy to Hard, and company tags indicating where each pattern is commonly asked. In 2026, interviewers weight approach explanation and complexity trade-off reasoning more heavily than raw memorized solutions, because AI coding assistants have made "getting a working solution" less differentiating than "explaining why this solution is correct and optimal."

## Arrays & Strings
tags: [dsa, arrays, strings, easy, medium, hard]

Core concepts: two-pointer technique, prefix sums, sliding window, in-place manipulation, sorting-based tricks.

1. [Easy] Move all zeros to the end of an array while preserving order — asked at TCS, Infosys, Amazon.
2. [Easy] Find the maximum subarray sum (Kadane's Algorithm) — asked almost universally across service and product companies.
3. [Medium] Longest substring without repeating characters — asked at Microsoft, Flipkart, Adobe.
4. [Medium] Merge overlapping intervals — asked at Google, Uber, Razorpay.
5. [Medium] Find all pairs in an array with a given sum, optimized to O(n) — asked at Cognizant, Wipro, Paytm.
6. [Hard] Trapping rain water — asked at Amazon, Meta, Zoho.
7. [Hard] Minimum window substring — asked at Google, Microsoft.

## Linked Lists
tags: [dsa, linked-lists, easy, medium, hard]

Core concepts: fast-slow pointers, reversal in groups, cycle detection.

1. [Easy] Reverse a singly linked list, iterative and recursive — universal.
2. [Medium] Detect and remove a cycle in a linked list (Floyd's algorithm) — asked at TCS Digital, Amazon.
3. [Medium] Merge two sorted linked lists — asked at Infosys SP, Flipkart.
4. [Hard] Reverse nodes in k-group — asked at Microsoft, Adobe.
5. [Hard] Flatten a multilevel doubly linked list — asked at Meta, Salesforce.

## Stacks & Queues
tags: [dsa, stacks, queues, easy, medium, hard]

Core concepts: monotonic stacks, queue-based simulation, design problems.

1. [Easy] Valid parentheses matching — universal.
2. [Medium] Next greater element using a monotonic stack — asked at Wipro, Cognizant, Ola.
3. [Medium] Implement a queue using two stacks (and vice versa) — common at service companies.
4. [Hard] Sliding window maximum using a deque — asked at Google, Amazon.

## Trees & Binary Search Trees
tags: [dsa, trees, bst, easy, medium, hard]

Core concepts: traversals, height/balance checks, LCA, BST properties.

1. [Easy] Level-order traversal (BFS) of a binary tree — universal.
2. [Medium] Lowest common ancestor in a BST and in a general binary tree — asked at Amazon, Flipkart, Zoho.
3. [Medium] Validate a binary search tree — asked at Microsoft, Adobe.
4. [Hard] Serialize and deserialize a binary tree — asked at Google, Meta.
5. [Hard] Construct a binary tree from inorder and preorder traversal — asked at Infosys SP, TCS Digital.

## Graphs
tags: [dsa, graphs, easy, medium, hard]

Core concepts: BFS/DFS, shortest path, topological sort, union-find, minimum spanning tree.

1. [Easy] Number of islands (grid DFS/BFS) — universal, especially at logistics companies.
2. [Medium] Course schedule / detect cycle via topological sort — asked at Amazon, Google, Uber.
3. [Medium] Dijkstra's shortest path — asked at Ola, Uber, Swiggy for ETA-style problems.
4. [Hard] Alien dictionary (topological sort on characters) — asked at Google, Microsoft.
5. [Hard] Minimum spanning tree via Kruskal's/Prim's with union-find — asked at Meta, cloud infra teams.

## Dynamic Programming
tags: [dsa, dynamic-programming, easy, medium, hard]

Core concepts: state definition, transition, memoization vs tabulation, space optimization.

1. [Easy] Fibonacci with memoization, climbing stairs — universal warm-up.
2. [Medium] Longest common subsequence — asked at TCS, Infosys, Accenture.
3. [Medium] 0/1 Knapsack and its variants — asked at Amazon, Flipkart, Paytm.
4. [Hard] Edit distance — asked at Google, Adobe.
5. [Hard] Longest increasing subsequence in O(n log n) — asked at Meta, Microsoft.
6. [Hard] Word break with backtracking optimization — asked at Google, Salesforce.

## Greedy Algorithms
tags: [dsa, greedy, easy, medium, hard]

1. [Easy] Activity selection / interval scheduling — common at service companies.
2. [Medium] Job sequencing with deadlines — asked at Wipro, Cognizant.
3. [Medium] Minimum number of platforms/meeting rooms required — asked at Amazon, Ola.
4. [Hard] Huffman encoding — asked at product companies with a compression/media focus (Adobe, Netflix).

## Backtracking
tags: [dsa, backtracking, medium, hard]

1. [Medium] N-Queens problem — asked at Google, Microsoft.
2. [Medium] Generate all permutations/subsets — universal.
3. [Hard] Sudoku solver — asked at Adobe, Meta.
4. [Hard] Word search in a grid — asked at Amazon, Flipkart.

## Heaps / Priority Queues
tags: [dsa, heaps, priority-queue, medium, hard]

1. [Medium] Kth largest element in a stream — asked at Amazon, Razorpay.
2. [Medium] Merge k sorted lists — asked at Microsoft, Google.
3. [Hard] Find median from a data stream using two heaps — asked at Meta, Flipkart.

## Tries & Bit Manipulation
tags: [dsa, tries, bit-manipulation, easy, medium]

1. [Medium] Implement a Trie with insert/search/startsWith — asked at Google, Adobe (autocomplete-related).
2. [Medium] Longest word in a dictionary formed by prefixes — asked at product companies with search features.
3. [Easy] Single number (XOR trick) — common warm-up across all companies.
4. [Medium] Count set bits, power of two checks — common at service-based aptitude-adjacent coding rounds.

## 2026-Specific DSA Trend
tags: [dsa, trend, 2026, ai]

A growing share of technical interviews now include a short "debug the AI-generated solution" segment: the interviewer shows a plausible-looking but subtly incorrect solution (often with an off-by-one error, wrong base case, or missed edge case) and asks the candidate to find and fix the bug under time pressure. Practicing code review of imperfect solutions — not just writing from scratch — is now a distinct, valuable prep activity.
