from splitter import chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

recursive_splitter = RecursiveCharacterTextSplitter(

    chunk_size=900,

    chunk_overlap=150,

    separators=[

        "\n### ",

        "\n## ",

        "\n\n",

        "\n",

        ". ",

        " ",

        ""

    ]
)

final_chunks = recursive_splitter.split_documents(chunks)

if __name__ == "__main__":

 print(f"Original Chunks : {len(chunks)}")
 print(f"Final Chunks    : {len(final_chunks)}")

 print("-" * 80)

 print(final_chunks[0].metadata)

 print("-" * 80)

 print("="*100)

 print(final_chunks[2].page_content)

 print("="*100)

 print(final_chunks[2].metadata)



if __name__ == "__main__":
 sizes = [len(doc.page_content) for doc in final_chunks]

 print()

 print("Minimum :", min(sizes))
 print("Maximum :", max(sizes))
 print("Average :", sum(sizes)/len(sizes))


filtered_chunks = []

MIN_CHUNK_SIZE = 120

for chunk in final_chunks:
    if len(chunk.page_content.strip()) >= MIN_CHUNK_SIZE:
        filtered_chunks.append(chunk)
        
for i, chunk in enumerate(filtered_chunks):

    chunk.metadata["chunk_id"] = i
    chunk.metadata["chunk_size"] = len(chunk.page_content)
    
if __name__ == "__main__":
   
 print(filtered_chunks[0].metadata)

 from pathlib import Path

 for chunk in filtered_chunks:

    chunk.metadata["filename"] = Path(
        chunk.metadata["source"]
    ).stem