import streamlit as st
import os
from utils import extract_text_from_pdf, extract_skills, extract_email, extract_phone, load_skills, calculate_similarity

st.set_page_config(page_title="Resume Analyzer", layout="wide")
st.title("📄 Resume Analyzer")

skills_list = load_skills()

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if uploaded_resume and jd_text:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        resume_skills = extract_skills(resume_text, skills_list)
        jd_skills = extract_skills(jd_text, skills_list)
        matched = list(set(resume_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))
        similarity = calculate_similarity(resume_text, jd_text)

    st.success("Analysis Complete!")
    
    st.subheader("📬 Contact Info")
    st.write(f"**Email**: {email}")
    st.write(f"**Phone**: {phone}")

    st.subheader("✅ Skill Match")
    st.write(f"**Matched Skills:** {', '.join(matched) if matched else 'None'}")
    st.write(f"**Missing Skills:** {', '.join(missing) if missing else 'None'}")

    st.subheader("🔍 Similarity Score")
    st.progress(int(similarity))
    st.write(f"**Similarity Score**: {similarity}%")
