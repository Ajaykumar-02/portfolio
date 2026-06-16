import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Ajay Kumar Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>


/* Normal Buttons */
.stButton > button {
    border-radius: 10px;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: red !important;
    color: white !important;
    transform: scale(1.05);
}

/* Download Button */
[data-testid="stDownloadButton"] button {
    border-radius: 10px;
    transition: all 0.3s ease;
}

[data-testid="stDownloadButton"] button:hover {
    background-color: red !important;
    color: white !important;
    transform: scale(1.05);
}

/* Link Buttons */
[data-testid="stLinkButton"] a {
    transition: all 0.3s ease;
}

[data-testid="stLinkButton"] a:hover {
    background-color: red !important;
    color: white !important;
    transform: scale(1.05);
}

           

.main-header {
    text-align: center;
    padding: 20px;
}

.skill-badge {
    display: inline-block;
    background-color: #2563eb;
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-weight: bold;
}

.project-card {
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-bottom: 20px;
}




.footer{
    text-align:center;
    padding:20px;
    margin-top:50px;
    border-top:2px solid #444;
}

.footer h3{
    margin-bottom:5px;
}

.footer-links{
    margin-top:10px;
}

.footer-links a{
    text-decoration:none;
    margin:0 10px;
    font-weight:bold;
    color:#4F8BF9;
}

.footer-links a:hover{
    color:red !important;
}


a {
    text-decoration: none !important;
}

a:hover {
    color: red !important;
    transition: 0.3s ease;
}
            
            

</style>
""", unsafe_allow_html=True)

# ==================================
# NAVBAR
# ==================================

selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "About",
        "Skills",
        "Projects",
        "Contact"
    ],
    icons=[
        "house",
        "person",
        "tools",
        "folder",
        "telephone"
    ],
    orientation="horizontal"
)

#sidebaar
with st.sidebar:

    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", width=180)

    st.title("Ajay Kumar")
    st.caption("AI & Machine Learning Enthusiast")

    st.markdown("---")

    st.markdown("""
### 📌 Quick Info

🎓 B.Tech AIML

📊 CGPA: 7.72

💻 12+ Projects

 🛠   20+ Skills                   

🚀 Aspiring ML Engineer
""")

    st.markdown("---")

    st.link_button(
        "💻 GitHub",
        "https://github.com/Ajaykumar-02"
    )

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/ajay-kumar-63a3b7326/"
    )


# ==================================
# HOME
# ==================================

if selected == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("profile.jpg"):
            st.image("profile.jpg", width=280)

        # Resume Download Button
        if os.path.exists("resume.pdf"):

            with open("resume.pdf", "rb") as pdf_file:

                st.download_button(
                    label="📄 Download Resume",
                    data=pdf_file,
                    file_name="Ajay_Kumar_Resume.pdf",
                    mime="application/pdf"
                )

    with col2:

        st.title("👋 Hi, I'm Ajay Kumar")

        st.subheader("AI & Machine Learning Enthusiast")

        st.markdown("""
### 🚀 Turning Data into Intelligent Solutions

Aspiring Machine Learning Engineer passionate about building AI-powered applications using Machine Learning, NLP, and Data Science.

Currently pursuing B.Tech in Artificial Intelligence & Machine Learning while developing real-world projects and continuously expanding my technical expertise.
""")

        col_a, col_b = st.columns(2)

        with col_a:
            st.link_button(
                "💻 GitHub",
                "https://github.com/Ajaykumar-02"
            )

        with col_b:
            st.link_button(
                "🔗 LinkedIn",
                "https://www.linkedin.com/in/ajay-kumar-63a3b7326"
            )

    st.markdown("---")

    st.subheader("📊 Portfolio Highlights")

    a, b, c, d = st.columns(4)

    a.metric("🚀 Projects", "12+")
    b.metric("🌐 Deployments", "8+")
    c.metric("🛠 Skills", "20+")
    d.metric("🎓 Current Semester", "7th")

    st.markdown("---")

    st.subheader("🎯 Career Objective")

    st.info("""
