from smart_hybrid_retriever import smart_hybrid_search
from prompt import RAG_PROMPT
from llm import llm



def format_docs(docs):

    context = ""

    for doc in docs:

        context += f"""
Company : {doc.metadata.get("company_name","General")}

Title : {doc.metadata.get("title","")}

Section : {doc.metadata.get("section","")}

Content:
{doc.page_content}

-----------------------------------
"""

    return context

def format_sources(docs):

    sources = []

    for doc in docs:

        sources.append(

            f"{doc.metadata.get('company_name','General')} → "
            f"{doc.metadata.get('section','')}"

        )

    return list(dict.fromkeys(sources))







    

def generate_answer(question):

    docs = smart_hybrid_search(question)

    context = format_docs(docs)

    prompt = RAG_PROMPT.invoke({

        "context": context,

        "question": question

    })

    response = llm.invoke(prompt)

    return {

        "answer": response.content,
        "sources": [

        f"{doc.metadata.get('company','Global')} → "
        f"{doc.metadata.get('section','unknown')}"

        for doc in docs

    ]


        

    }


if __name__ == "__main__":

    while True:

        query = input("\nAsk Question : ")

        if query.lower() == "exit":
            break

        result = generate_answer(query)

        print("\n")
        print("="*100)
        print("ANSWER\n")
        print(result["answer"])

        print("\n")
        print("="*100)
        print("SOURCES\n")

        for source in result["sources"]:

            print(source)