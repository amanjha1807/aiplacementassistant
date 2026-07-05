from rag_chain import ask

while True:

    question = input("\nAsk Question : ")

    if question.lower() == "exit":
        break

    answer, docs = ask(question)

    print("\n")
    print("=" * 100)
    print(answer)

    print("\nSources\n")

    for doc in docs:

        print(
            f"- {doc.metadata.get('title')} | "
            f"{doc.metadata.get('section')}"
        )