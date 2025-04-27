import streamlit as st

# Logo
image = "resources/logo.png"
st.logo(image, size='large')

with st.container():
    """ # 📚 Attend2Achieve 🎯
    A smart analytical tool to correlate subject-wise attendance with academic performance, revealing hidden trends and guiding actionable improvements.

    ## 🔍 Overview   
    Attend2Achieve analyzes the relationship between subject-wise attendance and theory/practical marks. It uses statistical methods like skewness, IQR, standard deviation, and mean-median analysis to explain performance patterns and suggest data-driven improvements. Visual dashboards make insights clear and actionable for institutions.

    ## ✨ Key Features
    ✔ Subject-wise Correlation Analysis: Attendance vs. marks (theory + practical).   
    ✔ Statistical Insight: Uses skewness, standard deviation, IQR, and mean-median gaps.   
    ✔ Diagnostic Reports: Recommends improvements through per-subject analysis.   
    ✔ Visualizations: Includes histograms, correlation heatmaps, and distribution plots.   
    ✔ Academic Insight Dashboard: Summarizes performance trends across all subjects.   
    ✔ Tech Stack: Python, Pandas, NumPy, Pyplot, Streamlit.   
    
    
    ## 📌 Explore the Tool
    """
    # View Research Paper Button
with st.container(border=True):
    "# Test Analysis Feature"
    "###### This page allows you to test the project and generate an analysis of student performance without uploading a file. If you prefer to test the app without providing your own data, you can use pre-existing analysis. To generate a synthetic analysis, simply click the button below."
    # View Synthetic Analysis Button
    st.page_link("page_files/View_Synthetic_Analysis.py", label="Generate Synthetic Analysis", icon="🧪")

with st.container(border=True):
    "# Generate Analysis "
    "###### Enter the details of your institution and get a detailed analysis of student performance."
    # Generate Analysis Button
    st.page_link("page_files/Generate_Analysis.py", label="Generate Analysis", icon="📊")  

with st.container(border=True):
    "# Want to provide feedback ?"
    "###### We would love to hear from you. Please provide your feedback."
    # Feedback Button
    st.page_link("page_files/Feedback.py", label="Feedback", icon="💭")    

with st.container(border=True):
    "# Want to know more ?"
    "###### It seems like you want to know more about this project."  
    # View GitHub Repository Button  
    st.page_link("page_files/Credits.py", label="Credits", icon="📇")

with st.container(border=True):
    "# 🌏 In an Alternate Universe..."
    # Page Title
    "#### 📊 BeyondTheMarks - Exposing Bias, Elevating Education"
    "##### 🔍 A Different Lens on Bias and Teaching Impact"
    st.write(
        "Similar to *Attend2Achieve*, *BeyondTheMarks* dives into academic performance but with a sharper focus on *bias detection and teaching effectiveness.* "
        "By leveraging *statistical methods and machine learning*, it evaluates whether *gender or religion* influence grades unfairly, assesses *professor effectiveness using ANOVA*, "
        "and uncovers hidden *subject correlations* to predict student success. This isn’t just another analytics dashboard—it’s a step towards a *fairer, more accountable education system.*"
    )
    
    # 🔗 Try It Now
    st.page_link("https://beyondthemarks.streamlit.app", label="Explore BeyondTheMarks", icon="🚀", use_container_width=True)
    