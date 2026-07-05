from load_vectorstore import vectorstore

from keyword_retriever import (
    company_keyword_search,
    global_keyword_search
)

from query_analyzer import analyze_query
from query_rewriter import rewrite_query
from conversation_memory import memory
from global_retriever import global_search
# ==========================================================
# Remove Duplicate Documents
# ==========================================================

def remove_duplicates(documents):

    unique_docs = []
    seen = set()

    for doc in documents:

        key = (
            doc.metadata.get("company", ""),
            doc.metadata.get("section", ""),
            doc.page_content[:150]
        )

        if key not in seen:
            seen.add(key)
            unique_docs.append(doc)

    return unique_docs


# ==========================================================
# Prioritize Sections
# ==========================================================

def prioritize_sections(documents, sections):

    if not sections:
        return documents

    priority = []
    remaining = []

    for doc in documents:

        section = doc.metadata.get("section", "")

        if section in sections:
            priority.append(doc)
        else:
            remaining.append(doc)

    return priority + remaining


# ==========================================================
# Smart Hybrid Search
# ==========================================================

def smart_hybrid_search(query, k=5):

    rewritten_query = rewrite_query(query)

    analysis = analyze_query(rewritten_query)

    company = analysis["company"]
    intent = analysis["intent"]
    sections = analysis["sections"]

    memory.update(
        analysis,
        rewritten_query
    )

    # =====================================
    # Company Semantic Search
    # =====================================

    if company:

        company_semantic = vectorstore.similarity_search(

            query=rewritten_query,

            k=15,

            filter={
                "company": company
            }

        )

    else:

        company_semantic = []

    company_semantic = prioritize_sections(
        company_semantic,
        sections
    )

    # =====================================
    # Global Semantic Search
    # =====================================

    global_semantic = global_search(
        intent,
        rewritten_query,
        k=5
    )

    # =====================================
    # Company BM25
    # =====================================

    company_bm25 = company_keyword_search(
        rewritten_query,
        company
    )

    # =====================================
    # Global BM25
    # =====================================

    global_bm25 = global_keyword_search(
        rewritten_query,
        intent
    )

    # =====================================
    # Merge
    # =====================================

    docs = (

        company_semantic +

        company_bm25 +

        global_semantic +

        global_bm25

    )

    docs = remove_duplicates(docs)

    return docs[:k]

# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    while True:

        query = input("\nAsk Question (exit to quit): ")

        if query.lower() == "exit":
            break

        docs = smart_hybrid_search(query)

        print("\nCurrent Memory")

        print(memory.get_context())

        for i, doc in enumerate(docs, 1):

            print("\n" + "=" * 90)

            print(f"Result {i}")

            print("\nMetadata:\n")

            print(doc.metadata)

            print("\nContent:\n")

            print(doc.page_content[:500])