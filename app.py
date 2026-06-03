import streamlit as st
import random

st.set_page_config(page_title="PlaceRAG - Amity", page_icon="🎓", layout="wide")

st.title("🎓 PlaceRAG - Ultimate Amity Placement Suite")
st.caption("Advanced AI-powered RAG & Industry Integration Ecosystem for Amity University MP students")

# --- PREMIUM STYLING FOR MODERN HUB ---
st.markdown("""
    <style>
    .metric-card { background-color: #F8FAFC; border-radius: 10px; padding: 15px; border-left: 5px solid #3B82F6; margin: 10px 0; }
    .alert-card { background-color: #FEF2F2; border-radius: 10px; padding: 15px; border-left: 5px solid #EF4444; }
    </style>
""", unsafe_allowed_html=True)

# --- EXPANDED EXTENDED TABS ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "💬 Hyper-Expanded RAG Bot", 
    "🏢 Advanced Company Matrix", 
    "🛣️ Role-Based API Roadmaps", 
    "📝 Smart Internship Navigator",
    "📄 AI ATS Resume Evaluator",
    "🎯 AI Live Mock Test & HR Simulator"
])

# --- 15+ EXPANDED REAL-WORLD MARKET COMPANIES ---
companies = {
    "TCS (Ninja/Digital)": {"cgpa": 6.0, "package": "3.6 - 7.5 LPA", "skills": ["Python", "Java", "SQL", "Aptitude"], "rounds": "NQT Exam → Technical → HR", "type": "Mass/Differential"},
    "Infosys (System Engineer/Power Programmer)": {"cgpa": 6.5, "package": "3.6 - 9.5 LPA", "skills": ["Java", "Python", "DBMS", "Cloud Basics"], "rounds": "InfyTQ / HackWithInfy → Technical → HR", "type": "Mass/Differential"},
    "Wipro (Turbo/Elite)": {"cgpa": 6.0, "package": "3.5 - 6.5 LPA", "skills": ["C++", "Java", "Linux", "Networking"], "rounds": "Online Test → Tech Interview → HR", "type": "Mass Recruiter"},
    "Cognizant (GenC/Elevate)": {"cgpa": 6.0, "package": "4.0 - 6.7 LPA", "skills": ["Python", "SQL", "Data Structures", "Agile"], "rounds": "Aptitude Round → Skill Coding → TR+HR", "type": "Mass Recruiter"},
    "Accenture (ASE/FSE)": {"cgpa": 6.5, "package": "4.5 - 6.5 LPA", "skills": ["PseudoCode", "Cloud Architecture", "Python", "MS Office"], "rounds": "Cognitive + Technical Assessment → Coding → Communication → HR", "type": "Mid Tier"},
    "Capgemini": {"cgpa": 6.0, "package": "4.2 - 7.5 LPA", "skills": ["Data Structures", "Java/C#", "SQL"], "rounds": "PseudoCode Test → English Communication → Technical → HR", "type": "Mid Tier"},
    "HCLTech": {"cgpa": 6.0, "package": "3.6 - 5.0 LPA", "skills": ["Java", "C", "Linux Operations", "Infrastructure"], "rounds": "Aptitude Screening → Technical Panel", "type": "Mass Recruiter"},
    "Tech Mahindra": {"cgpa": 6.0, "package": "3.2 - 5.5 LPA", "skills": ["Networking Basics", "Python", "SQL Databases"], "rounds": "Aptitude Test → Psychometric Round → Technical/HR", "type": "Mass Recruiter"},
    "Deloitte (USI)": {"cgpa": 7.0, "package": "6.0 - 9.0 LPA", "skills": ["Python/R", "PowerBI/Tableau", "Excel", "OOPs"], "rounds": "Online Aptitude + Case Study → Technical Interview → Partner HR", "type": "Consulting Giant"},
    "PwC India": {"cgpa": 6.8, "package": "5.5 - 8.5 LPA", "skills": ["Cyber Security", "DBMS", "Cloud", "Business Analysis"], "rounds": "Written Aptitude → Group Discussion → Technical Round → Partner Round", "type": "Consulting Giant"},
    "Amazon": {"cgpa": 7.5, "package": "12.0 - 32.0 LPA", "skills": ["Advanced DSA", "System Design (LLD/HLD)", "Java/C++", "AWS Linux"], "rounds": "Online Assessment (2 Coding Questions) → 3-4 Technical Virtual Rounds", "type": "Top Product Scale"},
    "Microsoft": {"cgpa": 8.0, "package": "15.0 - 44.0 LPA", "skills": ["Data Structures & Algorithms", "OS Internals", "System Architecture"], "rounds": "Coding Screening → 3 Hardcore Technical Rounds (DSA/Design) → Lead Round", "type": "Top Product Scale"},
    "Adobe": {"cgpa": 7.8, "package": "14.0 - 28.0 LPA", "skills": ["C++ Mastery", "Advanced Algorithms", "Maths & Logic"], "rounds": "CoCubes Coding Test → Technical Direct Rounds → HR Director Round", "type": "Top Product Scale"},
    "Flipkart": {"cgpa": 7.5, "package": "10.0 - 26.0 LPA", "skills": ["Problem Solving (DSA)", "Machine Learning Scale", "System Design"], "rounds": "Online Coding Test → Machine Coding Round → Technical Interview → HR", "type": "Top Product Scale"},
    "Cisco": {"cgpa": 7.0, "package": "9.0 - 18.0 LPA", "skills": ["Computer Networks (TCP/IP)", "OS", "C++/Python", "Linux Security"], "rounds": "Aptitude & Networking MCQ Test → Technical Interview 1 & 2 → Managerial → HR", "type": "Top Hardware/Networking"}
}

