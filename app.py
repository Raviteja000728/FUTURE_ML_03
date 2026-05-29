import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#00C8FF;
}

.insight-box{
    padding:15px;
    border-radius:10px;
    background-color:#1E1E1E;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    "<p class='main-title'>📄 Resume Screening System</p>",
    unsafe_allow_html=True
)

st.write(
    "AI-powered candidate screening and skill matching dashboard."
)

# -----------------------------------
# JOB ROLE SKILLS DATABASE
# -----------------------------------

job_roles = {

    "Machine Learning Engineer":[
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "SQL",
        "Docker",
        "AWS",
        "Git"
    ],

    "Data Scientist":[
        "Python",
        "Statistics",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "SQL",
        "Power BI"
    ],

    "Data Analyst":[
        "Excel",
        "SQL",
        "Power BI",
        "Tableau",
        "Python"
    ],

    "AI Engineer":[
        "Python",
        "LLM",
        "LangChain",
        "Machine Learning",
        "Deep Learning",
        "Vector Database",
        "Docker",
        "Git"
    ]
}

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Candidate Information")

candidate_name = st.sidebar.text_input(
    "Candidate Name",
    "Raviteja"
)

job_role = st.sidebar.selectbox(
    "Target Job Role",
    list(job_roles.keys())
)

education = st.sidebar.selectbox(
    "Education",
    [
        "B.Tech",
        "M.Tech",
        "B.Sc",
        "M.Sc",
        "PhD"
    ]
)

experience = st.sidebar.slider(
    "Years of Experience",
    0,
    15,
    2
)

skills = st.sidebar.text_area(
    "Candidate Skills (comma separated)",
    "Python, Machine Learning, Deep Learning, TensorFlow, SQL"
)

# -----------------------------------
# PROCESS SKILLS
# -----------------------------------

candidate_skills = [
    skill.strip()
    for skill in skills.split(",")
]

required_skills = job_roles[job_role]

matched_skills = []

missing_skills = []

for skill in required_skills:

    if skill.lower() in [
        s.lower() for s in candidate_skills
    ]:
        matched_skills.append(skill)

    else:
        missing_skills.append(skill)

# -----------------------------------
# MATCH SCORE
# -----------------------------------

match_score = (
    len(matched_skills)
    /
    len(required_skills)
) * 100

# Experience Bonus

match_score += min(
    experience * 2,
    10
)

match_score = min(
    match_score,
    100
)

# -----------------------------------
# RANKING
# -----------------------------------

if match_score >= 85:
    rank = 1
    recommendation = "Strong Candidate ✅"

elif match_score >= 70:
    rank = 2
    recommendation = "Good Candidate 👍"

elif match_score >= 50:
    rank = 3
    recommendation = "Average Candidate ⚠️"

else:
    rank = 4
    recommendation = "Needs Improvement ❌"

# -----------------------------------
# KPI SECTION
# -----------------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Match Score",
    f"{match_score:.1f}%"
)

col2.metric(
    "Matched Skills",
    len(matched_skills)
)

col3.metric(
    "Missing Skills",
    len(missing_skills)
)

col4.metric(
    "Candidate Rank",
    rank
)

st.divider()

# -----------------------------------
# PROFILE SUMMARY
# -----------------------------------

st.subheader("👤 Candidate Profile")

profile_df = pd.DataFrame({

    "Field":[
        "Candidate Name",
        "Job Role",
        "Education",
        "Experience"
    ],

    "Value":[
        candidate_name,
        job_role,
        education,
        f"{experience} Years"
    ]
})

st.dataframe(
    profile_df,
    use_container_width=True
)

# -----------------------------------
# SKILL MATCHING
# -----------------------------------

col1,col2 = st.columns(2)

with col1:

    st.subheader("✅ Matched Skills")

    if matched_skills:

        for skill in matched_skills:
            st.success(skill)

with col2:

    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.error(skill)

# -----------------------------------
# HIRING RECOMMENDATION
# -----------------------------------

st.subheader("📋 Hiring Recommendation")

if match_score >= 85:

    st.success(
        f"""
        {candidate_name} is highly suitable
        for the role of {job_role}.

        Recommendation:
        Proceed to Interview Round.
        """
    )

elif match_score >= 70:

    st.warning(
        f"""
        {candidate_name} is a good fit
        but requires minor upskilling.

        Recommendation:
        Technical Assessment.
        """
    )

elif match_score >= 50:

    st.info(
        f"""
        Candidate has partial skill match.

        Recommendation:
        Training Required.
        """
    )

else:

    st.error(
        f"""
        Candidate currently lacks
        key role requirements.

        Recommendation:
        Not Recommended.
        """
    )

# -----------------------------------
# SKILL GAP ANALYSIS
# -----------------------------------

st.subheader("📊 Skill Gap Analysis")

gap_df = pd.DataFrame({

    "Required Skills": required_skills,

    "Status":[

        "Available"
        if skill in matched_skills
        else "Missing"

        for skill in required_skills
    ]
})

st.dataframe(
    gap_df,
    use_container_width=True
)

# -----------------------------------
# AI INSIGHTS
# -----------------------------------

st.subheader("🤖 AI Insights")

if match_score >= 85:

    st.success(
        f"""
        Candidate demonstrates strong
        alignment with the role.

        Key strengths:
        {', '.join(matched_skills)}

        Recommended for immediate
        interview consideration.
        """
    )

elif match_score >= 70:

    st.warning(
        f"""
        Candidate shows good potential.

        Missing skills:
        {', '.join(missing_skills)}

        Upskilling recommended.
        """
    )

else:

    st.error(
        f"""
        Significant skill gaps identified.

        Focus areas:
        {', '.join(missing_skills)}
        """
    )

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "Machine Learning Internship Project | Resume Screening System"
)