Seeking opportunities in Artificial Intelligence, Machine Learning, and Data Science where I can apply my technical knowledge, problem-solving abilities, and project experience to build impactful real-world solutions while continuously learning and growing.
""")

    st.markdown("---")

    st.subheader("🔥 Featured Technologies")

    c1, c2, c3, c4 = st.columns(4)

    c1.success("🐍 Python")
    c2.success("🤖 Machine Learning")
    c3.success("🧠 NLP")
    c4.success("🚀 Streamlit")


# ==================================
# ABOUT
# ==================================

elif selected == "About":

    st.title("👨 About Me")

    st.subheader("🚀 Professional Summary")

    st.info("""
Aspiring Machine Learning Engineer and B.Tech AI/ML student with practical experience in Python,
Machine Learning, Natural Language Processing (NLP), and Data Analysis.

Built multiple academic and personal projects focused on predictive analytics,
recommendation systems, emotion detection, and intelligent AI solutions.

Passionate about solving real-world problems using data-driven approaches and continuously
enhancing technical expertise through hands-on project development and continuous learning.

Currently seeking opportunities to apply my technical skills and contribute to impactful
AI and Machine Learning solutions.
""")

    # Education

    st.subheader("🎓 Education")

    st.success("""
🎓 B.Tech Artificial Intelligence & Machine Learning

🏫 Chandigarh Group of Colleges (CGC), Jhanjeri

📅 Jul 2024 – Jun 2027

📊 Current CGPA: 7.72

• Learning DSA, OOPs, Python, DBMS and AI/ML Fundamentals

• Developing Machine Learning and Data Science Projects
""")

    st.success("""
🎓 Diploma in Computer Science & Engineering

🏫 Longowal Polytechnic College, Mohali

📅 Dec 2021 – Jun 2024

🏆 Graduated with First Division

• Strong foundation in Python Programming

• Software Development Fundamentals
""")

    # Internship

    st.subheader("💼 Internship Experience")

    st.info("""
🤖 AI & ML Intern | Pashi Technology

📅 Jun 2025 – Jul 2025

• Built ML models using Python, Pandas and Scikit-Learn

• Performed Data Preprocessing and EDA

• Improved model performance through Feature Engineering
""")

    st.info("""
🌐 Web Development Intern

🏫 Chandigarh Institute of Engineering and Vocational Courses

📅 Jul 2023 – Jul 2023

• HTML, CSS and MySQL Training

• Developed Responsive Web Pages

