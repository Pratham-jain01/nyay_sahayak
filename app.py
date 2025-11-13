import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document

# Page config
st.set_page_config(page_title="Nyay Sahayak", page_icon="⚖️", layout="wide")

# CSS
st.markdown("""<style>
.stButton>button {background-color: #FF6B35; color: white; font-weight: bold;}
</style>""", unsafe_allow_html=True)

# Header
st.title("⚖️ Nyay Sahayak - Your Legal Assistant")
st.markdown("*AI-Powered Legal Guidance for Indian Citizens*")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("Ask legal questions in simple language and get instant answers based on Indian law.")
    st.markdown("---")
    st.subheader("Quick Questions")
    quick_qs = [
        "How to file FIR?",
        "Tenant rights?",
        "Consumer complaint?",
        "Section 420 IPC?",
        "Marriage registration?"
    ]

# Initialize
@st.cache_resource
def load_qa():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    docs = [
        Document(page_content="Section 420 IPC: Cheating and fraud. Punishment up to 7 years.", metadata={"source": "IPC"}),
        Document(page_content="FIR filing: Visit police station. Register under Section 154 CrPC. Can be oral or written.", metadata={"source": "CrPC"}),
        Document(page_content="Tenant rights: Rent receipt, repairs, protection from eviction under Rent Control Act.", metadata={"source": "Rent Act"}),
        Document(page_content="Consumer complaint: District Forum (up to 50L), State (2Cr), National (above). Consumer Protection Act 2019.", metadata={"source": "Consumer Act"}),
        Document(page_content="Marriage registration: Required within 30 days under Hindu Marriage Act. Need photos, ID, address proof.", metadata={"source": "Marriage Law"}),
        Document(page_content="RTI Act 2005: File application with Rs 10. Response in 30 days mandatory.", metadata={"source": "RTI"}),
        Document(page_content="Domestic Violence Act 2005: File complaint with magistrate. Protection orders available.", metadata={"source": "DV Act"}),
        Document(page_content="Labour laws: Minimum wage, 9 hour workday, paid leave, safe conditions.", metadata={"source": "Labour Laws"}),
    ]
    
    vectorstore = FAISS.from_documents(docs, embeddings)
    
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0.3, "max_length": 512}
    )
    
    prompt = PromptTemplate(
        template="You are a legal assistant. Answer in simple language.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:",
        input_variables=["context", "question"]
    )
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

# Load
if 'qa' not in st.session_state:
    with st.spinner("Loading..."):
        st.session_state.qa = load_qa()
        st.success("Ready!")

# Sidebar buttons
with st.sidebar:
    for i, q in enumerate(quick_qs):
        if st.button(f"📌 {q}", key=f"q_{i}"):
            st.session_state.question = q

# Main
st.markdown("---")
question = st.text_input("Your Question:", value=st.session_state.get('question', ''), placeholder="Ask about Indian law...")

if st.button("Get Answer", type="primary"):
    if question:
        with st.spinner("Searching..."):
            result = st.session_state.qa({"query": question})
            st.markdown("### Answer:")
            st.info(result['result'])
            
            with st.expander("Sources"):
                for doc in result['source_documents']:
                    st.write(f"**{doc.metadata['source']}:** {doc.page_content}")
            
            st.warning("⚠️ For legal matters, consult a qualified lawyer.")
    else:
        st.error("Please enter a question.")

# Footer
st.markdown("---")
st.markdown("<center><small>Nyay Sahayak | NyayTech Innovators | WIT Solapur</small></center>", unsafe_allow_html=True)
