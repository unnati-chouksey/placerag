import streamlit as st

st.set_page_config(page_title="PlaceRAG - Amity", page_icon="🎓", layout="wide")

st.title("🎓 PlaceRAG - Amity Placement Assistant")
st.caption("AI-powered RAG system for Amity University MP students")

tab1, tab2, tab3, tab4 = st.tabs(["💬 Ask PlaceRAG", "🏢 Company Filter", "🛣️ Skill Roadmap", "📝 Internship Guide"])

companies = {
    "TCS": {"cgpa": 6.0, "package": "3.5-4.5 LPA", "skills": ["Python", "Java", "SQL", "Communication"], "rounds": "Aptitude → Technical → HR", "type": "Mass Recruiter"},
    "Infosys": {"cgpa": 6.5, "package": "3.5-5 LPA", "skills": ["Java", "Python", "DBMS", "OS"], "rounds": "Online Test → HR", "type": "Mass Recruiter"},
    "Wipro": {"cgpa": 6.0, "package": "3.5-4 LPA", "skills": ["C++", "Java", "Networking"], "rounds": "Aptitude → Technical → HR", "type": "Mass Recruiter"},
    "Cognizant": {"cgpa": 6.0, "package": "4-5 LPA", "skills": ["Python", "SQL", "Agile"], "rounds": "Aptitude → Coding → HR", "type": "Mass Recruiter"},
    "HCL": {"cgpa": 6.0, "package": "3.5-4.5 LPA", "skills": ["Java", "C", "Linux"], "rounds": "Aptitude → Technical", "type": "Mass Recruiter"},
    "Tech Mahindra": {"cgpa": 6.0, "package": "3-4.5 LPA", "skills": ["Networking", "Python", "SQL"], "rounds": "Aptitude → HR", "type": "Mass Recruiter"},
    "Accenture": {"cgpa": 7.0, "package": "4.5-8 LPA", "skills": ["Python", "AI/ML", "Cloud", "SQL"], "rounds": "Cognitive Test → Coding → HR", "type": "Mid Tier"},
    "Amazon": {"cgpa": 7.5, "package": "6-15 LPA", "skills": ["DSA", "System Design", "Python/Java", "Leadership"], "rounds": "OA → 4-5 Tech Rounds", "type": "Top Tier"},
}

knowledge_base = {
    "interview": "🎯 Common Amity Placement Interview Questions:\n1. Tell me about yourself\n2. Explain OOP concepts with example\n3. What is your best project?\n4. Difference between Array and LinkedList\n5. What is DBMS normalization?\n6. Why should we hire you?\n7. Where do you see yourself in 5 years?",
    "resume": "📝 Resume Tips for Freshers:\n• Keep it 1 page only\n• Add GitHub profile link\n• Mention CGPA if above 7.0\n• List top 3-4 projects with tech stack\n• Include internships\n• Use action verbs: Built, Designed, Implemented\n• Add certifications (Coursera, NPTEL)",
    "aptitude": "🧮 Aptitude Preparation:\n• Quantitative: Percentages, Profit/Loss, Time & Work, Pipes\n• Logical: Patterns, Blood Relations, Syllogisms\n• Verbal: Reading Comprehension, Fill in blanks\n• Practice: IndiaBix, PrepInsta, GeeksforGeeks\n• Give mock tests daily!",
    "salary": "💰 Salary Negotiation Tips:\n• Research on Glassdoor, AmbitionBox\n• TCS/Infosys/Wipro: 3.5-4.5 LPA\n• Accenture: 4.5-8 LPA\n• Amazon: 6-15 LPA\n• Don't reveal expected salary first\n• Consider total package (base + bonus + benefits)",
    "hr": "👔 HR Round Tips:\n• Research company thoroughly\n• Prepare STAR format answers\n• Why this company? — Be specific!\n• Weakness: Real one + how you're improving\n• Relocation: Always say yes\n• Salary: Say 'as per company standards'",
    "offcampus": "🌐 Off-Campus Strategy:\n• LinkedIn: Connect with 5 recruiters daily\n• Naukri.com + Shine.com profiles updated\n• Unstop, HackerEarth hackathons\n• GitHub portfolio with 3+ projects\n• Cold email HR with resume\n• Referrals: Best way to get interviews!",
    "cgpa": "📊 CGPA Importance:\n• Below 6.0: Very limited companies\n• 6.0-6.5: TCS, Wipro, HCL, Tech Mahindra\n• 6.5-7.0: Infosys, Cognizant\n• 7.0+: Accenture, Capgemini\n• 7.5+: Amazon, top product companies\n• Improve via internal exams + projects",
}

