import streamlit as st

st.set_page_config(page_title="PlaceRAG", page_icon="🎓")
st.title("🎓 PlaceRAG - Amity Placement Assistant")
st.subheader("Ask anything about placements!")

knowledge_base = {
    "interview": "Common Amity placement interview questions:\n1. Tell me about yourself\n2. Explain OOP concepts\n3. What is your biggest project?\n4. Why should we hire you?\n5. Where do you see yourself in 5 years?",
    "companies": "Companies visiting Amity University MP:\n- TCS, Infosys, Wipro (3.5-4.5 LPA)\n- Cognizant, HCL, Tech Mahindra\n- Amazon, Accenture\nMinimum CGPA: 6.0-7.0",
    "resume": "Resume Tips:\n- Keep it 1 page\n- Add GitHub link\n- Mention CGPA if above 7.0\n- Include projects and internships\n- Use action verbs",
    "aptitude": "Aptitude Preparation:\n- Quantitative: Percentages, Profit/Loss\n- Logical Reasoning: Patterns\n- Verbal: Grammar\n- Practice on: IndiaBix, PrepInsta",
    "internship": "Finding Internships:\n- Internshala, LinkedIn\n- Apply in 2nd/3rd semester\n- Amity Career Portal\n- Cold email professors",
    "salary": "Salary Info:\n- TCS/Infosys: 3.5-4.5 LPA\n- Amazon: 6-12 LPA\n- Research on Glassdoor\n- Negotiate total package",
    "hr": "HR Questions:\n- Are you willing to relocate?\n- What do you know about us?\n- Why should we hire you?\n- Your greatest weakness?",
    "offcampus": "Off-Campus Tips:\n- LinkedIn profile must\n- Naukri.com, Shine.com\n- Hackathons: Unstop, HackerEarth\n- GitHub portfolio important"
}

def get_answer(query):
    query = query.lower()
    keywords = {
        "interview": ["interview", "question", "ask"],
        "companies": ["company", "companies", "visit", "amity", "tcs", "infosys"],
        "resume": ["resume", "cv", "format"],
        "aptitude": ["aptitude", "test", "math", "logical"],
        "internship": ["internship", "intern"],
        "salary": ["salary", "package", "ctc", "lpa"],
        "hr": ["hr", "human"],
        "offcampus": ["off campus", "offcampus", "linkedin", "online"]
    }
    for topic, keys in keywords.items():
        if any(k in query for k in keys):
            return knowledge_base[topic]
    return "I can help with: interviews, companies, resume, aptitude, internships, salary, HR questions, off-campus placements. Please ask about any of these!"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask about placements..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    response = get_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

st.sidebar.title("📚 Ask me about:")
st.sidebar.write("🏢 Companies\n💼 Interviews\n📝 Resume\n🧮 Aptitude\n🔍 Internships\n💰 Salary\n👔 HR Questions\n🌐 Off-Campus")
