from prompt import RAG_PROMPT
from llm import llm

from smart_hybrid_retriever import smart_hybrid_search

if __name__ == "__main__":
 def format_docs(docs):

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

if __name__ == "__main__":
 def ask(question):

    docs = smart_hybrid_search(question)

    context = format_docs(docs)

    prompt = RAG_PROMPT.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(prompt)

    return response.content, docs