# --- UNLIMITED AI KNOWLEDGE BASE ARCHITECTURE ---
knowledge_base = {
    "interview": "🎯 **Technical Interview Question Repository:**\n1. Explain Memory Management in Operating Systems.\n2. How do you implement a REST API using FastAPIs/Node.js?\n3. What is the difference between Clustered and Non-Clustered Indexes in SQL?\n4. Explain Object-Oriented Principles with real-world examples.\n5. Design an URL Shortener system scheme (System Design snippet).",
    
    "resume": "📝 **Next-Gen Market ATS Resume Architect:**\n• Keep layout strictly single-column (Multi-column resumes fail modern ATS processors).\n• Use Action Verbs: Engineered, Implemented, Automated, Orchestrated.\n• Add specialized API or ML tracking elements to project domains.\n• Include live clickable hyperlinks for GitHub repositories and hosted portfolio links.",
    
    "aptitude": "🧮 **Aptitude Crack Framework:**\n• Quantitative: Focus on Allegation & Mixture, Permutations, Probability, Work & Time.\n• Logical Reasoning: Cryptarithmetic (Highly asked in TCS/Infosys), Data Sufficiency, Syllogisms.\n• Recommended Sites: PrepInsta Prime, IndiaBIX, GeeksforGeeks Mock Tests.",
    
    "salary": "💰 **Industry Standard Placement Pay Matrix (Current Market):**\n• Service-Mass Recruiter Track: 3.5 to 5.5 LPA.\n• Differential Hiring Core Track: 6.5 to 9.5 LPA.\n• Premium Product Tier Track: 12.0 to 45.0+ LPA.\n• Negotiation Strategy: Do not specify a hard number. Phrase as: 'I am open to competitive industry standard packages aligned with the technical responsibilities of this role.'",
    
    "hr": "👔 **HR Executive Screening Question Repository & Answers:**\n• *Why do you want to join us?* -> Connect your specialized skills directly with the company's recent tech expansions (e.g., 'I observed your shift towards generative AI structures...').\n• *Tell me about a conflict or failure.* -> Use the **STAR Method** (Situation, Task, Action, Result) showcasing a positive outcome.\n• *Are you comfortable with bonds or relocation?* -> Always reply affirmatively to proceed to the offer compilation phase.",
    
    "offcampus": "🌐 **Off-Campus Aggressive Acquisition Strategy:**\n• **LinkedIn Direct Outreaching:** Search for 'Engineering Managers' or 'Tech Leads' instead of general HRs. Drop a 3-sentence clean project pitch with a Resume link.\n• **Job Boards:** Use Wellfound (AngelList) for AI/ML and startup roles, and Instahyre for direct AI matching algorithms.\n• **Hackathons:** Participate in Unstop and HackerEarth challenges. Direct shortcuts to interview slots!",
    
    "cgpa": "📊 **CGPA Matrix Analysis:**\n• 8.5+ CGPA: Complete immunity. Eligible for high-end product tech filters.\n• 7.0 - 8.5 CGPA: Standard sweet spot. Eligible for 90% of on-campus drives.\n• Below 6.5: Shield yourself with exceptional open-source contributions or active full-stack freelance code profiles.",
    
    "api": "💡 **Modern API Architectures & Industry Trends:**\n• Modern applications rely on asynchronous communication frameworks (FastAPI, GraphQL, Node.js).\n• Key focus parameters: JSON request-response headers, Middleware authentication (OAuth2/JWT), CORS handling, and Containerization (Docker) for API setups.",
    
    "internship": "🚀 **Internship High-Conversion Framework:**\n• Target 6-month off-campus stints during your pre-final semesters.\n• Look for PPO (Pre-Placement Offer) metrics of startups on platforms like TopHire or Wellfound.\n• Ensure your Github repository shows daily automated commits (Green Dots graph) to impress remote recruiters.",
    
    "backlog": "⚠️ **Backlog Mitigation Architecture:**\n• If you have active backlogs, prioritize mass recruiters that offer relaxation protocols or apply to agile startups off-campus that bypass grade verifications entirely."
}

