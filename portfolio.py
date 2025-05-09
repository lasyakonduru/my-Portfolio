# -*- coding: utf-8 -*-
"""portfolio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ydmlGrOUqliwsyzBDbbXQeeob4EJI61L
"""

# pip install streamlit streamlit-lottie plotly

# portfolio.py
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import requests
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Lasya Priya Konduru Portfolio", layout="wide", page_icon="📊")

import json

# Load Lottie Animations Locally
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

hero_lottie = load_lottiefile("Animation 1.json")

# Global Styles
st.markdown("""
<style>
    html, body, [class*="css"] {
        background-color: #0e1117 !important;
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif;
        scroll-behavior: smooth;
    }
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #00c4ff;
        margin: 2rem 0 1rem 0;
        text-align: center;
    }

    button, .btn, .stButton>button {
        font-family: 'Segoe UI', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Welcome Section
col1, col2 = st.columns([1,2])
with col1:
    if hero_lottie:
        st_lottie(hero_lottie, height=400, key="hero")
with col2:
    st.markdown("### 👋 Hello, I am")
    st.markdown("# Lasya Priya Konduru")
    st.markdown("### Data Analyst | Data Scientist | Problem Solver 🌟")
    st.markdown("Welcome to explore ME!")
    st.download_button("📄 Download My Resume", data=open("Lasya___Resume.pdf", "rb"), file_name="Lasya_Konduru_Resume.pdf")

# About Section
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 id='about'>📌 About Me</h2>", unsafe_allow_html=True)

about_col1, about_col2 = st.columns([1, 2])

# --- LEFT COLUMN: Sticky Profile & Animation ---
with about_col1:
    st.markdown("""
    <style>
    .sticky-left {
        position: -webkit-sticky;
        position: sticky;
        top: 100px;
        align-self: flex-start;
        z-index: 1;
    }
    </style>
    <div class="sticky-left">
    """, unsafe_allow_html=True)

    st.image("Lass - Copy.png", caption="Lasya Priya Konduru", width=250)

    # Load Lottie animation
    home_lottie = load_lottiefile("Animation 2.json")
    if home_lottie:
        st_lottie(home_lottie, height=250, key="home-anim")

    st.markdown("</div>", unsafe_allow_html=True)

with about_col2:
    st.write("""
### Hi, I'm Lasya 🌸
A curious mind with a storyteller’s soul, I believe data isn’t just numbers — it’s emotion, insight, and impact waiting to be unlocked. 📊
Fueled by coffee ☕, inspired by good music 🎶, and deeply moved by great cinema 🎬, I find joy in both exploring patterns and creating them — whether that’s through code or a killer homemade dish (yes, I’m a proud food lover and maker 🍝✨).

Behind every dashboard, I bring a blend of empathy, communication, and conviction — turning complexity into clarity and ideas into action. I’m someone who leads with dedication, values, and vision, and thrives when managing teams or sparking collaboration that brings results.

If you’re looking for someone who’s data-driven and people-powered — that’s me. 💡
Let’s solve real problems, uncover meaningful stories, and maybe laugh a little along the way. 😄
    """)

    # Education Section
    st.markdown("<div id='education'></div>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .edu-section {
        text-align: center;
        margin-top: 3rem;
    }
    .edu-title {
        font-size: 1.8rem;
        font-weight: bold;
        color: #00c4ff;
        margin-bottom: 2rem;
    }
    .edu-cards {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
    }
    .edu-card {
        background: #3a5659;
        padding: 1.5rem;
        border-radius: 16px;
        width: 320px;
        box-shadow: 0 0 12px #00c4ff30;
        text-align: left;
    }
    .edu-card h4, h5{
        margin: 0 0 0.5rem 0;
        color: white;
    }
    .edu-card p {
        margin: 0;
        font-size: 14px;
        color: #ccc;
    }
    </style>

    <div class='edu-section'>
        <div class='edu-title'>🎓 Education</div>
        <div class='edu-cards'>
            <div class='edu-card'>
                <h4>Saint Louis University</h4>
                <h5>St Louis | Missouri</h5>
                <p>Master of Science in Analytics (2023–2024)</p>
                <p>GPA: 3.8</p>
            </div>
            <div class='edu-card'>
                <h4>Sreyas Institute of Engineering & Technology (Aff. JNTUH)</h4>
                <h5>Hyderabad | India</h5>
                <p>B.Tech in Computer Science (2018–2022)</p>
                <p>GPA: 3.2</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


    # Skills Pie Chart
    st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
    st.markdown(
    "<h2 style='text-align: center; color: #00c4ff; margin-top: 2rem;'>💡 Top Skills</h2>",
    unsafe_allow_html=True)

    st.markdown("""
    <style>
    .skills-section {
        margin-top: 4rem;
        text-align: center;
    }
    .skills-title {
        font-size: 1.8rem;
        font-weight: bold;
        color: #00c4ff;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Pie chart
    skills = ["Python", "SQL", "R", "Power BI", "Tableau", "AWS", "Machine Learning"]
    ratings = [95, 90, 85, 90, 85, 75, 90]

    fig = px.pie(
        names=skills,
        values=ratings,
        color_discrete_sequence=px.colors.sequential.Teal_r
    )
    fig.update_traces(
        textinfo='label+percent',
        textfont_size=14,
        marker=dict(line=dict(color='white', width=2))
    )
    fig.update_layout(
        height=450,
        showlegend=True,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(color='black', size=14)
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Certifications & Experience Timeline ---
    st.markdown("""
    <style>
    .cert-section, .exp-section {
        margin-top: 3rem;
        padding: 1rem 0;
        text-align: center;
    }

    .cert-section h2, .exp-section h2 {
        font-size: 1.8rem;
        font-weight: bold;
        color: #00c4ff;
        margin-bottom: 1.5rem;
    }

    .cert-list {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 2rem;
    }

    .cert-badge {
        background: #74bfc4;
        padding: 0.6rem 1.2rem;
        border-radius: 24px;
        font-size: 14px;
        font-weight: 500;
        color: #00c4ff;
        text-decoration: none !important;
        box-shadow: 0 4px 12px rgba(0, 196, 255, 0.15);
        transition: all 0.3s ease;
        display: inline-block;
    }

    .cert-badge:hover {
        background-color: #00c4ff;
        color: black !important;
        font-weight: 600;
        text-decoration: none !important;
        box-shadow: 0 6px 18px rgba(0, 196, 255, 0.3);
    }

    .exp-card {
        background-color: #062366;
        margin: 1rem auto;
        max-width: 700px;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        box-shadow: 0 0 10px #00c4ff20;
        text-align: left;
    }
    .exp-card h4 {
        margin: 0;
        color: white;
        font-size: 16px;
    }
    .exp-card p {
        margin: 0.3rem 0 0;
        color: #ccc;
        font-size: 14px;
    }
    </style>

    <div class="cert-section">
        <h2>📜 Certifications</h2>
        <div class="cert-list">
            <a class="cert-badge" href="https://cp.certmetrics.com/amazon/en/public/verify/credential" target="_blank">AWS Certified Data Analytics</a>
            <a class="cert-badge" href="https://skillshop.credential.net/64823a47-1671-4145-8310-ce9f57617521" target="_blank">Google Analytics</a>
            <a class="cert-badge" href="https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_tMpKmpA9LmihKJ8Tc_1738805509796_completion_certificate.pdf" target="_blank">Tata Group (Forage)</a>
            <a class="cert-badge" href="https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/BCG%20/Tcz8gTtprzAS4xSoK_BCG_tMpKmpA9LmihKJ8Tc_1726273601941_completion_certificate.pdf" target="_blank">BCG - Data Science (Forage)</a>
            <a class="cert-badge" href="https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/British%20Airways/NjynCWzGSaWXQCxSX_British%20Airways_tMpKmpA9LmihKJ8Tc_1727064432080_completion_certificate.pdf" target="_blank">British Airways (Forage)</a>
            <a class="cert-badge" href="https://www.credly.com/badges/ec7425f2-d275-4614-88c7-9eee8b02a84f/linked_in_profile" target="_blank">AWS Educate: Databases</a>
        </div>
    </div>

    <div class="exp-section">
        <h2>💼 Experience </h2>
        <div class="exp-card">
            <h4>Google Analytics Specialist, Resilience Inc.</h4>
            <p>Aug 2024 – Present  |  9 months</p>
        </div>
        <div class="exp-card">
            <h4>Data Scientist Intern, Coincent.ai</h4>
            <p>Jul 2022 – Dec 2022  |  6 months</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>🎯Projects</h2>", unsafe_allow_html=True)

projects = [
    {
        "Title": "Optimizing E-Commerce Logistics using Advanced SQL",
        "Description": "Designed and implemented SQL-powered analytics and reporting solutions to optimize order fulfillment, sales trends, customer segmentation, and shipping cost efficiency for an e-commerce platform with 51K+ transactions. Utilized Advanced SQL Techniques such as Window Functions, Common Table Expressions (CTEs), RANK(), Indexing, and Partitioning to enhance query performance by 40% and improve business decision-making.",
        "Skills": "SQL · Business Intelligence (BI) · Python (Programming Language) · Microsoft Power BI",
        "Link": "https://github.com/lasyakonduru/E-Commerce-Analysis-Using-Advanced-SQL",
        "Category": ["🛠SQL & Data Eng", "📊BI & Analytics", "📈Data Viz"]

    },
    {
        "Title": "Unraveling Viral News: Decoding the Dynamics of Social Media Engagement and Article Popularity",
        "Description": "This is a data-driven exploration into the factors that make news articles go viral on platforms like Facebook, LinkedIn, and GooglePlus. Using sentiment analysis, topic modeling, and predictive modeling, this project identifies key characteristics—such as sentiment, topics, hashtags, and mentions—that drive engagement. By analyzing platform-specific trends and building machine learning models, the project offers actionable insights into how content creators can optimize their strategies to maximize social media reach.",
        "Skills": "Real-time Analytics · Model Validation · Machine Learning · Statistical Analysis · Big Data Technologies · Python (Programming Language) · Microsoft Power BI",
        "Link": "https://github.com/lasyakonduru/Unraveling-Viral-News-across-social-media",
        "Category": ["🧠ML", "📈Data Viz", "🗣NLP"]
    },
    {
        "Title": "Web App for Sentiment Analyzer: A Comprehensive Tool for Analyzing Text and Dataset Sentiments",
        "Description": "A powerful and user-friendly tool for analyzing sentiments in text and datasets. This app leverages advanced sentiment analysis techniques to provide real-time insights, helping users classify text as Positive, Negative, or Neutral, and visualize sentiment trends for better decision-making.",
        "Skills": "Web Development · Machine Learning · Python (Programming Language), Sentiment Analysis, NLP",
        "Link": "https://github.com/lasyakonduru/Web-app-for-Sentiment-Analyzer-A-Comprehensive-Tool-for-Analyzing-Text-and-Dataset-Sentiments",
        "AppLink": "https://sentiment-analyz.streamlit.app/",
        "Category": ["💻Web Dev", "🗣NLP"]
    },
    {
        "Title": "Banking Customer Churn Prediction Using a Neural Network",
        "Description": "Developed a predictive model for banking customer churn using a neural network. This project involved analyzing customer data, performing feature engineering, and building a neural network model to identify customers at risk of leaving. Key metrics such as accuracy and F1-score were optimized to improve prediction quality, providing actionable insights for customer retention strategies.",
        "Skills": "Extract, Transform, Load (ETL) · Model Validation · Machine Learning · Deep Learning · Predictive Modeling · Feature Selection · Customer Analysis · Python (Programming Language) · Data Science Methodologies",
        "Link": "https://github.com/lasyakonduru/Banking-Customer-Churn-Prediction-Using-a-Neural-Network",
        "Category": ["🧠ML"]
    },
    {
        "Title": "CIFAR-10 Image Classification with Convolutional Neural Networks (CNNs)",
        "Description": "Developed a deep learning model to classify images into 10 categories from the CIFAR-10 dataset using Convolutional Neural Networks (CNNs). This project involved creating a baseline and enhanced model, applying data preprocessing, and evaluating model performance through metrics like accuracy, recall, and confusion matrices. The enhanced model, designed for real-world application in automotive safety systems, demonstrated improved accuracy and recall, with potential use in preventing deer-vehicle collisions. Implemented in TensorFlow/Keras with visualizations for model insights.",
        "Skills": "Machine Learning · Deep Learning · Data Science · Python (Programming Language) · Convolutional Neural Networks (CNN)",
        "Link": "https://github.com/lasyakonduru/CIFAR-10-Image-Classification-with-CNNs-Baseline-and-Enhanced-Models",
        "Category": ["🧠ML"]
    },
    {
        "Title": "Bayesian Classification of Cammeo and Osmancik: RiceVarieties",
        "Description": "This project employs Bayesian logistic regression to classify Cammeo and Osmancik rice varieties based on morphological features. By analyzing variables such as area, perimeter, and convex area, the study aims to improve classification accuracy while quantifying uncertainty in predictions. The results demonstrate the effectiveness of Bayesian methods in agricultural data analysis, highlighting significant predictors and validating model performance through diagnostic metrics and cross-validation.",
        "Skills": "Extract, Transform, Load (ETL) · Model Validation · Machine Learning · Data Handling and Preprocessing · Predictive Modeling · Feature Selection · Statistical Analysis · R programming · Decision-Making · Agricultural Research · Performance Measurement · Analytical thinking · Attention to Detail",
        "Link": "https://github.com/lasyakonduru/Bayesian-Classification-of-Cammeo-and-Osmancik-Rice-Varieties",
        "Category": ["🧠ML", "🧬BIO", " 🛠SQL & Data Eng"]
    },
    {
        "Title": "Enhancing Sales Performance and Operational Efficiency in a Superstore Using AWS Athena and QuickSight",
        "Description": "This project aims to analyze and improve a superstore's sales performance and operational efficiency using AWS Athena for data querying and AWS QuickSight for visualization. The comprehensive analysis covers various business aspects, including customer segmentation, shipping logistics, discount impacts, and overall sales performance.",
        "Skills": "Extract, Transform, Load (ETL) · AWS Glue · SQL · Amazon Web Services (AWS) · Business Intelligence (BI) · Data Handling and Preprocessing · Performance Optimization · Efficiency Optimization · Customer Analysis · Amazon QuickSight · Data Storage and Management · AWS Identity and Access Management (AWS IAM) · Decision-Making · Amazon Athena · Analytical Skills · Performance Measurement · Reports and Dashboards · Analytical thinking · Attention to Detail",
        "Link": "https://github.com/lasyakonduru/superstore-sales-data-analysis",
        "Category": ["📊BI & Analytics", "🛠SQL & Data Eng", "📈Data Viz"]
    },
    {
        "Title": "Breast Cancer Analysis",
        "Description": "This project analyzes the Breast Cancer Diagnostic dataset to create a machine-learning model that can accurately differentiate between benign and malignant breast tumors. Real-valued characteristics derived from breast mass sample cell nuclei are used for exploratory data analysis to find trends, control class imbalances, and address data distributions. The ultimate goal is to construct a prediction model that improves breast cancer screening accuracy, hence increasing early diagnosis and patient outcomes. To achieve clinical model robustness and interpretability, feature selection, data preprocessing, model creation, and validation are required.",
        "Skills": "Extract, Transform, Load (ETL) · Model Validation · Machine Learning · Data Handling and Preprocessing · Jupyter · Feature Selection · Statistical Analysis · Decision-Making · Problem Solving · Python (Programming Language) · Analytical Skills · Performance Measurement · Analytical thinking · Attention to Detail",
        "Link": "https://github.com/lasyakonduru/Breast-Cancer-Wisconsin",
        "Category": ["🧠ML", "📈Data Viz", "🧬BIO", "📊BI & Analytics"]
    },
    {
        "Title": "Steel Manufacturing Analysis",
        "Description": "This study used performance measures to compare predictive models and estimated the benefit/cost ratio by dividing accuracy by computing time. Analyzing the elements that lead a customer from exploring to buying helps improve the sales funnel, customer experience, and income. This study guides predictive modeling decision-making by identifying models with the optimum performance-computational efficiency trade-off.",
        "Skills": "Extract, Transform, Load (ETL) · Model Validation · Machine Learning · Cost-Benefit Analysis · Business Intelligence (BI) · Data Handling and Preprocessing · Predictive Modeling · Jupyter · Feature Selection · Data Mining · Efficiency Optimization · Customer Analysis · Statistical Analysis · Data Visualization · Decision-Making · Technical Documentation · Python (Programming Language) · Analytical Skills · Performance Measurement · Reports and Dashboards · Analytical thinking · Attention to Detail",
        "Link": "https://github.com/lasyakonduru/Steel-Manufacturing-Analysis",
        "Category": ["🧠ML", "📊BI & Analytics", "🛠SQL & Data Eng", "📈Data Viz"]
    },
    {
        "Title": "Healthy You",
        "Description": "The website Healthy You Blog is an online platform dedicated to promoting wellness and a healthy lifestyle. It features a clean, user-friendly interface to engage visitors with health-related content. The blog covers topics ranging from nutritious recipes and diet tips to exercise routines and mental health advice. Each post is thoughtfully crafted to provide valuable insights and practical advice for individuals looking to improve their health and well-being. The site's responsive design ensures a seamless browsing experience across different devices, making it accessible to a wide audience interested in enhancing their lifestyle through informed health choices.",
        "Skills": "HTML5 · Web Design · Cascading Style Sheets (CSS) · Responsive Web Design · User Interface Design · Web Content Writing · JavaScript · Attention to Detail",
        "Link": "https://github.com/lasyakonduru/healthy_you-blog-",
        "AppLink": "https://lasyakonduru.github.io/healthy_you-blog-/",
        "Category": ["💻Web Dev"]
    },
    {
        "Title": "Prioritized to-do list",
        "Description": "Scope: Developed a user-friendly web application to boost personal and professional productivity. The software uses HTML, Bootstrap, JavaScript, and CSS to create a dynamic UI for task management. Feedback: The app's intuitive design and excellent prioritization functions were highly praised. Color-coding activities by priority and filtering by urgency were extremely useful. Measurable Results: A user study showed a 40% improvement in productivity and task completion rates after implementing the priority-based to-do list. A weekly report feature was praised for delivering task progress insights and improving planning and time management.",
        "Skills": "HTML5 · Cascading Style Sheets (CSS) · Responsive Web Design · Software Testing · Data Storage and Management · Full-Stack Development · Technical Documentation · Node.js · Performance Measurement · Reports and Dashboards · JavaScript · Attention to Detail",
        "Link": "https://github.com/lasyakonduru/prioritized_to-do",
        "Category": ["💻Web Dev"]
    },
    {
        "Title": "Prediction of its Crop and its Yield",
        "Description": "I worked on a project focused on enhancing agricultural productivity through the use of technology. We created a website that employed Machine Learning techniques to predict the best crop to plant based on current weather and soil conditions. Additionally, our system could estimate the expected crop yield by considering factors like weather, soil quality, and historical crop data. By integrating data from various sources and using data analytics and prediction analysis, our project aimed to increase farmers' profit margins and improve overall crop yield productivity.",
        "Skills": "Data Integration · Extract, Transform, Load (ETL) · Model Validation · Web Development · Machine Learning · Business Intelligence (BI) · Data Handling and Preprocessing · Predictive Modeling · User Interface Design · Feature Selection · Data Mining · Project Management · Statistical Analysis · Decision-Making · Geographic Analysis · Technical Documentation · Database Management System (DBMS) · Python (Programming Language) · Analytical Skills · Agricultural Research · Performance Measurement · Reports and Dashboards · Analytical thinking · Attention to Detail",
        "Category": ["🧠ML", "🧬BIO", "🛠SQL & Data Eng", "💻Web Dev"]
    },
    {
        "Title": "McD sales dashboard in South America",
        "Description": "The 2022 Sales Dashboard for McDonald’s South America displays a robust financial year, with total sales reaching $2,544 million, 85% of the set goal, and a profit of $890 million at 89% of the target. The customer base touched 87 million, achieving 87% of the customer target. The sales trend over 2021-2022 indicates a generally positive trajectory, with 2022 surpassing the previous year's figures most months. Customer satisfaction rates are high in Hygiene and Availability, at 93% and 95%, respectively, while Speed and Service have room for improvement. The map illustrates sales distribution across countries, with standout figures in two specific nations, highlighting areas of strength and potential growth opportunities in the region.",
        "Skills": "Extract, Transform, Load (ETL) · Microsoft Excel · Business Intelligence (BI) · Data Handling and Preprocessing · User Interface Design · Customer Analysis · Geographic Analysis · Excel Dashboards · Analytical Skills · Performance Measurement · Reports and Dashboards · Analytical thinking · Attention to Detail",
        "Category": ["📊BI & Analytics", "🛠SQL & Data Eng", "📈Data Viz"]
    }
]

# --- Filter Buttons (Horizontal only) ---
categories = ["🌐All", "🧠ML", "📊BI & Analytics", "💻Web Dev", "🛠SQL & Data Eng", "📈Data Viz", "🗣NLP", "🧬BIO"]
st.markdown("<div class='filter-row'>", unsafe_allow_html=True)
filter_cols = st.columns(len(categories))
for i, cat in enumerate(categories):
    if filter_cols[i].button(cat, key=cat):
        st.session_state.selected_category = cat
st.markdown("</div>", unsafe_allow_html=True)

# Fix: Category selection logic with default
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "🌐All"

selected = st.session_state.selected_category
filtered_projects = [p for p in projects if selected == "🌐All" or selected in p["Category"]]

# --- Card Grid Styling ---
st.markdown("""
<style>
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}
.card {
    background: #1c1f26;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 0 12px #00c4ff22;
    transition: transform 0.3s;
    margin-bottom: 1.5rem;
}
.card:hover {
    transform: scale(1.02);
}
.card h4 {
    margin-bottom: 0.6rem;
    font-size: 18px;
    color: #ffffff;
}
.card p {
    font-size: 15px;
    color: #dddddd;
}
.card .skills {
    font-size: 13px;
    color: #cccccc;
    margin-top: 0.6rem;
}
.card .button-container {
    margin-top: 1rem;
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}
.card .btn {
    background-color: #00c4ff;
    color: black !important;
    font-weight: bold;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    display: inline-block;
    transition: background-color 0.3s;
}
.card .btn:hover {
    background-color: #009dcf;
    color: white !important;
    text-decoration: none;
}
.filter-row {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin-top: 1rem;
}
.filter-btn {
    background: #0e1117;
    border: 2px solid #00c4ff;
    border-radius: 25px;
    padding: 0.5rem 1rem;
    color: white;
    font-weight: 600;
    cursor: pointer;
}
.filter-btn:hover {
    background: #00c4ff;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Render Project Cards
st.markdown("<div class='card-grid'>", unsafe_allow_html=True)
for proj in filtered_projects:
    github_link = f"<a class='btn' href='{proj.get('Link')}' target='_blank'>📁 GitHub Repo</a>" if proj.get("Link") else ""
    app_link = f"<a class='btn' href='{proj.get('AppLink')}' target='_blank'>🚀 Live App</a>" if proj.get("AppLink") else ""

    # Inside rendering loop
    button_block = ""
    if proj.get("Link") or proj.get("AppLink"):
        button_block = "<div class='button-container'>"
        if proj.get("Link"):
            button_block += f"<a class='btn' href='{proj['Link']}' target='_blank'>📁 GitHub Repo</a>"
        if proj.get("AppLink"):
            button_block += f"<a class='btn' href='{proj['AppLink']}' target='_blank'>🚀 Live App</a>"
        button_block += "</div>"

    st.markdown(f"""
        <div class='card'>
            <h4>{proj['Title']}</h4>
            <p>{proj['Description']}</p>
            <div class='skills'><b>Skills:</b> {proj['Skills']}</div>
            {button_block}
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- CONTACT / FOOTER SECTION ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)

st.markdown("""
<style>
.footer {
    background-color: #1c1f26;
    width: 100%;
    padding: 2.5rem 1rem;
    margin: 0;
    border-radius: 0;
    box-shadow: inset 0 1px 0 #333;
    text-align: center;
}
.footer h2 {
    font-size: 26px;
    color: white;
    margin-bottom: 0.5rem;
}
.footer p, .footer a {
    color: #f1f1f1;
    font-size: 16px;
}
.footer .contact-icons {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 1rem;
}
.footer .contact-icons a {
    font-size: 26px;
    color: #00c4ff;
    transition: transform 0.3s ease;
}
.footer .contact-icons a:hover {
    transform: scale(1.2);
    color: white;
}
.footer .bottom-text {
    color: #888;
    margin-top: 1.5rem;
    font-size: 13px;
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<div class="footer">
    <h2>📫 Contact Me</h2>
    <p><i class="fas fa-map-marker-alt"></i> Sammamish, WA 98075, United States</p>
    <div class='contact-icons'>
        <a href="mailto:konduru.lasya@gmail.com" target="_blank"><i class="fas fa-envelope"></i></a>
        <a href="https://www.linkedin.com/in/lasya-priya-k/" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/lasyakonduru" target="_blank"><i class="fab fa-github"></i></a>
    </div>
    <div class="bottom-text">© 2025 Lasya Priya Konduru. All rights reserved.</div>
</div>
""", unsafe_allow_html=True)
