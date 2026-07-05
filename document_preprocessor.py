from directoryloader import docs
from yamlparser import extract_metadata
from langchain_core.documents import Document

processed_docs = []

for doc in docs:

    # ----------------------------------------
    # Extract YAML metadata and clean content
    # ----------------------------------------
    metadata, content = extract_metadata(doc.page_content)

    # ----------------------------------------
    # Company Information
    # ----------------------------------------
    company_name = metadata.get("company", "").strip()

    # ----------------------------------------
    # Document Type
    # ----------------------------------------
    if company_name:
        document_type = "company"
    else:
        document_type = "global"

    # ----------------------------------------
    # Merge Metadata
    # ----------------------------------------
    final_metadata = {
        **doc.metadata,
        **metadata,
        "company_name": company_name,
        "document_type": document_type,
    }

    # ----------------------------------------
    # Create LangChain Document
    # ----------------------------------------
    processed_docs.append(
        Document(
            page_content=content,
            metadata=final_metadata
        )
    )

# =====================================================
# Testing
# =====================================================
if __name__ == "__main__":

    print(f"\nProcessed {len(processed_docs)} documents.\n")

    print("=" * 100)
    print("First Document Metadata")
    print("=" * 100)
    print(processed_docs[0].metadata)

    print("\n" + "=" * 100)
    print("First Document Content")
    print("=" * 100)
    print(processed_docs[0].page_content[:500])

    print("\n" + "=" * 100)
    print("Company Documents")
    print("=" * 100)

    for doc in processed_docs:
        if doc.metadata["document_type"] == "company":
            print(doc.metadata["company_name"])