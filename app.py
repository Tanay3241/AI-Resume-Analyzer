import streamlit as st
import pdfplumber
import spacy
from skills import SKILLS

nlp = spacy.load("en_core_web_sm")

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text.lower()

def extract_skills(text):
    doc = nlp(text)
    found_skills = []
    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)
    return list(set(found_skills))

st.title("AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if resume_file:
    resume_text = extract_text(resume_file)
    resume_skills = extract_skills(resume_text)

    st.subheader("Skills Detected in Resume")
    st.write(resume_skills)

    if job_description:
        jd_skills = extract_skills(job_description.lower())

        match = len(set(resume_skills) & set(jd_skills))
        score = int((match / len(jd_skills)) * 100) if jd_skills else 0

        st.subheader("ATS Match Score")
        st.success(str(score) + "%")

        missing_skills = list(set(jd_skills) - set(resume_skills))

        st.subheader("Missing Skills")
        st.write(missing_skills)