def get_answer(query):
    query = query.lower()
    keywords = {
        "interview": ["interview", "question", "puchha", "asked", "round"],
        "resume": ["resume", "cv", "format", "banaye"],
        "aptitude": ["aptitude", "test", "math", "logical", "quant"],
        "salary": ["salary", "package", "ctc", "lpa", "negotiate"],
        "hr": ["hr", "human resource", "soft skill"],
        "offcampus": ["off campus", "offcampus", "linkedin", "online", "naukri"],
        "cgpa": ["cgpa", "marks", "percentage", "score", "eligible"],
    }
    for topic, keys in keywords.items():
        if any(k in query for k in keys):
            return knowledge_base[topic]
    company_found = None
    for comp in companies:
        if comp.lower() in query:
            company_found = comp
            break
    if company_found:
        c = companies[company_found]
        return f"🏢 {company_found}\n📦 Package: {c['package']}\n📊 Min CGPA: {c['cgpa']}\n🛠️ Skills: {', '.join(c['skills'])}\n🔄 Rounds: {c['rounds']}\n🏷️ Type: {c['type']}"
    return "I can help with: interviews, resume, aptitude, salary, HR, off-campus, CGPA, or ask about any company like TCS, Amazon, Infosys!"

with tab1:
    st.subheader("💬 Ask anything about placements!")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    if prompt := st.chat_input("Ask about companies, resume, salary, interview..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        response = get_answer(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

with tab2:
    st.subheader("🏢 Company Filter — Enter your CGPA")
    cgpa = st.slider("Your CGPA", 0.0, 10.0, 7.0, 0.1)
    st.write(f"### Companies eligible for CGPA {cgpa}:")
    eligible = [(name, info) for name, info in companies.items() if cgpa >= info["cgpa"]]
    if eligible:
        for name, info in eligible:
            with st.expander(f"✅ {name} — {info['package']}"):
                st.write(f"**Min CGPA:** {info['cgpa']}")
                st.write(f"**Skills needed:** {', '.join(info['skills'])}")
                st.write(f"**Interview rounds:** {info['rounds']}")
                st.write(f"**Type:** {info['type']}")
    else:
        st.error("No companies match. Focus on improving CGPA!")

with tab3:
    st.subheader("🛣️ Skill Roadmap — Based on your target company")
    target = st.selectbox("Select target company", list(companies.keys()))
    role = st.selectbox("Select role", ["Software Engineer", "Data Analyst", "AI/ML Engineer", "Full Stack Developer"])
    if target:
        info = companies[target]
        st.success(f"### Roadmap for {target} — {role}")
        st.write(f"**Required Skills:** {', '.join(info['skills'])}")
        st.write("**Month 1-2:** DSA basics — Arrays, Strings, LinkedList (LeetCode Easy)")
        st.write("**Month 3-4:** Core subjects — DBMS, OS, CN, OOP")
        st.write("**Month 5:** Projects — Build 2 good GitHub projects")
        st.write("**Month 6:** Mock interviews + aptitude practice daily")
        st.write("**Online Resources:** Coursera, NPTEL, GeeksforGeeks, YouTube")
        st.write("**Offline:** Amity placement cell workshops, coding clubs")

with tab4:
    st.subheader("📝 Internship Guide")
    semester = st.radio("Your current semester", ["1st-2nd", "3rd-4th", "5th-6th", "7th-8th"])
    mode = st.radio("Mode", ["Online", "Offline/On-campus"])
    if semester == "1st-2nd":
        st.info("**Focus on:** Learn C/C++/Python basics, build profile on LinkedIn, join college coding clubs")
    elif semester == "3rd-4th":
        st.success("**Apply on:** Internshala, LinkedIn, LetsIntern\n\n**Skills to show:** 1 project + basics of DSA\n\n**Target:** 1-2 month stipend internship (5k-15k/month)")
    elif semester == "5th-6th":
        st.success("**Apply on:** Unstop, AngelList, company career pages\n\n**Target:** 2-6 month internship (15k-40k/month)\n\n**PPO chance:** High if performance is good!")
    else:
        st.warning("**Final year:** Focus on full-time placement + keep internship experience ready for resume")
    if mode == "Online":
        st.write("🌐 **Online platforms:** Internshala, LinkedIn, Unstop, Wellfound, TopHire")
    else:
        st.write("🏫 **Offline/Campus:** Amity placement cell, college job fair, professor referrals, industry visits")

st.sidebar.title("📚 PlaceRAG Topics")
st.sidebar.write("💬 Chat with AI\n🏢 Company Filter\n🛣️ Skill Roadmap\n📝 Internship Guide")
st.sidebar.success("Built for Amity University MP students!")
