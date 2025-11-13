import streamlit as st

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
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# ⚖️ Nyay Sahayak")
st.markdown("*Your AI-Powered Legal Assistant for India*")

# Sidebar
with st.sidebar:
    st.header("📚 About Nyay Sahayak")
    st.write("""
    AI assistant to help you understand Indian law in simple language.
    
    **Features:**
    - Ask legal questions in plain language
    - Get instant answers based on Indian laws
    - Understand your rights and procedures
    """)
    
    st.markdown("---")
    st.subheader("🎯 Quick Questions")

# Legal knowledge base with answers
legal_qa = {
    "How to file an FIR?": """
**Filing an FIR (First Information Report):**

1. **Visit the Police Station:** Go to your nearest police station in the jurisdiction where the crime occurred.

2. **Oral or Written Complaint:** You can file an FIR either orally or in writing. If you file it orally, the police will write it down for you.

3. **Under Section 154 CrPC:** Police are legally obligated to register your complaint under Section 154 of the Code of Criminal Procedure.

4. **Get a Copy:** You have the right to receive a free copy of the FIR. Ask for it!

5. **Zero FIR:** If the crime occurred outside the police station's jurisdiction, you can still file a "Zero FIR" which will be transferred to the correct station.

**Important:** Police cannot refuse to register your FIR. If they do, you can file a complaint with the Superintendent of Police or use online complaint systems.

**Legal Reference:** Section 154, Code of Criminal Procedure (CrPC)
""",
    
    "What are tenant rights in India?": """
**Tenant Rights in India:**

1. **Rent Receipt:** You have the right to receive a proper rent receipt every time you pay rent.

2. **Essential Repairs:** Landlords must ensure essential repairs like plumbing, electricity, and structural issues are fixed.

3. **Protection from Arbitrary Eviction:** Under various State Rent Control Acts, you cannot be evicted without proper legal notice and court proceedings.

4. **Notice Period:** Typically 15-30 days notice is required before eviction (varies by state law).

5. **No Forceful Eviction:** Landlords cannot forcefully evict you or change locks without a court order.

6. **Peaceful Possession:** You have the right to peaceful possession of the property during your tenancy.

**Note:** Rent control laws vary by state. Check your state's specific Rent Control Act for detailed provisions.

**Legal Reference:** State Rent Control Acts, Transfer of Property Act
""",
    
    "How to file consumer complaint?": """
**Filing a Consumer Complaint:**

**Choose the Right Forum Based on Claim Value:**
- **District Consumer Forum:** Claims up to ₹50 lakhs
- **State Consumer Commission:** ₹50 lakhs to ₹2 crores
- **National Consumer Commission:** Above ₹2 crores

**Steps to File:**

1. **Online Filing:** Visit the **e-Daakhil portal** (edaakhil.nic.in) for online filing

2. **Documents Required:**
   - Copy of bill/receipt
   - Proof of payment
   - Details of defect/deficiency
   - Correspondence with seller/service provider

3. **Fee Structure:**
   - FREE for claims under ₹5 lakhs
   - Minimal fee for higher claims

4. **Timeline:** Cases should be decided within 90-150 days

5. **Remedies Available:**
   - Refund of amount paid
   - Replacement of goods
   - Compensation for deficiency
   - Removal of defects

**Legal Reference:** Consumer Protection Act, 2019
""",
    
    "What is Section 420 IPC?": """
**Section 420 of Indian Penal Code (IPC):**

**Offense:** Cheating and Dishonestly Inducing Delivery of Property

**Definition:** This section deals with:
- Cheating someone
- Dishonestly inducing them to deliver property
- Making or altering valuable security
- Fraud in transactions

**Common Examples:**
- Financial fraud
- Fake investment schemes
- Credit card fraud
- Property fraud
- Fake document creation

**Punishment:**
- Imprisonment up to **7 years**
- **Fine** (amount determined by court)
- Or both

**Nature of Offense:**
- Cognizable (police can arrest without warrant)
- Non-bailable (bail is at court's discretion)
- Triable by Magistrate

**Note:** This is one of the most commonly invoked sections in fraud cases in India.

**Legal Reference:** Section 420, Indian Penal Code, 1860
""",
    
    "Marriage registration process?": """
**Marriage Registration Process in India:**

**Under Hindu Marriage Act (for Hindus, Buddhists, Jains, Sikhs):**

**Timeline:** Should be done within **30 days** of marriage

**Documents Required:**
1. Application form (from registrar's office)
2. Proof of date of marriage (invitation card, photos)
3. Age proof (birth certificate, school certificate)
4. Address proof (Aadhaar, passport, voter ID)
5. Passport-size photographs
6. Two witnesses with ID proof

**Process:**
1. Visit the **local Sub-Registrar office** in the area where marriage was conducted or where either spouse resides

2. Fill the application form

3. Submit documents with prescribed fee (around ₹100-500, varies by state)

4. Marriage officer verifies documents

5. Publication of notice (30 days waiting period)

6. If no objection, certificate is issued

**For Other Religions:**
- Muslims: No mandatory registration (optional under Muslim law)
- Christians: Register under Christian Marriage Act
- Special Marriage Act: For inter-faith marriages

**Benefits of Registration:**
- Legal proof of marriage
- Required for passport, visa applications
- Property rights protection
- Legal remedy in case of disputes

**Legal Reference:** Hindu Marriage Act, 1955; Special Marriage Act, 1954
"""
}

