from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from pathlib import Path

loader = DirectoryLoader(
    "interview_prep_rag_corpus",
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={
        "encoding":"utf-8"
    }
)
docs=loader.load()

docs = [
    doc
    for doc in docs
    if Path(doc.metadata["source"]).name.lower() != "readme.md"
]


if __name__ == "__main__":

    print(len(docs))