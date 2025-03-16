import streamlit as st

# Logo
image = "resources/logo.png"
st.logo(image, size='large')

# Image
st.image(image, use_container_width=True)

with st.container(border=True):
    """ # What is Attendance for Impact ? 
    This is an app designed to help institutions refine their policies and gain deeper insights into academic performance, revealing hidden patterns through thoughtful analysis and guidance."""
    # View Research Paper Button

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
        "Similar to *Attendance for Impact*, *BeyondTheMarks* dives into academic performance but with a sharper focus on *bias detection and teaching effectiveness.* "
        "By leveraging *statistical methods and machine learning*, it evaluates whether *gender or religion* influence grades unfairly, assesses *professor effectiveness using ANOVA*, "
        "and uncovers hidden *subject correlations* to predict student success. This isn’t just another analytics dashboard—it’s a step towards a *fairer, more accountable education system.*"
    )
    
    # 🔗 Try It Now
    st.page_link("https://beyondthemarks.streamlit.app", label="Explore BeyondTheMarks", icon="🚀", use_container_width=True)
    