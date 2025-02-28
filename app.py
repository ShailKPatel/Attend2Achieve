import streamlit as st

home = st.Page("page_files/Home.py", icon='🏠')

generate_analysis = st.Page("page_files/Generate_Analysis.py", icon='📊')

feedback = st.Page("page_files/Feedback.py", icon='💭')

credits = st.Page("page_files/Credits.py", icon='📇')


pg = st.navigation({
    "Home": [home],
    "Analysis": [generate_analysis],
    "Miscellaneous ": [feedback, credits]
})

pg.run()