# Additional QA pairs
additional_qa = {
    "What is RTI Act?": """
**Right to Information (RTI) Act, 2005:**

**Purpose:** Empowers citizens to seek information from government departments and public authorities.

**How to File RTI:**
1. Write an application in simple language
2. Address it to Public Information Officer (PIO)
3. Pay fee of ₹10 (₹2 for BPL cardholders)
4. Can file online or offline

**Timeline:**
- Response within **30 days** (mandatory)
- 48 hours for life and liberty matters

**What You Can Ask:**
- Government decisions and records
- Details of projects and spending
- Information about government schemes
- Complaints and their status

**Exemptions:** National security, cabinet proceedings, personal information

**Legal Reference:** RTI Act, 2005
""",
    
    "Domestic violence protection?": """
**Protection of Women from Domestic Violence Act, 2005:**

**Who Can File:** Any woman subjected to physical, sexual, verbal, emotional, or economic abuse by:
- Husband or male relatives
- Live-in partner
- Any adult male member of household

**How to File:**
1. Approach local **Magistrate Court**
2. Or contact **Protection Officer** appointed in each district
3. Free legal aid available

**Remedies Available:**
- **Protection Order:** Stop violence and harassment
- **Residence Order:** Right to live in shared household
- **Monetary Relief:** Compensation for injuries, loss of earnings
- **Custody Order:** Child custody provisions

**Important:** You do NOT need to file for divorce to get protection under this Act.

**Helplines:**
- Women Helpline: 181
- National Commission for Women: 011-26942369

**Legal Reference:** Protection of Women from Domestic Violence Act, 2005
""",
    
    "Labour rights in India?": """
**Labour Rights in India:**

**Working Hours:**
- Maximum: **9 hours per day**
- Maximum: **48 hours per week**
- Overtime should be paid extra

**Minimum Wages:**
- Set by respective State Governments
- Varies by state and industry
- Must be paid in cash/bank transfer

**Leave Entitlements:**
- Earned Leave: 1 day per 20 days worked
- Casual Leave: As per company policy
- Sick Leave: Medical certificate required

**Safe Working Conditions:**
- Employer must provide safe workplace
- Protective equipment for hazardous work
- First aid facilities

**Social Security:**
- EPF (Employees' Provident Fund)
- ESI (Employee State Insurance)
- Gratuity after 5 years

**Rights:**
- Cannot be discriminated based on gender, religion, caste
- Right to form unions
- Protection against unfair dismissal

**Complaint:** Contact Labour Commissioner office in your district

**Legal Reference:** Code on Wages 2019, Industrial Disputes Act, Factories Act
"""
}

# Combine all QA
all_qa = {**legal_qa, **additional_qa}

# Session state
if 'selected_q' not in st.session_state:
    st.session_state.selected_q = ""

