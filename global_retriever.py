from load_vectorstore import vectorstore


CATEGORY_MAP = {

    "dsa": "dsa",

    "system_design": "system_design",

    "projects": "projects",

    "hr": "hr",

    "oa": "coding_hints"

}


def global_search(intent, query, k=5):

    category = CATEGORY_MAP.get(intent)

    if category is None:
        return []

    docs = vectorstore.similarity_search(
        query=query,
        k=20
    )

    filtered = []

    for doc in docs:

        if (
            doc.metadata.get("document_type") == "global"
            and
            doc.metadata.get("category") == category
        ):

            filtered.append(doc)

    return filtered[:k]