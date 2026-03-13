<p align="center">
  <img src="header.png" width="100%">
</p>

# 🧠 AI Resume Analyzer

AI Resume Analyzer is a **Natural Language Processing (NLP) based web application** that analyzes resumes and compares them with job descriptions to calculate an **ATS-style match score**.

This tool helps job seekers understand **how well their resume matches a job role** by identifying **skills present in the resume and missing skills required by the job description**.

---

# 🚀 Features

✔ Upload Resume in **PDF format**
✔ Extract **technical skills automatically**
✔ Compare resume with **job description**
✔ Calculate **ATS match score**
✔ Identify **missing skills**
✔ Simple **interactive web interface**

---

# 🛠 Tech Stack

* **Python**
* **Streamlit**
* **spaCy (NLP)**
* **pdfplumber (PDF text extraction)**

---

# 📂 Project Structure

```
AI-Resume-Analyzer
│
├── app.py
├── skills.py
├── requirements.txt
├── README.md
└── screenshots
      ├── upload.png
      ├── skills.png
      └── match.png
```

---

# ⚙ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
```

### 2️⃣ Navigate to project folder

```
cd AI-Resume-Analyzer
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Install spaCy model

```
python -m spacy download en_core_web_sm
```

### 5️⃣ Run the application

```
streamlit run app.py
```

The application will start in your browser.

---

# 📸 Application Screenshots

## 1️⃣ Upload Resume Interface

![Upload Resume](upload.png)

This screen allows the user to **upload their resume in PDF format** and paste a job description for analysis.

---

## 2️⃣ Skills Extracted from Resume

![Skills Extracted](skills.png)

The system automatically **detects technical skills** present in the uploaded resume.

Example detected skills:

```
Python
SQL
Machine Learning
React
```

---

## 3️⃣ ATS Match Score & Missing Skills

![Match Score](match.png)

The system compares resume skills with the job description and calculates:

* **Match Score**
* **Missing Skills**

Example output:

```
Match Score: 72%
```

Missing Skills:

```
Docker
AWS
Kubernetes
```

---

# 💡 How It Works

1️⃣ Resume text is extracted from the uploaded **PDF file**.

2️⃣ NLP techniques are used to **identify skills** in the resume.

3️⃣ Skills are compared with the **job description requirements**.

4️⃣ The system calculates an **ATS-style match score** and highlights **missing skills**.

---

# 📈 Example Workflow

Upload Resume → Extract Skills → Compare with Job Description → Generate ATS Score

---

# 🎯 Future Improvements

* Advanced skill detection using **machine learning**
* Resume improvement suggestions
* Job recommendation system
* Deployment as a **cloud web application**

---

# 👨‍💻 Author

Developed as an **AI/NLP project for learning and demonstration purposes**.

This project demonstrates practical use of **Python, NLP, and web application development**.

---
