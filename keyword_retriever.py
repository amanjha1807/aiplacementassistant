from langchain_community.retrievers import BM25Retriever
from hybrid_chunker import filtered_chunks

# ==========================================
# Split Company and Global Documents
# ==========================================

company_docs = []
global_docs = []

for doc in filtered_chunks:

    if doc.metadata.get("document_type") == "company":
        company_docs.append(doc)

    else:
        global_docs.append(doc)

# ==========================================
# Build BM25 Retrievers
# ==========================================

company_bm25 = BM25Retriever.from_documents(company_docs)
company_bm25.k = 10

global_bm25 = BM25Retriever.from_documents(global_docs)
global_bm25.k = 10


# ==========================================
# Company BM25
# ==========================================

def company_keyword_search(query, company=None):

    docs = company_bm25.invoke(query)

    if company:

        docs = [

            doc

            for doc in docs

            if doc.metadata.get("company") == company

        ]

    return docs


# ==========================================
# Global BM25
# ==========================================

def global_keyword_search(query, category=None):

    docs = global_bm25.invoke(query)

    if category:

        docs = [

            doc

            for doc in docs

            if doc.metadata.get("category") == category

        ]

    return docs