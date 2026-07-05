from langchain_text_splitters import MarkdownHeaderTextSplitter
from document_preprocessor import processed_docs

headers_to_split_on = [
    ("#", "title"),
    ("##", "section"),
    ("###", "topic"),
] 

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False
)




chunks = []

for doc in processed_docs:

    splits = markdown_splitter.split_text(doc.page_content)

    # Preserve original metadata
    for split in splits:
        split.metadata = {
            **doc.metadata,
            **split.metadata
        }

    chunks.extend(splits)
    
if __name__ == "__main__":

  print(f"Total Chunks : {len(chunks)}")

  print()

  print(chunks[0].metadata)

  print()

  print(chunks[0].page_content)