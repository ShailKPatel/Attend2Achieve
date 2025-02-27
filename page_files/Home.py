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
    "# Guide to use this app "
    "###### Learn how to use this app and get the most out of it."
    # User Guide Button
    

with st.container(border=True):
    "# Want to know more ?"
    "###### It seems like you want to know more about this project."  
    # View GitHub Repository Button  
    st.page_link("page_files/Credits.py", label="Credits", icon="📇")
