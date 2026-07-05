import streamlit as st
import time

from answergenerator import generate_answer

from conversation_memory import ConversationMemory

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

memory = st.session_state.memory
# =====================================================
# Session State Initialization
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "example_query" not in st.session_state:
    st.session_state.example_query = None
# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="AI Placement Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# Custom CSS
# =====================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:2rem;
}

.stChatMessage{
    border-radius:15px;
    padding:10px;
}

.source-box{
    background:#262730;
    padding:12px;
    border-radius:10px;
    margin-bottom:8px;
}

.metric-box{
    background:#1E1E1E;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("🤖 AI Placement Assistant")

    st.markdown("---")

    st.subheader("💡 Suggested Questions")

    st.markdown("""
- Amazon OA Pattern
- Infosys DSA
- Accenture HR Round
- Google Interview Process
- Dynamic Programming
- Tell me about DBMS
- Difference between Stack & Heap
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        memory.clear()

        st.rerun()

    st.markdown("---")

    st.subheader("🧠 Conversation Memory")

    context = memory.get_context()

    st.write("**Company:**", context["company"])

    st.write("**Intent:**", context["intent"])

    st.write("**Topic:**", context["topic"])
    
with st.sidebar.expander("⚙ Retrieval Pipeline"):

    st.markdown("""
1. 🧠 Conversation Memory

2. 🔍 Query Rewriter

3. 📄 Query Analyzer

4. 📚 Hybrid Retriever

5. 🤖 LLM

6. ✅ Final Answer
""")
    
with st.sidebar.expander("🧠 Memory"):

    st.json(context) 
    
    
if len(st.session_state.messages)==0:

    st.info("""
### Welcome 👋

Ask anything about:

- Company Recruitment Process
- DSA Preparation
- HR Questions
- Projects
- System Design
- Resume
- Interview Experience

""") 
    

examples = [

    "Amazon OA Pattern",

    "Infosys DSA",

    "Accenture HR Round",

    "Google Interview Process"

]

for q in examples:

    if st.sidebar.button(q):

        st.session_state.example_query = q
        
        
prompt = st.chat_input(...)

if not prompt and "example_query" in st.session_state:
    prompt = st.session_state.pop("example_query") 
    
    
st.markdown("---")

st.caption(
    "Built using LangChain • ChromaDB • Hybrid Retrieval • Streamlit"
)

# =====================================================
# Title
# =====================================================

st.title("🤖 AI Placement Assistant")

st.caption("Hybrid RAG • Semantic Search • BM25 • Conversation Memory")

# =====================================================
# Session
# =====================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# =====================================================
# Previous Chat
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================================
# Chat Input
# =====================================================

prompt = st.chat_input("Ask anything about placements...")

if prompt:

    st.session_state.messages.append(

        {
            "role":"user",
            "content":prompt
        }

    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        placeholder.markdown("⏳ Thinking...")

        start = time.time()

        result = generate_answer(prompt)

        end = time.time()

        answer = result["answer"]

        sources = result["sources"]

        response_time = round(end-start,2)

        placeholder = st.empty()

        streamed_text = ""

        for word in answer.split():

           streamed_text += word + " "

           placeholder.markdown(streamed_text + "▌")

           time.sleep(0.015)
   
        placeholder.markdown(streamed_text)

    with st.expander("📚 Sources Used"):

        for source in sources:

          st.markdown(
            f"""
   <div style="
   padding:10px;
   margin-bottom:8px;
   border-radius:10px;
   background-color:#1f2937;
   border-left:5px solid #4CAF50;
   ">
   📄 <b>{source}</b>
   </div>
    """,
    unsafe_allow_html=True
)