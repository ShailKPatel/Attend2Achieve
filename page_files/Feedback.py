import streamlit as st
import collections
import os

FEEDBACK_FILE = "feedback.txt"
MAX_FEEDBACKS = 5

def load_feedbacks():
    """Load feedbacks from the file into a deque."""
    feedbacks = collections.deque(maxlen=MAX_FEEDBACKS)
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                feedbacks.append(line.strip())
    return feedbacks

def save_feedbacks(feedbacks):
    """Save the feedbacks to the file."""
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        for feedback in feedbacks:
            f.write(feedback.replace("\n", " ") + "\n")

st.title("Feedback Collector")
feedbacks = load_feedbacks()

user_feedback = st.text_area("Enter your feedback:",max_chars=50).replace("\n", " ")
if st.button("Submit Feedback"):
    if user_feedback.strip():
        feedbacks.append(user_feedback.strip())
        save_feedbacks(feedbacks)
    else:
        st.warning("Please enter a valid feedback.")

st.header("Recent Feedbacks")
if feedbacks:
    num_feedbacks = len(feedbacks)
    for i in range(0, num_feedbacks, 3):
        cols = st.columns(min(3, num_feedbacks - i),border=True)
        for j in range(min(3, num_feedbacks - i)):
            with cols[j]:
                st.write(feedbacks[i + j])
else:
    st.write("No feedback yet.")
