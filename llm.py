# llm.py
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
load_dotenv()

llm = ChatOpenRouter(
    model="openrouter/free",
    temperature=0.5
)

#response = llm.invoke("Tell me about Cristiano Ronaldo in 5 lines")
#print(response.content)