# Quick question buttons in sidebar
with st.sidebar:
    for question in legal_qa.keys():
        if st.button(f"📌 {question.split('?')[0]}?", key=question):
            st.session_state.selected_q = question

# Main section
st.markdown("---")
st.subheader("💬 Ask Your Question")

user_question = st.text_input(
    "Type your legal question:",
    value=st.session_state.selected_q,
    placeholder="Example: How to register a consumer complaint?"
)

col1, col2 = st.columns([1, 5])
with col1:
    ask_btn = st.button("🔍 Get Answer", type="primary")
with col2:
    if st.button("🔄 Clear"):
        st.session_state.selected_q = ""
        st.rerun()

# Process and display answer
if ask_btn and user_question:
    with st.spinner("🤔 Searching legal database..."):
        
        # Find matching answer
        answer_found = False
        
        # Exact match first
        if user_question in all_qa:
            answer = all_qa[user_question]
            answer_found = True
        else:
            # Keyword matching
            question_lower = user_question.lower()
            
            if "fir" in question_lower or "police" in question_lower:
                answer = all_qa["How to file an FIR?"]
                answer_found = True
            elif "tenant" in question_lower or "rent" in question_lower or "evict" in question_lower:
                answer = all_qa["What are tenant rights in India?"]
                answer_found = True
            elif "consumer" in question_lower or "complaint" in question_lower:
                answer = all_qa["How to file consumer complaint?"]
                answer_found = True
            elif "420" in question_lower or "cheating" in question_lower or "fraud" in question_lower:
                answer = all_qa["What is Section 420 IPC?"]
                answer_found = True
            elif "marriage" in question_lower or "registration" in question_lower or "wedding" in question_lower:
                answer = all_qa["Marriage registration process?"]
                answer_found = True
            elif "rti" in question_lower or "information" in question_lower:
                answer = all_qa["What is RTI Act?"]
                answer_found = True
            elif "domestic" in question_lower or "violence" in question_lower or "abuse" in question_lower:
                answer = all_qa["Domestic violence protection?"]
                answer_found = True
            elif "labour" in question_lower or "worker" in question_lower or "employee" in question_lower or "job" in question_lower:
                answer = all_qa["Labour rights in India?"]
                answer_found = True
        
        # Display answer
        st.markdown("---")
        st.markdown("### ✨ Answer")
        
        if answer_found:
            st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
            
            # Sources
            with st.expander("📚 Legal Sources Referenced"):
                st.write("✓ Indian Penal Code (IPC)")
                st.write("✓ Code of Criminal Procedure (CrPC)")
                st.write("✓ Consumer Protection Act 2019")
                st.write("✓ RTI Act 2005")
                st.write("✓ State Rent Control Acts")
                st.write("✓ Hindu Marriage Act 1955")
                st.write("✓ Labour Laws and Code on Wages 2019")
            
        else:
            st.markdown(f"""
            <div class="answer-box">
            <p><strong>I can help you with questions about:</strong></p>
            <ul>
                <li>Filing FIR / Police complaints</li>
                <li>Tenant rights and rent issues</li>
                <li>Consumer complaints</li>
                <li>IPC sections (like 420, 498A, etc.)</li>
                <li>Marriage registration</li>
                <li>RTI applications</li>
                <li>Domestic violence protection</li>
                <li>Labour rights and wages</li>
            </ul>
            <p>Please try one of the quick questions from the sidebar, or rephrase your question to match these topics!</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Disclaimer
        st.info("⚠️ **Legal Disclaimer:** This information is for educational purposes only. For actual legal matters, please consult a qualified lawyer or legal professional.")

elif ask_btn:
    st.warning("⚠️ Please enter a question first!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p style="font-size: 18px; font-weight: bold; margin-bottom: 5px;">⚖️ Nyay Sahayak</p>
    <p style="font-size: 14px; margin-bottom: 10px;">Empowering Every Citizen with Accessible Justice</p>
    <p style="font-size: 12px; color: #999;">
        Developed by <strong>NyayTech Innovators</strong><br>
        Walchand Institute of Technology, Solapur
    </p>
</div>
""", unsafe_allow_html=True)
