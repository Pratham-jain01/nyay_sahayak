import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="Nyay Sahayak", page_icon="⚖️", layout="wide")

# CSS
st.markdown("""
<style>
.stButton>button {
    background-color: #FF6B35;
    color: white;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 8px;
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
st.markdown("# ⚖️ Nyay Sahayak")
st.markdown("*Your AI-Powered Legal Assistant for India*")

# Sidebar
with st.sidebar:
    st.header("📚 About")
    st.write("AI assistant for understanding Indian law in simple language.")
    
    st.markdown("---")
    st.subheader("🎯 Quick Questions")
    
    quick_qs = [
        "How to file an FIR?",
        "What are tenant rights in India?",
        "How to file consumer complaint?",
        "What is Section 420 IPC?",
        "Marriage registration process?"
    ]
    
    # API key input
    api_key = st.text_input("Google API Key (optional)", type="password", help="Get free key from ai.google.dev")

# Legal knowledge base
legal_kb = """
INDIAN LEGAL KNOWLEDGE BASE:

1. FIR Filing (Section 154 CrPC):
- Visit nearest police station
- Can be filed orally or in writing
- Police must register your complaint
- You get a free copy of FIR
- Zero FIR can be filed at any station

2. Section 420 IPC (Cheating):
- Deals with cheating and fraud
- Punishment: Up to 7 years imprisonment and fine
- Applies to dishonest property dealings

3. Tenant Rights (Rent Control Acts):
- Right to rent receipt
- Right to request repairs
- Protection from arbitrary eviction
- Notice period: 15-30 days (varies by state)
- Cannot be evicted without court order

4. Consumer Complaints (Consumer Protection Act 2019):
- District Forum: Claims up to ₹50 lakhs
- State Commission: ₹50 lakhs to ₹2 crores
- National Commission: Above ₹2 crores
- Can file online via e-Daakhil portal
- Free for claims under ₹5 lakhs

5. Marriage Registration:
- Hindu Marriage Act: Within 30 days
- Documents: Photos, ID, address proof, invitation
- Register at local registrar office
- Certificate issued within 30 days

6. RTI Act 2005:
- File application with ₹10 fee (₹2 for BPL)
- Response within 30 days mandatory
- Can be filed online or offline

7. Domestic Violence Act 2005:
- File complaint with magistrate
- Protection orders available
- Free legal aid provided
- Monetary relief possible

8. Labour Rights:
- Minimum wages as per state law
- Max 9 hours/day, 48 hours/week
- Mandatory paid leave
- Overtime payment required
- Safe working conditions
"""

# Initialize session
if 'selected_q' not in st.session_state:
    st.session_state.selected_q = ""

# Quick question buttons
with st.sidebar:
    for i, q in enumerate(quick_qs):
        if st.button(f"📌 {q}", key=f"q_{i}"):
            st.session_state.selected_q = q

# Main input
st.markdown("---")
st.subheader("💬 Ask Your Question")

question = st.text_input(
    "Type your legal question:",
    value=st.session_state.selected_q,
    placeholder="Example: What are the steps to register a consumer complaint?"
)

col1, col2 = st.columns([1, 5])
with col1:
    ask = st.button("🔍 Get Answer", type="primary")
with col2:
    if st.button("🔄 Clear"):
        st.session_state.selected_q = ""
        st.rerun()

# Process question
if ask and question:
    with st.spinner("🤔 Searching legal database..."):
        try:
            # Use Google Gemini (free tier)
            if api_key:
                genai.configure(api_key=api_key)
            else:
                # Default demo key (limited usage)
                genai.configure(api_key=st.secrets.get("GOOGLE_API_KEY", ""))
            
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"""You are Nyay Sahayak, a legal assistant for Indian citizens.

Use this legal knowledge to answer the question:

{legal_kb}

Question: {question}

Provide a clear, simple answer in 2-3 paragraphs. Include relevant law sections.
Answer:"""
            
            response = model.generate_content(prompt)
            
            # Display answer
            st.markdown("---")
            st.markdown("### ✨ Answer")
            
            st.markdown(f"""
            <div class="answer-box">
                {response.text}
            </div>
            """, unsafe_allow_html=True)
            
            # Sources
            with st.expander("📚 Sources Referenced"):
                st.write("Indian Penal Code (IPC)")
                st.write("Code of Criminal Procedure (CrPC)")
                st.write("Consumer Protection Act 2019")
                st.write("RTI Act 2005")
                st.write("Various Rent Control Acts")
            
            st.info("⚠️ **Disclaimer:** AI-generated for educational purposes. Consult a lawyer for actual legal matters.")
            
        except Exception as e:
            # Fallback to simple matching if API fails
            st.warning("Using offline knowledge base...")
            
            answer = "I can help with that! "
            
            if "fir" in question.lower():
                answer += "To file an FIR: Visit your nearest police station. You can file it orally or in writing under Section 154 of CrPC. Police must register your complaint and give you a free copy."
            elif "420" in question or "cheating" in question.lower():
                answer += "Section 420 IPC deals with cheating and fraud. It involves dishonestly inducing someone to deliver property. Punishment can be up to 7 years imprisonment and fine."
            elif "tenant" in question.lower() or "rent" in question.lower():
                answer += "Tenant rights include: receiving rent receipts, requesting repairs, protection from arbitrary eviction. Notice period is typically 15-30 days. Landlords cannot evict without court order."
            elif "consumer" in question.lower():
                answer += "Consumer complaints: File in District Forum (up to ₹50L), State Commission (₹50L-₹2Cr), or National Commission (above ₹2Cr). Use e-Daakhil portal for online filing under Consumer Protection Act 2019."
            elif "marriage" in question.lower():
                answer += "Marriage registration under Hindu Marriage Act should be done within 30 days. Need: Photos, ID proof, address proof, marriage invitation. Visit local registrar office."
            else:
                answer += "Please ask about specific topics like FIR filing, consumer complaints, tenant rights, marriage registration, or specific IPC sections. Or select a quick question from the sidebar."
            
            st.markdown(f"""
            <div class="answer-box">
                {answer}
            </div>
            """, unsafe_allow_html=True)
            
            st.info("⚠️ **Note:** For detailed answers, add a Google API key in the sidebar (free at ai.google.dev)")

elif ask:
    st.warning("Please enter a question first!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p><strong>Nyay Sahayak</strong> - Empowering Every Citizen with Accessible Justice</p>
    <p style="font-size: 12px;">NyayTech Innovators | WIT Solapur</p>
</div>
""", unsafe_allow_html=True)
