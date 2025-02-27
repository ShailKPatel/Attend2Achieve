import streamlit as st

def analyze_skewness_attendance(skewness, institute_type):
    if institute_type == "School":
        if skewness <= -1.0:
            st.success("Highly Negative Skew (≤ -1.0) - 🚨 Almost All Students Have High Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Nearly all students attend regularly, with very few absences.")
                st.write("Could indicate strict attendance policies, parental pressure, or school-enforced compliance.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Students may be attending due to rules rather than genuine interest.")
                    st.write("Long-term: Can lead to passive learning—students are physically present but mentally disengaged.")
                with st.popover("Actions for Schools", icon="✅"):
                    st.write("Ensure engagement: Make sure students are not just present but actively learning.")
                    st.write("Check for artificial attendance inflation: Avoid excessive enforcement that leads to forced compliance rather than interest.")
        
        elif -1.0 < skewness <= -0.5:
            st.success("Moderately Negative Skew (-1.0 to -0.5) - ✅ Mostly Good Attendance with Some Irregularities")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Attendance is generally strong, with a small portion of students having irregular attendance.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Most students benefit from regular attendance.")
                    st.write("Long-term: Some students may start falling behind due to occasional absences.")
                with st.popover("Actions for Schools", icon="✅"):
                    st.write("Identify students with frequent absences and provide early intervention (mentorship, parental communication).")
                    st.write("Ensure learning remains engaging so that students attend voluntarily, not just because of rules.")
        
        elif -0.5 < skewness <= 0.5:
            st.success("Near Zero Skew (-0.5 to 0.5) - 🎯 Balanced Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Ideal distribution—students attend regularly without extreme highs or lows.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term & Long-term: Ensures steady learning, peer collaboration, and consistent academic performance.")
                with st.popover("Actions for Schools", icon="✅"):
                    st.write("Maintain current attendance policies while keeping students engaged.")
                    st.write("Keep track of trends to prevent future dips in attendance.")
        
        elif 0.5 < skewness <= 1.0:
            st.success("Moderately Positive Skew (0.5 to 1.0) - ⚠ Some Students Have Low Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A small but noticeable number of students have low attendance.")
                st.write("Reasons could include lack of motivation, family problems, or disengagement.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Some students fall behind in lessons.")
                    st.write("Long-term: The attendance gap could widen, leading to increased dropout risks.")
                with st.popover("Actions for Schools", icon="✅"):
                    st.write("Identify at-risk students and provide personalized support.")
                    st.write("Make learning more interactive to increase voluntary attendance.")
                    st.write("Consider flexible catch-up sessions for those with legitimate reasons for missing school.")
        
        elif skewness > 1.0:
            st.success("Highly Positive Skew (≥ 1.0) - 🚨 Most Students Have Very Low Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A severe attendance crisis—most students attend rarely.")
                st.write("Causes may include poor teaching quality, lack of parental involvement, transportation issues, or disengagement.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Immediate drop in academic performance.")
                    st.write("Long-term: Increased risk of dropouts, lower grades, and weaker future career opportunities.")
                with st.popover("Actions for Schools", icon="✅"):
                    st.write("Conduct student surveys to identify the root cause.")
                    st.write("Improve teaching methods to make learning more engaging and interactive.")
                    st.write("Work on attendance improvement programs (incentives, hybrid learning, better student-teacher engagement).")
    
    if institute_type == "College":
        if skewness <= -1.0:
            st.success("Highly Negative Skew (≤ -1.0) - 🚨 Nearly All Students Have High Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students attend regularly, possibly due to mandatory attendance policies.")
                st.write("Could indicate inflated attendance records (proxies, forced compliance).")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Ensures students attend regularly, but doesn’t guarantee engagement.")
                    st.write("Long-term: If students attend just to fulfill requirements, learning quality may suffer.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Encourage active participation rather than just attendance.")
                    st.write("Consider flexibility in attendance rules to focus on learning quality.")
        
        elif -1.0 < skewness <= -0.5:
            st.success("Moderately Negative Skew (-1.0 to -0.5) - ✅ Mostly Good Attendance with Some Absentees")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students attend regularly, but a small group may be absent frequently.")
                st.write("Could indicate strategic skipping—students attend important lectures but skip others.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Small group might miss key content.")
                    st.write("Long-term: Could lead to lower performance in assessments.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Identify why students skip certain lectures—is it lack of interest, scheduling conflicts, or teaching quality?")
                    st.write("Improve course structure to make all classes feel valuable.")
        
        elif -0.5 < skewness <= 0.5:
            st.success("Near Zero Skew (-0.5 to 0.5) - 🎯 Balanced Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Ideal case—students attend regularly without excessive enforcement.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term & Long-term: Ensures consistent academic engagement and performance.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Maintain flexibility in attendance policies while ensuring course engagement remains strong.")
                    st.write("Avoid unnecessary attendance pressure—allow students some autonomy.")
        
        elif 0.5 < skewness <= 1.0:
            st.success("Moderately Positive Skew (0.5 to 1.0) - ⚠ Noticeable Group of Students Skipping Classes")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A visible portion of students have low attendance.")
                st.write("Could indicate disinterest in course material, ineffective teaching, or rigid attendance policies.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Reduced participation in discussions and practical learning.")
                    st.write("Long-term: Could lower exam performance and overall grades.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Identify which classes are skipped the most and why.")
                    st.write("Improve teaching engagement strategies—less lecture, more discussion-based learning.")
        
        elif skewness > 1.0:
            st.success("Highly Positive Skew (≥ 1.0) - 🚨 Most Students Have Very Low Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Majority of students rarely attend, possibly due to:")
                st.write("- Rigid schedules")
                st.write("- Unengaging classes")
                st.write("- Overemphasis on self-study or online materials")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Lower understanding of practical coursework.")
                    st.write("Long-term: Higher dropout rates and weaker employability skills.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Conduct student feedback surveys to determine why attendance is low.")
                    st.write("Consider hybrid models (online + offline learning).")
                    st.write("Provide attendance incentives (interactive participation, graded in-class exercises).")
