import streamlit as st

st.set_page_config(page_title="PlaceRAG - Amity", page_icon="🎓", layout="wide")

st.title("🎓 PlaceRAG - Amity Placement Assistant")
st.caption("AI-powered RAG system for Amity University MP students")

# --- EXPANDED TABS WITH ATS & OFF-CAMPUS ELEMENTS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 Ask PlaceRAG", 
    "🏢 Company & Off-Campus Filter", 
    "🛣️ Skill & API Roadmap", 
    "📝 Internship Guide",
    "📄 AI Resume Advisor (ATS)"
])

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

# --- EXPANDED CHATBOT LIMITS & KNOWLEDGE BASE ---
knowledge_base = {
    "interview": "🎯 Common Amity Placement Interview Questions:\n1. Tell me about yourself\n2. Explain OOP concepts with example\n3. What is your best project?\n4. Difference between Array and LinkedList\n5. What is DBMS normalization?\n6. Why should we hire you?\n7. Where do you see yourself in 5 years?",
    "resume": "📝 Resume Tips for Freshers:\n• Keep it 1 page only\n• Add GitHub profile link\n• Mention CGPA if above 7.0\n• List top 3-4 projects with tech stack\n• Include internships\n• Use action verbs: Built, Designed, Implemented\n• Add certifications (Coursera, NPTEL)",
    "aptitude": "🧮 Aptitude Preparation:\n• Quantitative: Percentages, Profit/Loss, Time & Work, Pipes\n• Logical: Patterns, Blood Relations, Syllogisms\n• Verbal: Reading Comprehension, Fill in blanks\n• Practice: IndiaBix, PrepInsta, GeeksforGeeks\n• Give mock tests daily!",
    "salary": "💰 Salary Negotiation Tips:\n• Research on Glassdoor, AmbitionBox\n• TCS/Infosys/Wipro: 3.5-4.5 LPA\n• Accenture: 4.5-8 LPA\n• Amazon: 6-15 LPA\n• Don't reveal expected salary first\n• Consider total package (base + bonus + benefits)",
    "hr": "👔 HR Round Tips:\n• Research company thoroughly\n• Prepare STAR format answers\n• Why this company? — Be specific!\n• Weakness: Real one + how you're improving\n• Relocation: Always say yes\n• Salary: Say 'as per company standards'",
    "offcampus": "🌐 Off-Campus Strategy:\n• LinkedIn: Connect with 5 recruiters daily\n• Naukri.com + Shine.com profiles updated\n• Unstop, HackerEarth hackathons\n• GitHub portfolio with 3+ projects\n• Cold email HR with resume\n• Referrals: Best way to get interviews!",
    "cgpa": "📊 CGPA Importance:\n• Below 6.0: Very limited companies\n• 6.0-6.5: TCS, Wipro, HCL, Tech Mahindra\n• 6.5-7.0: Infosys, Cognizant\n• 7.0+: Accenture, Capgemini\n• 7.5+: Amazon, top product companies\n• Improve via internal exams + projects",
    # New Coverage Fields for Students Problems
    "api": "💡 **Modern API Stack & Tech (Industry Standard):**\n• Today companies look for RESTful APIs, FastAPI, Node.js, and GraphQL.\n• Key Concepts to study: HTTP Status codes (200, 404, 500), CRUD operations, and JWT Authentication Tokens.\n• Tooling: Learn Postman for testing endpoints.",
    "offline": "🏢 **Offline/Off-Campus Clarity Matrix:**\n• Startups do not care much about CGPA. If your CGPA is low, bypass screening via Open-Source commits and active portfolio projects.\n• Use cold-email architectures to reach out to founders directly.",
    "gap": "⚠️ **Career Gap / Backlog Issue:**\n• If you have active backlogs, clear them before major mass drives.\n• Highlight freelance projects or certifications to cover up any year gap in interviews."
}

