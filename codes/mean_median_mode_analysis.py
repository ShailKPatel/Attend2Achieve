import streamlit as st

def analyze_mean_median(mean, median, institute_type):
    diff = mean - median

    if institute_type == "School":
        if diff > 0:
            st.success("Right (Positive) Skew - 🚨 Attendance Issues")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A small group of students has very low attendance, pulling the average down.")
                st.write("Suggests disengagement, lack of motivation, or external constraints affecting attendance.")
                with st.popover("Advice", icon="✅"):
                    st.write("Identify students with low attendance and provide targeted support.")
                    st.write("Investigate reasons for frequent absences (family issues, travel constraints, lack of interest, etc.).")
                    st.write("Implement student engagement initiatives to improve attendance.")

        elif diff < 0:
            st.success("Left (Negative) Skew - ✅ Strict Attendance Patterns")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A few students have exceptionally high attendance, pulling the average up.")
                st.write("Indicates possible strict attendance enforcement or over-reporting.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure attendance reflects genuine participation rather than compulsion.")
                    st.write("Encourage active engagement rather than just physical presence.")
                    st.write("Balance policies to prevent undue pressure on students.")

        else:
            st.success("Balanced Attendance - ✅ Evenly Distributed Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Attendance distribution is fairly even, with no extreme variations.")
                st.write("Suggests a well-managed attendance policy with natural fluctuations.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current attendance policies and engagement strategies.")
                    st.write("Monitor for any shifts in patterns over time.")
    
    if institute_type == "College":
    # Skewness Interpretation for College Students
        if diff > 0:
            st.success("Right (Positive) Skew - 🚨 Attendance Gaps")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A subset of students has very low attendance, lowering the average.")
                st.write("Indicates possible academic disengagement, scheduling conflicts, or lack of interest.")
                with st.popover("Advice", icon="✅"):
                    st.write("Identify students with irregular attendance and assess reasons.")
                    st.write("Offer flexible attendance solutions such as online resources or recorded lectures.")
                    st.write("Encourage attendance through interactive learning techniques.")

        elif diff < 0:
            st.success("Left (Negative) Skew - ✅ High Commitment")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A few students have extremely high attendance, raising the average.")
                st.write("Suggests high engagement but could also indicate grade-conscious behavior.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure attendance is driven by learning, not just compliance.")
                    st.write("Encourage active class participation beyond mere presence.")
                    st.write("Consider incentivizing knowledge application rather than attendance alone.")

        else:
            st.success("Balanced Attendance - ✅ Well-Distributed Engagement")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Attendance is evenly distributed, reflecting healthy student participation.")
                st.write("Suggests that policies are effective and class engagement is consistent.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current attendance monitoring strategies.")
                    st.write("Encourage continuous engagement through discussions and activities.")

def analyze_mean_mode(mean, mode, institute_type):
    diff = mean - mode

    if institute_type == "School":
    # Mean - Mode Interpretation for School Students
        if diff > 0:
            st.success("🚨 Some Students Have Much Lower Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students attend regularly, but a few have significantly lower attendance.")
                st.write("The mean is pulled down by students who frequently miss classes.")
                with st.popover("✅ Advice"):
                    st.write("Identify frequently absent students and understand their challenges (health, family issues, lack of motivation).")
                    st.write("Implement early intervention programs like parental engagement, attendance incentives, and mentoring.")

        elif diff < 0:
            st.success("✅ Most Students Attend Regularly, but Some Are Extremely Absent")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A majority of students have high attendance, but a small group is nearly absent.")
                st.write("Might indicate students attending due to external pressure (strict school policies, fear of penalties).")
                with st.popover("✅ Advice"):
                    st.write("Ensure students attend classes due to engagement, not compulsion.")
                    st.write("Investigate whether strict rules or harsh penalties force attendance rather than encourage learning.")
                    st.write("Promote student engagement through interactive teaching methods.")

        else:
            st.success("✅ Attendance Distribution is Stable")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Attendance levels are uniform, and most students fall within the expected range.")
                st.write("No extreme absenteeism or forced attendance patterns.")
                with st.popover("✅ Advice"):
                    st.write("Maintain current attendance policies and engagement strategies.")
                    st.write("Continue monitoring trends to prevent future attendance concerns.")

    if institute_type == "College":
        # Mean - Mode Interpretation for College Students
        if diff > 0:
            st.success("🚨 A Group of Students Has Very Low Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students have moderate to high attendance, but a subset is frequently absent.")
                st.write("Could indicate disengagement due to poor class relevance, external responsibilities, or lack of motivation.")
                with st.popover("✅ Advice"):
                    st.write("Conduct surveys to understand why students are missing classes.")
                    st.write("Introduce flexible attendance policies, recorded lectures, or hybrid learning options.")
                    st.write("Engage students through real-world applications and interactive sessions.")

        elif diff < 0:
            st.success("✅ Most Students Are Highly Regular, but Some Are Chronically Absent")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A majority of students maintain high attendance, while a small group is absent nearly all the time.")
                st.write("This could indicate students attending for grades rather than learning.")
                with st.popover("✅ Advice"):
                    st.write("Ensure attendance policies emphasize learning engagement over compulsion.")
                    st.write("Provide alternative participation methods for students who struggle with in-person attendance.")

        else:
            st.success("✅ Attendance Distribution is Balanced")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Attendance patterns are consistent, with no major outliers.")
                st.write("Indicates a stable classroom environment with proper engagement and attendance policies.")
                with st.popover("✅ Advice"):
                    st.write("Continue maintaining student engagement and attendance strategies.")
                    st.write("Use periodic attendance reviews to sustain long-term consistency.")