def analyze_skewness_theory(skewness,institute_type):
    if institute_type == "School":
        if skewness <= -1.0:
            st.success("Highly Negative Skew (≤ -1.0) - 🚨 Grade Inflation Risk")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students scored very high, with very few low scorers.")
                st.write("May indicate an easy exam or grade inflation.")
                st.write("Students may not be challenged enough to demonstrate higher-level understanding.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure exams cover all difficulty levels (easy, medium, hard).")
                    st.write("If skewness is extreme, consider adjusting grading rubrics.")
                    st.write("Check if high marks translate into actual knowledge (compare with practical performance).")
        elif skewness > -1.0 and skewness <= -0.5:
            st.success("Moderately Negative Skew (-1.0 to -0.5) - ✅ Slightly Easy Exam")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students did well, but some struggled.")
                st.write("Indicates good teaching quality, but weaker students may need support.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain balanced exam difficulty.")
                    st.write("Identify students who scored poorly and offer targeted interventions.")
                    st.write("Encourage challenging questions to differentiate top students.")
        elif skewness > -0.5 and skewness <= 0.5:
            st.success("Near Zero Skew (-0.5 to 0.5) - 🎯 Ideal (Balanced Marks Distribution)")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Marks are evenly spread, with no extreme highs or lows.")
                st.write("Indicates a well-designed exam that accurately assesses student ability.")
                with st.popover("Advice", icon="✅"):
                    st.write("No immediate changes needed—exam structure is working well.")
                    st.write("Continue monitoring long-term trends to maintain fairness.")
        elif skewness > 0.5 and skewness <= 1.0:
            st.success("Moderately Positive Skew (0.5 to 1.0) - ⚠ Exam Too Difficult for Most Students")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A few students scored well, but most struggled.")
                st.write("Indicates the exam was too difficult or not well-aligned with the teaching material.")
                st.write("Possible causes:")
                st.write("Unfamiliar question types.")
                st.write("Poor teaching coverage of key concepts.")
                st.write("Higher-order thinking questions without sufficient preparation.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure exams match curriculum difficulty expectations.")
                    st.write("Analyze common mistakes—were questions too tricky?")
                    st.write("Provide additional practice materials for weaker students.")
        elif skewness >= 1.0:
            st.success("Highly Positive Skew (≥ 1.0) - 🚨 Major Performance Gap")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students failed or scored very low, with only a few high scorers.")
                st.write("Indicates serious learning issues, possibly due to:")
                st.write("Overly difficult exams.")
                st.write("Poor teaching methods.")
                st.write("Lack of student motivation.")
                with st.popover("Advice", icon="✅"):
                    st.write("Conduct student feedback to understand difficulties.")
                    st.write("Offer remedial classes for struggling students.")
                    st.write("Adjust grading scales or question difficulty to be more balanced.")

    if institute_type == "College":
        if skewness <= -1.0:
            st.success("Highly Negative Skew (≤ -1.0) - 🚨 Most Students Scored High")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students received high scores, with very few performing poorly.")
                st.write("Could indicate an easy exam, lenient grading, or low academic rigor.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: High scores boost confidence.")
                    st.write("Long-term: Students may lack real problem-solving skills if assessments are too easy.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Increase difficulty level to test critical thinking and application-based skills.")
                    st.write("Ensure grading is consistent with industry expectations.")
        
        elif -1.0 < skewness <= -0.5:
            st.success("Moderately Negative Skew (-1.0 to -0.5) - ✅ Mostly Good Scores with Some Low Performers")
            with st.expander("What's Happening?", icon="📌"):
                st.write("The exam was slightly easier, but not unrealistic.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Encourages learning but does not push top students enough.")
                    st.write("Long-term: May not prepare students well for competitive exams or job assessments.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Offer advanced-level assignments to challenge stronger students.")
                    st.write("Support low scorers with personalized academic counseling.")
        
        elif -0.5 < skewness <= 0.5:
            st.success("Near Zero Skew (-0.5 to 0.5) - 🎯 Balanced Scores")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A fair distribution—students are graded accurately based on skill level.")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term & Long-term: Encourages a merit-based learning environment.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Maintain current exam structure and assessment balance.")
                    st.write("Regularly review exam quality to keep up with industry standards.")
        
        elif 0.5 < skewness <= 1.0:
            st.success("Moderately Positive Skew (0.5 to 1.0) - ⚠ Majority Struggled")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students scored well, but the majority had difficulty.")
                st.write("Could be due to:")
                st.write("- Challenging questions")
                st.write("- Unclear syllabus coverage")
                st.write("- Gaps in student preparation")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Poor performers lose confidence.")
                    st.write("Long-term: Leads to higher failure rates and repeat courses.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Analyze which questions students found hardest and why.")
                    st.write("Align teaching materials with exam expectations.")
                    st.write("Offer academic mentoring and revision workshops.")
        
        elif skewness > 1.0:
            st.success("Highly Positive Skew (≥ 1.0) - 🚨 Most Students Performed Poorly")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A large number of students failed, with only a few doing well.")
                st.write("Could indicate:")
                st.write("- Overly tough exams")
                st.write("- Lack of clear guidance")
                st.write("- Poor lecture effectiveness")
                with st.popover("Impact on Students", icon="🔹"):
                    st.write("Short-term: Academic stress and mental health issues.")
                    st.write("Long-term: Dropout risk and career setbacks.")
                with st.popover("Actions for Colleges", icon="✅"):
                    st.write("Collect student feedback on exam difficulty and clarity.")
                    st.write("Improve faculty training and lecture quality.")
                    st.write("Offer graded assignments and practice tests before major exams.")