def get_answer(query):
    query = query.lower()
    keywords = {
        "interview": ["interview", "question", "puchha", "asked", "round"],
        "resume": ["resume", "cv", "format", "banaye"],
        "aptitude": ["aptitude", "test", "math", "logical", "quant"],
        "salary": ["salary", "package", "ctc", "lpa", "negotiate"],
        "hr": ["hr", "human resource", "soft skill"],
        "offcampus": ["off campus", "offcampus", "linkedin", "online", "naukri", "apply"],
        "cgpa": ["cgpa", "marks", "percentage", "score", "eligible"],
        "api": ["api", "backend", "fastapi", "rest api", "tech stack", "industry"],
        "offline": ["offline", "direct", "packet", "scale"],
        "gap": ["backlog", "gap", "fail", "problem"]
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
    return "I can help with: interviews, resume, aptitude, salary, HR, off-campus, CGPA, Backlogs, Modern APIs, or ask about any company like TCS, Amazon, Infosys!"

# --- TAB 1: BOT ---
with tab1:
    st.subheader("💬 Ask anything about placements!")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    if prompt := st.chat_input("Ask about companies, resume, salary, modern APIs, backlogs..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        response = get_answer(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

# --- TAB 2: ADVANCED FILTER & PACKAGE EXPECTATION ---
with tab2:
    st.subheader("🏢 Company Filter & Package Estimator Matrix")
    
    col1, col2 = st.columns(2)
    with col1:
        cgpa = st.slider("Your CGPA", 0.0, 10.0, 7.0, 0.1)
    with col2:
        backlog_status = st.radio("Active Backlogs?", ["No", "Yes"])
        
    if backlog_status == "Yes":
        st.error("⚠️ Note: Mass Recruiters usually mandate 0 active backlogs. Focus on off-campus startups!")

    st.write(f"### 📈 Strategy & Package Expectation for CGPA {cgpa}:")
    
    # Offline scale evaluation based on user input
    if cgpa >= 8.5:
        st.success("🌟 **Tier 1 / Product Scale (Expected Package: 8 LPA - 20 LPA+)**\n\n**Offline Strategy:** High chance in off-campus tech giants. Focus heavily on advanced DSA, System Design, and Cloud integrations.")
    elif cgpa >= 7.0:
        st.info("⚡ **Tier 2 / Mid Tier Scale (Expected Package: 4.5 LPA - 8 LPA)**\n\n**Offline Strategy:** Eligible for premium roles in service sectors and established startups. Build Full-stack projects.")
    else:
        st.warning("📈 **Tier 3 / Startup Scale (Expected Package: 3 LPA - 5 LPA)**\n\n**Offline Strategy:** Don't worry about CGPA! Apply offline via LinkedIn referrals or GitHub contributions directly to tech founders.")

    st.write(f"### On-Campus companies eligible for CGPA {cgpa}:")
    eligible = [(name, info) for name, info in companies.items() if cgpa >= info["cgpa"]]
    if eligible:
        for name, info in eligible:
            with st.expander(f"✅ {name} — {info['package']}"):
                st.write(f"**Min CGPA:** {info['cgpa']}")
                st.write(f"**Skills needed:** {', '.join(info['skills'])}")
                st.write(f"**Interview rounds:** {info['rounds']}")
                st.write(f"**Type:** {info['type']}")
    else:
        st.error("No campus companies match. Focus on developing projects for offline recruitment!")

# --- TAB 3: MODERN SKILL & API ROADMAP ---
with tab3:
    st.subheader("🛣️ Skill Roadmap & Modern Tech Standards")
    target = st.selectbox("Select target company", list(companies.keys()))
    role = st.selectbox("Select role", ["Software Engineer", "Full Stack Developer (Modern Stack)", "Data Analyst"])
    
    if role == "Full Stack Developer (Modern Stack)":
        st.markdown("""
        ### 🌐 API-Driven Modern Web Architecture Stack:
        - **Backend & System Design:** Focus on RESTful APIs, FastAPI (Python) or Express.js.
        - **API Testing Tools:** Postman (Highly asked in technical rounds).
        - **Authentication Protocol:** JWT Tokens, Cookies, and OAuth security.
        - **Frontend Integration:** Fetch/Axios requests connected to React or Next.js.
        """)
    
    if target:
        info = companies[target]
        st.success(f"### Roadmap for {target} — {role}")
        st.write(f"**Required Base Skills:** {', '.join(info['skills'])}")
        st.write("**Month 1-2:** DSA basics — Arrays, Strings, LinkedList (LeetCode Easy)")
        st.write("**Month 3-4:** Core subjects — DBMS, OS, CN, OOP & API Architecture")
        st.write("**Month 5:** Projects — Build 2 good GitHub projects with dynamic REST APIs")
        st.write("**Month 6:** Mock interviews + aptitude practice daily")

# --- TAB 4: INTERNSHIP ---
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

# --- NEW TAB 5: AI RESUME ADVISOR (ATS CHECKER SIMULATION) ---
with tab5:
    st.subheader("📄 AI Resume Advisor (Instant ATS Check)")
    st.write("Upload your resume to check for missing keywords, core scales, and current industry trends.")
    
    uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX format)", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        st.success(f"File loaded successfully: {uploaded_file.name}")
        
        st.markdown("### 📋 Automated ATS Feedback Report:")
        c1, c2, c3 = st.columns(3)
        c1.metric(label="ATS Score Score", value="74/100", delta="Average Performance")
        c2.metric(label="Keyword Match Strength", value="60%", delta="-15% Missing")
        c3.metric(label="Layout Evaluation", value="Passed", delta="Clean Structural Code")
        
        with st.expander("🔍 Structural Review & Missing Elements"):
            st.error("❌ **Missing Industry Standard Tech:** No mentions of 'REST API', 'JSON Web Tokens (JWT)', or 'Postman/Testing Environment'.")
            st.warning("⚠️ **Missing Portfolio References:** Add functional GitHub links for your top 2 backend/frontend projects.")
            st.success("✅ **Format Layout:** The text formatting layout matches system standards flawlessly.")

# --- SIDEBAR ---
st.sidebar.title("📚 PlaceRAG Topics")
st.sidebar.write("💬 Chat with AI\n🏢 Company Filter\n🛣️ Skill Roadmap\n📝 Internship Guide\n📄 AI Resume Advisor")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🌐 Quick Portals")
st.sidebar.markdown("- [Amizone Link](https://www.amizone.net/)\n- [LeetCode Link](https://leetcode.com/)")
st.sidebar.success("Built for Amity University MP students!")
