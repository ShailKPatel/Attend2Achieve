import streamlit as st

# Logo
image = "resources/logo.png"
st.logo(image, size='large')

"# 🎖️ Credits "

with st.container(border=True):
    "## Made By : "

    "### **Panchal Dev**"
    st.link_button("LinkedIn", "https://www.linkedin.com/in/dev-panchal-connect/", icon="🔗", use_container_width=True)
    st.link_button("GitHub", "https://github.com/DevPanchal2005", icon="🔗", use_container_width=True)

with st.container(border=True):
    "## GitHub Repository :"
    st.link_button("Attendance For Impact", "https://github.com/DevPanchal2005/Attendance-For-Impact", icon="🔗")

with st.container(border=True):
    """
    ## 🛠️ Technologies Used  
    - 📌 **Programming & Libraries :** Python 🐍, Streamlit, NumPy 🔢, Pandas 📊, Matplotlib 📈, Seaborn 🎨, Scikit-Learn 🤖, SciPy 🔬, io, PIL 🖼️  
    - 💻 **IDE & Development :** VS Code 📝, Jupyter Notebook 📓  
    - 🌍 **Version Control :** GitHub 🗄️ (Project Repository)  
    - 🤖 **Documentation Assistance :** ChatGPT 📝 (Generating Documentation)  
    """