def analyze_skewness_practical(skewness, institute_type):
    if institute_type == "School":
        if skewness <= -1.0:
            st.success("Highly Negative Skew (≤ -1.0) - 🚨 Overly Easy or Lenient Grading")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Practical assessments might be too simple, leading to inflated scores.")
                with st.popover("Advice", icon="✅"):
                    st.write("Introduce slightly more challenging experiments to assess real understanding.")
        
        elif -1.0 < skewness <= -0.5:
            st.success("Moderately Negative Skew (-1.0 to -0.5) - ✅ Mostly Balanced, Slightly Easy")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students do well, but weaker students struggle slightly.")
                with st.popover("Advice", icon="✅"):
                    st.write("Keep current methods but add reinforcement activities for struggling students.")
        
        elif -0.5 < skewness <= 0.5:
            st.success("Near Zero Skew (-0.5 to 0.5) - 🎯 Ideal Practical Marks Distribution")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Balanced assessment of students’ practical skills.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current practical structure and monitoring.")
        
        elif 0.5 < skewness <= 1.0:
            st.success("Moderately Positive Skew (0.5 to 1.0) - ⚠ Students Struggling with Practical Skills")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A few students excel, but many face difficulties in applying concepts practically.")
                with st.popover("Advice", icon="✅"):
                    st.write("Provide extra hands-on practice sessions and better guidance during experiments.")
        
        elif skewness > 1.0:
            st.success("Highly Positive Skew (≥ 1.0) - 🚨 Major Practical Skill Deficiency")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students score poorly, indicating poor lab infrastructure or lack of exposure.")
                with st.popover("Advice", icon="✅"):
                    st.write("Increase lab practice sessions and improve teacher guidance during practical work.")

    if institute_type == "College": 

        if skewness <= -1.0:
            st.success("Highly Negative Skew (≤ -1.0) - 🚨 Overly Easy or Lenient Grading")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students scored very high, with very few low marks.")
                st.write("Suggests that:")
                st.write("Practical assessments are too easy.")
                st.write("Lenient grading or excessive instructor guidance.")
                st.write("Limited differentiation between top and weak students.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure practical assessments challenge students effectively.")
                    st.write("Introduce rubrics that measure different skill levels.")
                    st.write("Verify if practical work is being done independently.")
        elif skewness > -1.0 and skewness <= -0.5:
            st.success("Moderately Negative Skew (-1.0 to -0.5) - ✅ Mostly Balanced, Slightly Easy")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students did well, but a few struggled.")
                st.write("Indicates good hands-on training, but some students may need extra support.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current evaluation methods, but provide extra practice for weaker students.")
                    st.write("Ensure practical assignments test real-world application rather than rote execution.")
        elif skewness > -0.5 and skewness <= 0.5:
            st.success("Near Zero Skew (-0.5 to 0.5) - 🎯 Ideal (Balanced Practical Marks Distribution)")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Marks are evenly distributed, meaning practical exams are well-structured and fair.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain consistent practical training methods.")
                    st.write("Monitor trends over time to ensure assessments remain valid and unbiased.")
        elif skewness > 0.5 and skewness <= 1.0:
            st.success("Moderately Positive Skew (0.5 to 1.0) - ⚠ Students Struggling with Practical Skills")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A few students did well, but most struggled.")
                st.write("Suggests that:")
                st.write("Practical training is insufficient.")
                st.write("Students may lack experience with real-world applications.")
                st.write("The evaluation may be too strict.")
                with st.popover("Advice", icon="✅"):
                    st.write("Provide more hands-on practice sessions.")
                    st.write("Identify specific practical skill gaps and offer remediation.")
                    st.write("Ensure practical exams align with what is taught in labs.")
        elif skewness >= 1.0:
            st.success("Highly Positive Skew (≥ 1.0) - 🚨 Major Practical Skill Deficiency")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students scored poorly, with only a few high performers.")
                st.write("Indicates severe issues, such as:")
                st.write("Poor lab facilities or lack of practice opportunities.")
                st.write("Unclear grading criteria.")
                st.write("Students being unprepared for hands-on work.")
                with st.popover("Advice", icon="✅"):
                    st.write("Conduct additional practical sessions for weak students.")
                    st.write("Improve availability of lab equipment and guidance.")
                    st.write("Ensure grading is transparent and well-structured.")
