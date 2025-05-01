import streamlit as st
import os
from utils import (
    extract_text_from_pdf, extract_skills,
    extract_email, extract_phone,
    load_skills, calculate_similarity
)

# Page settings
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.markdown("<h1 style='text-align: center;'>📄 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load predefined skill list
skills_list = load_skills()

# Layout for inputs
col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])

with col2:
    jd_text = st.text_area("💼 Paste the Job Description", height=220)

# Once both inputs are provided
if uploaded_resume and jd_text:
    with st.spinner("🔍 Analyzing resume..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        resume_skills = extract_skills(resume_text, skills_list)
        jd_skills = extract_skills(jd_text, skills_list)
        matched = list(set(resume_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))
        similarity = calculate_similarity(resume_text, jd_text)

    st.success("✅ Analysis Complete!")
    st.markdown("---")

    # Contact Info
    with st.expander("📬 Contact Information", expanded=True):
        col1, col2 = st.columns(2)
        col1.markdown(f"**📧 Email:** `{email if email else 'Not Found'}`")
        col2.markdown(f"**📞 Phone:** `{phone if phone else 'Not Found'}`")

    # Skill Match
    with st.expander("✅ Skill Match Details", expanded=True):
        st.markdown("### 🎯 Matched Skills")
        st.success(", ".join(matched) if matched else "No matched skills.")
        
        st.markdown("### ❌ Missing Skills")
        st.warning(", ".join(missing) if missing else "No missing skills!")

    # Similarity Score
    st.markdown("### 📊 Similarity Score")
    similarity_percent = int(similarity)
    st.progress(similarity_percent)
    color = "green" if similarity_percent > 70 else "orange" if similarity_percent > 40 else "red"
    st.markdown(f"<h2 style='color:{color}'>{similarity_percent}% Match</h2>", unsafe_allow_html=True)

    # Summary Panel
    st.markdown("---")
    st.markdown("### 📄 Resume Summary")
    with st.expander("📝 View Extracted Resume Text"):
        st.markdown(f"<div style='color:#555;font-size:14px'>{resume_text[:3000]}</div>", unsafe_allow_html=True)
