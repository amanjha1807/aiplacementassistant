from langchain_chroma import Chroma
from embedder import embedding_model
from hybrid_chunker import filtered_chunks
import shutil
import os

# Delete old DB during development
if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")

vectorstore = Chroma.from_documents(
    documents=filtered_chunks,
    embedding=embedding_model,
    persist_directory="chroma_db",
    collection_name="placement_assistant"
)

if __name__ == "__main__":

 print("✅ Vector DB Built Successfully")
 print("Collection:", vectorstore._collection.name)
 print("Chunks:", vectorstore._collection.count())