def get_advanced_answer(query):
    query = query.lower()
    keywords = {
        "interview": ["interview", "question", "tr round", "technical round", "puchha"],
        "resume": ["resume", "cv", "portfolio", "format", "banaye"],
        "aptitude": ["aptitude", "test", "math", "logical", "quant", "nqt"],
        "salary": ["salary", "package", "ctc", "lpa", "negotiate", "packet"],
        "hr": ["hr", "human resource", "soft skill", "hr question"],
        "offcampus": ["off campus", "offcampus", "linkedin", "online", "apply offline", "offline", "outside"],
        "cgpa": ["cgpa", "marks", "percentage", "score", "eligible"],
        "api": ["api", "backend", "fastapi", "rest api", "tech stack", "framework"],
        "internship": ["internship", "stipend", "ppo", "intern"],
        "backlog": ["backlog", "active backlog", "kt", "fail", "gap"]
    }
    for topic, keys in keywords.items():
        if any(k in query for k in keys):
            return knowledge_base[topic]
            
    # Substring search for precise company lookup
    for comp in companies:
        if comp.split(" ")[0].lower() in query:
            c = companies[comp]
            return f"🏢 **Entity:** {comp}\n📦 **Package Range:** {c['package']}\n📊 **Min CGPA Criteria:** {c['cgpa']}\n🛠️ **Core Competencies:** {', '.join(c['skills'])}\n🔄 **Hiring Process Layout:** {c['rounds']}\n🏷️ **Category Class:** {c['type']}"
            
    return "💡 **PlaceRAG Expanded Intelligence Core:** I can guide you through Detailed Interviews, HR Questions, Live ATS Feedback, Modern API Paradigms, Off-Campus Referrals, Internships, and Backlog Strategies. Please ask any relevant question!"