• Hands-on Web Development Experience
""")

    # Certifications

    st.subheader("📜 Certifications & Learning")

    c1, c2 = st.columns(2)

    with c1:
        st.success("🐍 Basic Python Programming")
        st.success("🤖 Intro to Machine Learning")
        st.success("🧠 AI & ML Fundamentals")
        st.success("📊 SQL for Beginners")

    with c2:
        st.success("🌐 Web Development")
        st.success("🎤 Personality Development")
        st.success("🏆 AINCAT 2026 Participation")

    # Languages

    st.subheader("🌍 Languages")

    c1, c2, c3 = st.columns(3)

    c1.success(" English")
    c2.success(" Hindi")
    c3.success(" Punjabi")

# ==================================
# SKILLS
# ==================================

elif selected == "Skills":

    st.title("🛠 Technical Skills")

    # Programming

    st.subheader("💻 Programming")

    c1,c2,c3,c4 = st.columns(4)

    c1.success("🐍 Python")
    c2.success("📊 SQL")
    c3.success("💻 OOPs")
    c4.success("🧩 DSA")

    # Machine Learning

    st.subheader("🤖 Machine Learning")

    c1,c2,c3,c4 = st.columns(4)

    c1.info("📈 Regression")
    c2.info("🎯 Classification")
    c3.info("🧠 NLP")
    c4.info("📋 EDA")
    c4.info("🎤 Speech Recognition")


    # Data Science

    st.subheader("📊 Data Science")

    c1,c2,c3,c4 = st.columns(4)

    c1.warning("📐 Statistics")
    c2.warning("🧹 Data Preprocessing")
    c3.warning("🚀 Model Deployment")
    c4.warning("📑 Feature Engineering")

    # Libraries

    st.subheader("📚 Libraries")

    c1,c2,c3,c4 = st.columns(4)

    c1.success("🐼 Pandas")
    c2.success("🔢 NumPy")
    c3.success("📈 Matplotlib")
    c4.success("📉 Seaborn")

    c1,c2 = st.columns(2)

    c1.success("🤖 Scikit-Learn")
    c2.success("🧠 NLP Toolkit")

    # Tools

    st.subheader("🛠 Tools & Platforms")

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.info("🚀 Streamlit")
    c2.info("📒 Jupyter")
    c3.info("☁️ Colab")
    c4.info("🏆 Kaggle")
    c5.info("💻 GitHub")
    c5.info("🚀 API Integration")

    # Professional Skills

    st.subheader("🌟 Professional Skills")

    c1,c2,c3 = st.columns(3)

    c1.success("🧠 Logical Thinking")
    c2.success("🔍 Problem Solving")
    c3.success("📊 Data-Driven Decisions")

    c1,c2,c3 = st.columns(3)

    c1.info("🤝 Team Collaboration")
    c2.info("🗣 Effective Communication")
    c3.info("⚡ Adaptability")

    c1,c2 = st.columns(2)

    c1.warning("⏰ Time Management")
    c2.warning("📈 Continuous Learning")
# ==================================
# PROJECTS
# ==================================

elif selected == "Projects":

    st.title("🚀 Projects")

    # Emotion Detection

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/emotion.png"):
            st.image("assets/emotion.png")

    with col2:

        st.subheader("Emotion Detection System")

        st.write("""
        NLP-based emotion detection system using
        TF-IDF Vectorization and Logistic Regression.
        Accuracy: 86%
        """)

        st.link_button(
            "🔗 Live Link",
            "https://ajaykumar-02-emotionsense-ai-app-i2arj8.streamlit.app/"
        )
        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/EmotionSense-AI"
        )

    st.divider()

    # Movie Recommendation

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/movie.png"):
            st.image("assets/movie.png")

    with col2:

        st.subheader("Movie Recommendation System")

        st.write("""
        Content-based recommendation system
        using TF-IDF and Cosine Similarity.
        """)

      
        st.link_button(
            "🔗 Video Demo ",
            "https://www.linkedin.com/posts/ajay-kumar-63a3b7326_machinelearning-nlp-python-ugcPost-7471138958580596736-CFyz/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFJI8c4BMD6QxMXLZAivbxdHOFLdWxEtOqU"
        )
        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/movie-recommendation-system"
        )


    st.divider()

    # House Rent Prediction

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/rent.png"):
            st.image("assets/rent.png")

    with col2:

        st.subheader("House Rent Prediction")

        st.write("""
        House rent prediction system using
        XGBoost Regression and Streamlit.
        """)

        st.link_button(
            "🔗 Live Link",
            "https://houserentprediction-eoosjjs93u9uprrjysnhjt.streamlit.app/"
        )
        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/HouseRentPrediction"
        )
         

        st.divider()
            # Insurance Cost Predictor

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/insurance.png"):
            st.image("assets/insurance.png")

    with col2:

        st.subheader("Insurance Cost Predictor")

        st.write("""
        Insurance premium prediction system using
        Machine Learning and Streamlit.
        """)

        st.link_button(
            "🔗 Live Link",
            "https://insurance-cost-predictor-sd4qkvxsdc76icpsqcxp7b.streamlit.app/"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/insurance-cost-predictor"
        )

    st.divider()
        # Heart Disease Prediction System

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/heart.png"):
            st.image("assets/heart.png")

    with col2:

        st.subheader("Heart Disease Prediction System")

        st.write("""
        Heart disease prediction system using
        Machine Learning and Streamlit.
        """)

        st.link_button(
            "🔗 Live Link",
            "https://ajaykumar-02-p-2-app-vigks3.streamlit.app/"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/Heart_Disease_Prediction_System"
        )

    st.divider()
        # Robo

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/robospeaker.png"):
            st.image("assets/robospeaker.png")

    with col2:

        st.subheader("RoboSpeaker")

        st.write("""
         Multilingual Text-to-Speech converter
        using Python, gTTS and Streamlit.
        """)

        st.link_button(
            "🔗 Live Link",
            "https://robospeaker-ajay.streamlit.app/"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/RoboSpeaker"
        )

    st.divider()
        # Jarvis

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/jarvis.png"):
            st.image("assets/jarvis.png")

    with col2:

        st.subheader("Jarvis AI Assistant")

        st.write("""
        Voice-controlled AI assistant built using
        Python, Speech Recognition, Pyttsx3,
        PyWhatKit 
        """)

        st.link_button(
            "🔗 Video Demo",
            "https://drive.google.com/file/d/1mY-sR-r-zraAmedkvUTYCBwTv03SiolQ/view?usp=sharing"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/Jarvis-AI-Assistant"
        )

    st.divider()
        # Smart Image Optimizer

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/resizer.png"):
            st.image("assets/resizer.png")

    with col2:

        st.subheader("Smart Image Optimizer")

        st.write("""
        Resize and optimize images with custom
        dimensions and quality settings using
        OpenCV and Streamlit. 
        """)

        st.link_button(
            "🔗 Live Link ",
            "https://imageresizer-jdttnslk66jpkaahxmjtmb.streamlit.app/"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/ImageResizer"
        )

    st.divider()
        # Snake Water Gun Game

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/snakewatergun.png"):
            st.image("assets/snakewatergun.png")

    with col2:

        st.subheader("Snake Water Gun Game")

        st.write("""
        Interactive Snake Water Gun game built
        using Python and Streamlit with score
        tracking and game logic. 
        """)

        st.link_button(
            "🔗 Live Link ",
            "https://snakewatergun-ajay.streamlit.app/"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/SnakeWaterGun"
        )

    st.divider()
        #Guess The Number Game

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/guess.png"):
            st.image("assets/guess.png")

    with col2:

        st.subheader("Guess The Number Game")

        st.write("""
         Number guessing game with difficulty
        levels, high score tracking and
        interactive Streamlit UI. 
        """)

        st.link_button(
            "🔗 Live Link ",
            "https://numberguesser-ajay.streamlit.app/"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/NumberGuesser"
        )

    st.divider()
        # Calculator Using tkinter

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/Calculator.png"):
            st.image("assets/Calculator.png")

    with col2:

        st.subheader("Calculator Using tkinter")

        st.write("""
        Graphical User Interface (GUI) calculator
        built using Python's Tkinter library. 
        It performs arithmetic operations. 
        """)

        st.link_button(
            "🔗 Video Demo  ",
            "https://drive.google.com/file/d/1UA8gkoPLqmBg8tbWXdlWLGunYK0CfOwY/view?usp=sharing"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/Pyhton-Projects/blob/main/Calculator.py"
        )

    st.divider()
        #Travel India Website

    col1, col2 = st.columns([1, 2])

    with col1:

        if os.path.exists("assets/travel.png"):
            st.image("assets/travel.png")

    with col2:

        st.subheader("Travel India Website")

        st.write("""
        A responsive website for exploring travel 
        destinations and tour packages across India. 
        """)

        st.link_button(
            "🔗 Video Demo  ",
            "https://drive.google.com/file/d/1-4EGcbnxKwiW2LgHW_WSkpV84kEDAaTA/view?usp=sharing"
        )

        st.link_button(
            "💻 GitHub",
            "https://github.com/Ajaykumar-02/Travel-India-Website"
        )

    st.divider()
 


# ==================================
# CONTACT
# ==================================

elif selected == "Contact":

    st.title("📞 Contact")

    st.write("📧 kumarajay3023ak3@gmail.com")
    st.write("💻 GitHub: https://github.com/Ajaykumar-02")
    st.write("💼 LinkedIn: https://www.linkedin.com/in/ajay-kumar-63a3b7326/")

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">

    <h4>👨‍💻 Ajay Kumar</h4>

    <p>
    <a href="https://github.com/Ajaykumar-02" target="_blank">GitHub</a>
    &nbsp; | &nbsp;
    <a href="https://www.linkedin.com/in/ajay-kumar-63a3b7326/" target="_blank">LinkedIn</a>
    &nbsp; | &nbsp;
    <a href="mailto:kumarajay3023ak3@gmail.com">Email</a>
    </p>

    <p style="font-size:12px;">
    Made with ❤️ using Streamlit
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

