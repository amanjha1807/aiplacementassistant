from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "device": "cpu"
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)


if __name__ == "__main__":

    print("✅ Embedding model loaded successfully!")

    query = "Amazon Interview Process"

    embedding = embedding_model.embed_query(query)

    print(type(embedding))
    print()

    print("Dimensions:", len(embedding))
    print()

    print(embedding[:10])

    from hybrid_chunker import filtered_chunks

    sample_chunk = filtered_chunks[0]

    vector = embedding_model.embed_documents(
        [sample_chunk.page_content]
    )

    print()

    print("Number of vectors:", len(vector))
    print("Dimensions:", len(vector[0]))