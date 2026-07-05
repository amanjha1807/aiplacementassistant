from langchain_chroma import Chroma
from embedder import embedding_model

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model,
    collection_name="placement_assistant"
)

