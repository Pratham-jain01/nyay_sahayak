import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document

# Page config
st.set_page_config(page_title="Nyay Sahayak", page_icon="⚖️", layout="wide")

# CSS
st.markdown("""
<style>
.stButton>button {
    background-color: #FF6B35;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}
.answer-box {
    background-color: #E8F4F8;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #FF6B35;
}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 10])
with col1:
    st.markdown("# ⚖️")
with col2:
    st.title("Nyay Sahayak")
    st.markdown("*Your AI-Powered Legal Assistant for India*")

# Sidebar
with st.sidebar:
    st.header("📚 About Nyay Sahayak")
    st.write("""
    This AI assistant helps you understand Indian law in simple language.
    
    **Features:**
    - Ask legal questions in plain language
    - Get instant answers based on Indian laws
    - Understand your rights and legal procedures
    """)
    
    st.markdown("---")
    st.subheader("🎯 Quick Questions")
    
    quick_questions = [
        "How to file FIR?",
        "What are tenant rights?",
        "Consumer complaint process?",
        "Section 420 IPC?",
        "Marriage registration?"
    ]

# Initialize session state
if 'selected_question' not in st.session_state:
    st.session_state.selected_question = ""

# Load QA system
@st.cache_resource
def load_qa_system():
    try:
        # Initialize embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Legal knowledge base
        legal_docs = [
            Document(
                page_content="Section 420 of the Indian Penal Code deals with cheating and dishonestly inducing delivery of property. The punishment for this offense can be imprisonment up to 7 years and a fine. This section is commonly invoked in fraud cases.",
                metadata={"source": "Indian Penal Code", "section": "420"}
            ),
            Document(
                page_content="To file an FIR (First Information Report), visit the nearest police station. You can file it orally or in writing. The police are legally obligated to register your complaint under Section 154 of the Code of Criminal Procedure (CrPC). You have the right to receive a copy of the FIR.",
                metadata={"source": "Code of Criminal Procedure", "section": "154"}
            ),
            Document(
                page_content="Tenant rights in India include: right to receive rent receipts, right to request essential repairs, protection from arbitrary eviction under various Rent Control Acts. Notice periods vary by state law, typically 15-30 days. Landlords cannot forcefully evict without court orders.",
                metadata={"source": "Rent Control Acts", "section": "General"}
            ),
            Document(
                page_content="Consumer complaints can be filed in: District Consumer Forum (claims up to ₹50 lakhs), State Consumer Commission (₹50 lakhs to ₹2 crores), and National Consumer Commission (above ₹2 crores). The Consumer Protection Act 2019 provides these remedies. Complaints can be filed online through the e-Daakhil portal.",
                metadata={"source": "Consumer Protection Act", "section": "2019"}
            ),
            Document(
                page_content="Marriage registration in India varies by religion. Under the Hindu Marriage Act, registration is required within 30 days of marriage. Required documents include: passport-size photos, age proof, address proof, marriage invitation card, and witnesses. Registration can be done at the local registrar's office.",
                metadata={"source": "Hindu Marriage Act", "section": "Registration"}
            ),
            Document(
                page_content="The Right to Information (RTI) Act 2005 allows Indian citizens to request information from public authorities. File an RTI application with a ₹10 fee (₹2 for BPL). Public authorities must respond within 30 days. RTI can be filed online or offline to the concerned Public Information Officer (PIO).",
                metadata={"source": "RTI Act", "section": "2005"}
            ),
            Document(
                page_content="Domestic violence victims can file complaints under the Protection of Women from Domestic Violence Act 2005. Magistrates can issue protection orders, residence orders, monetary relief, and custody orders. Complaints can be filed by the victim or on her behalf. Free legal aid is available.",
                metadata={"source": "DV Act", "section": "2005"}
            ),
            Document(
                page_content="Labour laws in India protect workers' rights including: minimum wages as per state government notifications, maximum working hours (9 hours per day, 48 hours per week), mandatory paid leave, overtime payment, and safe working conditions. The Code on Wages 2019 consolidates these provisions.",
                metadata={"source": "Labour Laws", "section": "Code on Wages 2019"}
            ),
        ]
        
        # Create vector store
        vectorstore = FAISS.from_documents(legal_docs, embeddings)
        
        # Initialize LLM
        llm = HuggingFaceHub(
            repo_id="google/flan-t5-large",
            model_kwargs={"temperature": 0.3, "max_length": 512}
        )
        
        # Create prompt
        prompt_template = """You are Nyay Sahayak, a helpful legal assistant for Indian citizens.
Use the following legal information to answer the question clearly and simply.

Legal Context: {context}

Question: {question}

Provide a practical, easy-to-understand answer. Include relevant law sections where applicable.

Answer:"""

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )
        
        return qa_chain, vectorstore
        
    except Exception as e:
        st.error(f"Error loading system: {str(e)}")
        return None, None

# Load system
if 'qa_chain' not in st.session_state:
    with st.spinner("🔄 Loading Nyay Sahayak AI..."):
        qa_chain, vectorstore = load_qa_system()
        if qa_chain:
            st.session_state.qa_chain = qa_chain
            st.session_state.vectorstore = vectorstore
            st.success("✅ System ready!")
        else:
            st.error("Failed to load system. Please refresh.")
            st.stop()

# Quick question buttons in sidebar
with st.sidebar:
    for idx, question in enumerate(quick_questions):
        if st.button(f"📌 {question}", key=f"quick_{idx}"):
            st.session_state.selected_question = question

# Main interface
st.markdown("---")
st.subheader("💬 Ask Your Legal Question")

user_question = st.text_input(
    "Type your question:",
    value=st.session_state.selected_question,
    placeholder="Example: What are the steps to file a police complaint?",
    key="main_input"
)

col1, col2 = st.columns([1, 5])
with col1:
    ask_button = st.button("🔍 Get Answer", type="primary")
with col2:
    if st.button("🔄 Clear"):
        st.session_state.selected_question = ""
        st.rerun()

# Process question
if ask_button and user_question:
    with st.spinner("🤔 Searching legal database..."):
        try:
            result = st.session_state.qa_chain({"query": user_question})
            
            # Display answer
            st.markdown("---")
            st.markdown("### ✨ Answer")
            
            st.markdown(f"""
            <div class="answer-box">
                <p style="font-size: 16px; line-height: 1.8; color: #333;">
                    {result['result']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display sources
            if result.get('source_documents'):
                with st.expander("📚 Legal Sources"):
                    for i, doc in enumerate(result['source_documents'], 1):
                        st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'Legal Database')}")
                        if 'section' in doc.metadata:
                            st.markdown(f"*Section:* {doc.metadata['section']}")
                        st.markdown(f"> {doc.page_content[:200]}...")
                        st.markdown("---")
            
            # Disclaimer
            st.info("⚠️ **Legal Disclaimer:** This is AI-generated information for educational purposes only. For actual legal matters, please consult a qualified lawyer or legal professional.")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please try rephrasing your question or select a quick question from the sidebar.")

elif ask_button:
    st.warning("⚠️ Please enter a question first.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p style="font-size: 18px; font-weight: bold;">Nyay Sahayak</p>
    <p style="font-size: 14px;">Empowering Every Citizen with Accessible Justice</p>
    <p style="font-size: 12px; color: #999;">
        Developed by NyayTech Innovators | Walchand Institute of Technology, Solapur
    </p>
</div>
""", unsafe_allow_html=True)
