from load_vectorstore import vectorstore
from keyword_retriever import bm25_retriever
from query_analyzer import analyze_query


# =====================================================
# Remove Duplicate Documents
# =====================================================

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


# =====================================================
# Prioritize Important Sections
# =====================================================

def prioritize_sections(documents, sections):

    if not sections:
        return documents

    priority_docs = []
    remaining_docs = []

    for doc in documents:

        section = doc.metadata.get("section", "")

        if section in sections:
            priority_docs.append(doc)

        else:
            remaining_docs.append(doc)

    return priority_docs + remaining_docs


# =====================================================
# Smart Hybrid Search
# =====================================================

def smart_hybrid_search(query, k=5):

    analysis = analyze_query(query)

    company = analysis["company"]
    sections = analysis["sections"]

    print("\nDetected Query")

    print(analysis)

    # ==========================================
    # Semantic Search
    # ==========================================

    if company:

        semantic_docs = vectorstore.similarity_search(
            query=query,
            k=15,
            filter={
                "company": company
            }
        )

    else:

        semantic_docs = vectorstore.similarity_search(
            query=query,
            k=15
        )

    # ==========================================
    # Prioritize Sections
    # ==========================================

    semantic_docs = prioritize_sections(
        semantic_docs,
        sections
    )

    # ==========================================
    # Fallback
    # ==========================================

    if len(semantic_docs) < k:

        if company:

            extra_docs = vectorstore.similarity_search(
                query=query,
                k=10,
                filter={
                    "company": company
                }
            )

        else:

            extra_docs = vectorstore.similarity_search(
                query=query,
                k=10
            )

        semantic_docs.extend(extra_docs)

    # ==========================================
    # BM25 Search
    # ==========================================

    bm25_docs = bm25_retriever.invoke(query)

    # ==========================================
    # Merge
    # ==========================================

    documents = semantic_docs + bm25_docs

    # ==========================================
    # Remove Duplicates
    # ==========================================

    documents = remove_duplicates(documents)

    return documents[:k]


# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":

    while True:

        query = input("\nAsk Question (exit to quit): ")

        if query.lower() == "exit":
            break

        docs = smart_hybrid_search(query)

        for i, doc in enumerate(docs, 1):

            print("\n" + "=" * 100)

            print(f"Result {i}")

            print("\nMetadata\n")

            print(doc.metadata)

            print("\nContent\n")

            print(doc.page_content[:700])