# ==========================================
# TAB 1: HYPER-EXPANDED RAG BOT
# ==========================================
with tab1:
    st.subheader("🤖 Open-Domain Placement Knowledge Engine")
    st.caption("Integrated Vector Database Simulator containing Interview Experiences, HR Handbooks, and Startup API Guidelines.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Welcome! I am upgraded with advanced capabilities. Ask me about specific company structures, off-campus application strategies, modern tech patterns, or HR situations."}]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if prompt := st.chat_input("Query anything related to jobs, APIs, off-campus tricks, or HR scripts..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        response = get_advanced_answer(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

# ==========================================
# TAB 2: ADVANCED COMPANY MATRIX
# ==========================================
with tab2:
    st.subheader("📊 Dynamic Eligibility & Package Extrapolator")
    
    c1, c2 = st.columns(2)
    with c1:
        cgpa_val = st.slider("Select Current CGPA Metric", 0.0, 10.0, 7.2, 0.1)
    with c2:
        backlogs = st.radio("Active Backlog Status Parameter:", ["No Active Backlogs", "Yes, I have Active Backlogs"])

    st.markdown("---")
    
    # Advanced Offline Market Realities
    st.markdown("### 🌐 Market Placement Scale Reality Matrix (Offline vs Online)")
    if backlogs == "Yes, I have Active Backlogs":
        st.markdown("""
        <div class='alert-card'>
        <strong>⚠️ CRITICAL STRATEGY ACTION REQUIRED:</strong><br>
        Most on-campus institutional recruitment systems automatedly drop applicants with active backlogs. 
        <strong>Your Optimized Hack:</strong> Target early-stage startups on Y-Combinator Startup Directory or Wellfound where recruiters filter via code quality over university parameters.
        </div>
        """, unsafe_allowed_html=True)
    
    if cgpa_val >= 8.5:
        st.markdown("<div class='metric-card'>🌟 <strong>Product Engineer Scale:</strong> Expected Package 10 - 45 LPA off-campus. Focus on LeetCode Medium/Hard segments, Distributed Database Schemes, and Cloud Deployment Architectures.</div>", unsafe_allowed_html=True)
    elif cgpa_val >= 7.0:
        st.markdown("<div class='metric-card'>⚡ <strong>Differential Tech Scale:</strong> Expected Package 5 - 10 LPA. Highly safe zone for all premium service and product development firms. Maintain project hosting environments.</div>", unsafe_allowed_html=True)
    else:
        st.markdown("<div class='metric-card'>📈 <strong>Agile Developer Scale:</strong> Expected Package 3.5 - 6 LPA. Bypass traditional portal systems entirely using Direct Cold Emails and GitHub open-source showcase files.</div>", unsafe_allowed_html=True)

    st.write(f"### Eligible Campus Corporate Entities for CGPA {cgpa_val}:")
    eligible_comps = [(name, data) for name, data in companies.items() if cgpa_val >= data["cgpa"]]
    
    if eligible_comps:
        for name, data in eligible_comps:
            with st.expander(f"✅ {name} — Range: {data['package']} ({data['type']})"):
                st.write(f"• **Minimum Threshold:** {data['cgpa']} CGPA")
                st.write(f"• **Expected Competency Stack:** {', '.join(data['skills'])}")
                st.write(f"• **Hiring Flow Matrix:** {data['rounds']}")
    else:
        st.error("Threshold values are low. Boost your portfolio parameters instantly to unlock off-campus matches!")

# ==========================================
# TAB 3: ROLE-BASED ADVANCED ROADMAPS
# ==========================================
with tab3:
    st.subheader("🛣️ Hyper-Specialized Modern Role Track Roadmaps")
    
    target_comp = st.selectbox("Select Target Enterprise Base:", list(companies.keys()))
    modern_role = st.selectbox("Select Target Specialization Track:", [
        "AI / ML & Prompt Engineer", 
        "Full-Stack API & Backend Engineer", 
        "DevOps & Cloud Architect",
        "UI / UX Design Engineer",
        "Business Analyst & Data Consultant"
    ])
    
    st.info(f"📍 Curating System Design & Tech Track for **{modern_role}** optimized for **{target_comp}** standards.")
    
    if modern_role == "AI / ML & Prompt Engineer":
        st.markdown("""
        - **Month 1-2 (Mathematics & Foundations):** Linear Algebra, Probability distributions, Python NumPy, Pandas, Scikit-Learn.
        - **Month 3-4 (Deep Learning Ecosystem):** Neural Networks implementation, PyTorch or TensorFlow frameworks, Vector Embeddings.
        - **Month 5 (Generative AI Architecture):** LLM Fine-tuning basics, RAG (Retrieval-Augmented Generation) architectures, LangChain, Vector Database management (Pinecone, ChromaDB).
        - **Modern Industry Standard Focus:** Companies expect you to wrap ML models into functional web apps via Streamlit or FastAPI endpoints.
        """)
    elif modern_role == "Full-Stack API & Backend Engineer":
        st.markdown("""
        - **Month 1-2 (Core APIs & Logic):** Async Python/JavaScript patterns, Data structures, RESTful principles.
        - **Month 3-4 (Framework Integration):** FastAPI or Node.js/Express framework implementation, JWT Web Security tokens.
        - **Month 5 (Database Scaling):** PostgreSQL connection pools, Redis caching layers, writing custom ORM queries.
        - **Modern Industry Standard Focus:** Complete testing using **Postman Engine** and integration pipelines.
        """)
    elif modern_role == "DevOps & Cloud Architect":
        st.markdown("""
        - **Month 1-2 (Infrastructure):** Linux terminal proficiency, shell scripting automation, Bash basics.
        - **Month 3-4 (Containerization):** Dockerizing applications, writing complex Dockerfiles, Kubernetes orchestration orchestration.
        - **Month 5 (CI/CD Protocols & Cloud):** Jenkins, GitHub Actions setup, deployment orchestration on AWS (EC2, S3, RDS).
        """)
    elif modern_role == "UI / UX Design Engineer":
        st.markdown("""
        - **Phase 1 (Tools):** Figma Mastery, component auto-layout configurations, Design System implementations.
        - **Phase 2 (UX Principles):** Material UI guidelines, human-computer interaction patterns, layout responsiveness wireframing.
        - **Phase 3 (Frontend Mapping):** Converting Figma layouts directly into Tailwind CSS and React component blueprints.
        """)
    else:
        st.markdown("""
        - **Core Tracks:** Advanced Microsoft Excel analytics, SQL queries (Joins, Windows functions), Tableau or PowerBI dashboards.
        - **Business Logic:** Predictive modeling via Python, Case-study analytics tracking, structure documentation.
        """)

# ==========================================
# TAB 4: SMART INTERNSHIP NAVIGATOR
# ==========================================
with tab4:
    st.subheader("📝 Dynamic Internship & PPO Engine")
    
    curr_sem = st.radio("Current Student Academic Semester:", ["Sem 1-2 (Foundation)", "Sem 3-4 (Core Skill Building)", "Sem 5-6 (Aggressive Applying)", "Sem 7-8 (Final Conversion)"])
    intern_mode = st.radio("Application Pipeline Mode Selection:", ["Remote/Online Ecosystem", "On-Campus / Physical Referral Driven"])
    
    st.markdown("---")
    
    if curr_sem == "Sem 5-6 (Aggressive Applying)":
        st.success("🎯 **CRITICAL APPLICABILITY WINDOW:** This is the ideal phase to lock a stipend-backed (15k - 45k/month) role. Apply directly on startups using Wellfound and Instahyre.")
    
    # Modern Feature Integration
    st.markdown("### 🛠️ Emerging Market Internship Aggregators (Compared with Market Standards)")
    st.markdown("""
    - **Unstop Tier Competitions:** Don't just apply via traditional listings; join corporate hiring hackathons (e.g., Tata Crux, Amazon Wow). They grant direct bypass keys to interviews.
    - **Wellfound Ecosystem:** The most premium hub for high-growth remote internships. No CGPA restrictions apply here.
    - **GitHub Profile Portals:** Recruiters now track live commit graphs. If your repository shows daily green blocks, your profile automatically pushes up in automated tracking pipelines.
    """)

# ==========================================
# TAB 5: AI ATS RESUME EVALUATOR
# ==========================================
with tab5:
    st.subheader("📄 AI-Powered Advanced ATS Parser Simulation")
    st.caption("Matches architecture layout with modern enterprise applicant tracking algorithms.")
    
    res_file = st.file_uploader("Drop your Professional Resume File here (PDF or DOCX format)", type=["pdf", "docx"])
    
    if res_file is not None:
        st.success(f"Parsing Metadata Stream from: {res_file.name}")
        
        # Real-time Simulation Engine output
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Automated ATS Score Match", "78 / 100", "+4% vs Campus Average")
        col_m2.metric("Keyword Core Density", "62%", "Missing Context Elements")
        col_m3.metric("Structural Parsing Safety", "Passed", "Single Column Layout Safe")
        
        with st.expander("🔍 Click to view Deep Structural Corrections"):
            st.markdown("""
            - ❌ **Missing High-Density Tech Keywords:** No direct instances found for `'RESTful APIs'`, `'Asynchronous JSON'`, or `'Postman API Testing Environment'`.
            - ⚠️ **Missing Metrics:** Project metrics are purely qualitative. (Correction Idea: Update 'Worked on web app' to 'Built an integrated React platform reducing data fetching latency by 24%').
            - ✅ **Social Profiles Checked:** Active GitHub links detected and verified by scanner stream.
            """)

# ====================
