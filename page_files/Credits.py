import streamlit as st

# Logo
image = "resources/logo.png"
st.logo(image, size='large')

"# 🎖️ Credits "

with st.container(border=True):
    "## Made By : "

    "### **Panchal Dev**"
    st.link_button("Connect on LinkedIn", "https://www.linkedin.com/in/dev-panchal-connect/", icon="🔗", use_container_width=True)
    st.link_button("Explore His GitHub", "https://github.com/DevPanchal2005", icon="🐙", use_container_width=True)

    "### **Shail K Patel**"
    st.link_button("Stalk Him on LinkedIn", "https://www.linkedin.com/in/shail-k-patel/", icon="🔗", use_container_width=True)
    st.link_button("Investigate His GitHub", "https://github.com/ShailKPatel", icon="🐙", use_container_width=True)

with st.container(border=True):
    "## GitHub Repository :"
    st.link_button("Attendance For Impact", "https://github.com/DevPanchal2005/Attendance-For-Impact", icon="🔗")


with st.container(border=True):
    """
    ## 🛠️ Technologies Used  
    - 📌 **Programming & Libraries :** Python 🐍, Streamlit, NumPy 🔢, Pandas 📊, Plotly 📈, Scikit-Learn 🤖, SciPy 🔬, PIL 🖼️  
    - 💻 **IDE & Development :** VS Code 📝, Jupyter Notebook 📓  
    - 🌍 **Version Control :** GitHub 🗄️ (Project Repository)  
    - 🤖 **Documentation Assistance :** ChatGPT 📝 (Generating Documentation)  
    """
