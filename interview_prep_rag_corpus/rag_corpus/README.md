# 🤖 AI Placement Assistant

An AI-powered Placement Preparation Assistant built using **Retrieval-Augmented Generation (RAG)**, **LangChain**, **ChromaDB**, **Hybrid Retrieval (Semantic + BM25)**, and **Streamlit**.

The assistant helps students prepare for technical interviews, online assessments, HR interviews, DSA, system design, and company-specific recruitment processes by retrieving relevant knowledge from a curated knowledge base before generating responses with an LLM.

---

## 🚀 Features

- 📚 RAG-based Question Answering
- 🧠 Conversation Memory
- 🔍 Hybrid Retrieval (Semantic + BM25)
- 🏢 Company-specific Knowledge Retrieval
- 🌍 Global Topic Retrieval
- 📄 YAML Metadata Parsing
- ✂️ Intelligent Markdown Chunking
- 🎯 Query Analysis & Query Rewriting
- 🤖 LLM-powered Answer Generation
- 💬 Streamlit Chat Interface
- 📚 Source Attribution for every response

---

# 🏗️ System Architecture

```
                    User Query
                         │
                         ▼
              Conversation Memory
                         │
                         ▼
                 Query Rewriter
                         │
                         ▼
                 Query Analyzer
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
 Company Semantic Search          Global Semantic Search
        │                                 │
        ▼                                 ▼
 Company BM25 Search             Global BM25 Search
        └──────────────┬──────────────────┘
                       ▼
               Hybrid Retrieval
                       ▼
             Duplicate Removal
                       ▼
                Prompt Template
                       ▼
                      LLM
                       ▼
                 Final Response
```

---

# 📂 Project Structure

```
AI-Placement-Assistant/
│
├── app.py
├── answergenerator.py
├── prompt_template.py
│
├── query_analyzer.py
├── query_rewriter.py
├── conversation_memory.py
│
├── smart_hybrid_retriever.py
├── keyword_retriever.py
├── global_retriever.py
│
├── load_vectorstore.py
├── embedder.py
│
├── directoryloader.py
├── yamlparser.py
├── document_preprocessor.py
├── splitter.py
├── hybrid_chunker.py
├── create_vectorstore.py
│
├── llm.py
│
├── chroma_db/
├── interview_prep_rag_corpus/
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

### Languages

- Python

### Frameworks & Libraries

- LangChain
- ChromaDB
- HuggingFace Embeddings
- Streamlit
- Sentence Transformers
- PyYAML

### Retrieval

- Semantic Search
- BM25 Keyword Search
- Hybrid Retrieval

### LLM

- OpenRouter / Compatible LLM Provider

---

# 📖 Knowledge Base

The assistant retrieves information from a curated markdown corpus containing:

### Company Guides

- Amazon
- Google
- Microsoft
- Adobe
- Meta
- Netflix
- Uber
- Flipkart
- TCS
- Infosys
- Accenture
- Wipro
- Cognizant
- LTIMindtree
- HCLTech
- and more...

### Technical Topics

- Data Structures & Algorithms
- System Design
- HR Interview Questions
- Resume & Projects
- Coding Hints
- Learning Roadmaps

---

# 🔍 Retrieval Pipeline

The application combines multiple retrieval strategies:

### Semantic Search

Uses vector embeddings stored in ChromaDB for semantic similarity.

### BM25 Retrieval

Keyword-based retrieval for exact matches.

### Hybrid Retrieval

Merges semantic and BM25 results to improve recall.

### Conversation Memory

Remembers the current company and intent to support follow-up questions.

Example:

```
User:
Tell me about Amazon OA

↓

User:
What about HR round?

↓

Automatically rewritten as

Amazon HR Round
```

---

# ✨ Example Queries

```
Amazon OA Pattern

Infosys DSA Preparation

Google Interview Process

Accenture HR Questions

Dynamic Programming Roadmap

System Design Basics

Difference between Stack and Heap

Resume Project Ideas
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/AI-Placement-Assistant.git
```

Move into the project

```bash
cd AI-Placement-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Build the Vector Database

```bash
python create_vectorstore.py
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots of:

- Chat Interface
- Retrieval Sources
- Conversation Memory
- Streamlit Dashboard

---

# 🔮 Future Improvements

- Cross-Encoder Reranking
- LLM-based Query Rewriting
- Metadata Ranking
- RAG Evaluation (RAGAS)
- Docker Support
- Authentication
- Admin Dashboard
- Knowledge Base Upload Interface
- Multi-user Session Management

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author:

  Aman Jha



⭐ If you found this project useful, consider giving it a star!
