import streamlit as st

def analyze_standard_deviation_attendance(sd, institute_type):
    if institute_type == "College":
        if sd <= 10:
            st.success("Very Low Spread (≤ 10) - 🚨 Uniform Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students have very similar attendance—either everyone attends regularly, or almost no one does.")
                st.write("This suggests very strict attendance policies or strong external factors influencing attendance uniformly.")
                with st.popover("Advice", icon="✅"):
                    st.write("If attendance is universally high, ensure students are engaged and not just attending for the sake of rules.")
                    st.write("If attendance is universally low, investigate possible systemic issues (poor teaching, class scheduling problems, etc.).")
        elif sd > 10 and sd <= 20:
            st.success("Moderate Spread (10 to 20) - ✅ Healthy Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students occasionally miss classes, but overall, attendance patterns are stable.")
                st.write("This suggests that attendance is neither forced nor ignored, meaning policies are reasonable.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current attendance policies.")
                    st.write("Keep an eye on individual students with consistently low attendance and provide early intervention if needed.")
        elif sd > 20 and sd <= 30:
            st.success("High Spread (20 to 30) - ⚠ Attendance Gaps Emerging")
            with st.expander("What's Happening?", icon="📌"):
                st.write("A significant difference between regular attendees and frequently absent students.")
                st.write("Some students may struggle with attendance due to personal or external challenges.")
                with st.popover("Advice", icon="✅"):
                    st.write("Identify students with very low attendance and understand their reasons.")
                    st.write("Consider flexible learning options (recorded lectures, hybrid attendance policies, etc.).")
                    st.write("Encourage attendance through engagement initiatives like interactive sessions or participation-based rewards.")
        elif sd > 30:
            st.success("Very High Spread (≥ 30) - 🚨 Major Attendance Issue")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students attend nearly all classes, while others hardly show up.")
                st.write("Suggests deeply rooted issues—either with class structure, student motivation, or external constraints (transportation, finances, family responsibilities, etc.).")
                with st.popover("Advice", icon="✅"):
                    st.write("Conduct student surveys to understand why attendance varies so much.")
                    st.write("Implement targeted interventions for students with very low attendance.")
                    st.write("Consider attendance incentives, flexible policies, or engagement-focused learning techniques.")
    
    if institute_type == "School":
        if sd <= 10:
            st.success("Very Low Spread (≤ 10) - 🚨 Uniform Attendance")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Attendance is highly consistent—either everyone attends, or hardly anyone does.")
                st.write("Could result from rigid attendance enforcement or a disengaged student body.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure students are attending due to engagement rather than compulsion.")
                    st.write("If attendance is very low, investigate systemic issues (bullying, teacher quality, school environment).")

        elif 10 < sd <= 20:
            st.success("Moderate Spread (10 to 20) - ✅ Healthy Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students occasionally miss school, but attendance remains stable.")
                st.write("Indicates a well-balanced attendance culture.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current attendance policies.")
                    st.write("Identify students with declining attendance early and intervene.")

        elif 20 < sd <= 30:
            st.success("High Spread (20 to 30) - ⚠ Attendance Gaps Emerging")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students are always present, while others frequently miss school.")
                st.write("Likely caused by lack of interest, school climate, or personal challenges.")
                with st.popover("Advice", icon="✅"):
                    st.write("Identify students with chronic absenteeism and understand their reasons.")
                    st.write("Implement engagement strategies, like interactive learning and student participation incentives.")

        elif sd > 30:
            st.success("Very High Spread (≥ 30) - 🚨 Major Attendance Issue")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Large differences in attendance, with some students rarely attending school.")
                st.write("Likely causes include family issues, financial constraints, or lack of motivation.")
                with st.popover("Advice", icon="✅"):
                    st.write("Survey students to understand absenteeism causes.")
                    st.write("Implement flexible attendance policies and alternative learning methods.")
                    st.write("Offer support services for struggling students.")

def analyze_standard_deviation_theory(sd, institute_type):
    if institute_type == "College":
        if sd <= 10:
            st.success("Very Low Spread (≤ 10) - 🚨 Little to No Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students have similar marks, meaning the exam may have been too easy or too hard.")
                st.write("Could indicate a lack of differentiation between strong and weak students.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure exam difficulty is balanced to effectively differentiate student performance.")
                    st.write("Introduce more diverse questions, including critical thinking and application-based problems.")
        elif sd > 10 and sd <= 20:
            st.success("Moderate Spread (10 to 20) - ✅ Healthy Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students have some variation in scores, but it is within an expected range.")
                st.write("Suggests that the exam was appropriately structured and students performed fairly consistently.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current exam structure and difficulty.")
                    st.write("Monitor future tests to ensure standard deviation stays within this range.")
        elif sd > 20 and sd <= 30:
            st.success("High Spread (20 to 30) - ⚠ Significant Performance Gaps")
            with st.expander("What's Happening?", icon="📌"):
                st.write("There is a noticeable gap between high and low scorers.")
                st.write("Some students may struggle significantly, while others excel, indicating differences in preparation or understanding.")
                with st.popover("Advice", icon="✅"):
                    st.write("Provide extra support to weaker students through additional resources or tutoring.")
                    st.write("Identify difficult topics and ensure they are taught more effectively.")
                    st.write("Review exam structure to make sure it is balanced and fair.")
        elif sd > 30:
            st.success("Very High Spread (≥ 30) - 🚨 Extreme Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students score very high, while others score extremely low.")
                st.write("Likely caused by an exam that is either too difficult, unfairly graded, or inconsistently taught.")
                st.write("Could indicate major gaps in teaching methods or student preparation levels.")
                with st.popover("Advice", icon="✅"):
                    st.write("Conduct a review of the exam's difficulty and fairness.")
                    st.write("Offer remedial classes or structured revision sessions for weaker students.")
                    st.write("Ensure teachers follow a consistent curriculum to reduce learning disparities.")
    
    if institute_type == "School":
        if sd <= 10:
            st.success("Very Low Spread (≤ 10) - 🚨 Limited Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Almost all students have similar marks, meaning the exam may have been too easy or too hard.")
                st.write("Could indicate a lack of differentiation between strong and weak students.")
                with st.popover("Advice", icon="✅"):
                    st.write("Adjust exam difficulty to better assess student comprehension.")
                    st.write("Include more application-based and critical thinking questions.")

        elif 10 < sd <= 20:
            st.success("Moderate Spread (10 to 20) - ✅ Healthy Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some variation in scores, but within an expected range.")
                st.write("Suggests that the exam was well-structured and students performed fairly.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current exam structure and difficulty.")
                    st.write("Continue monitoring test performance for consistency.")

        elif 20 < sd <= 30:
            st.success("High Spread (20 to 30) - ⚠ Performance Gaps Emerging")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students excel while others struggle significantly.")
                st.write("Indicates preparation differences, learning gaps, or inconsistent teaching methods.")
                with st.popover("Advice", icon="✅"):
                    st.write("Provide additional resources and tutoring for weaker students.")
                    st.write("Ensure all key topics are thoroughly covered in class.")
                    st.write("Review exam structure for fairness and clarity.")

        elif sd > 30:
            st.success("Very High Spread (≥ 30) - 🚨 Extreme Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students score very high, while others score extremely low.")
                st.write("Indicates either an unbalanced exam, unfair grading, or significant student knowledge gaps.")
                with st.popover("Advice", icon="✅"):
                    st.write("Conduct a review of the exam’s difficulty and fairness.")
                    st.write("Offer remedial classes and structured revision sessions.")
                    st.write("Standardize teaching methods across different classes.")

def analyze_standard_deviation_practical(sd, institute_type):
    if institute_type == "College":
        if sd <= 10:
            st.success("Very Low Spread (≤ 10) - 🚨 Lack of Differentiation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Practical marks are too uniform, meaning either everyone is equally skilled (unlikely) or the grading system lacks distinction between good and weak performers.")
                st.write("Might indicate lenient or standardized marking rather than evaluating true ability.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure practical exams test a variety of skills, not just basic execution.")
                    st.write("Use detailed rubrics to differentiate student performance more effectively.")
        elif sd > 10 and sd <= 20:
            st.success("Moderate Spread (10 to 20) - ✅ Healthy Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Students have slightly varying practical scores, meaning assessment is reasonably fair.")
                st.write("Indicates good evaluation criteria and fairly structured practical exams.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain current grading and evaluation strategies.")
                    st.write("Ensure assessments test both theoretical understanding and practical execution.")
        elif sd > 20 and sd <= 30:
            st.success("High Spread (20 to 30) - ⚠ Skill Gaps Emerging")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students excel in practical work, while others struggle significantly.")
                st.write("Indicates skill disparities—some students grasp concepts better than others.")
                st.write("May be due to differences in prior experience, preparation, or teaching quality.")
                with st.popover("Advice", icon="✅"):
                    st.write("Offer extra lab sessions or one-on-one guidance for weaker students.")
                    st.write("Standardize grading criteria to ensure fair evaluation across students.")
                    st.write("Encourage more hands-on practice to bridge skill gaps.")
        elif sd > 30:
            st.success("Very High Spread (≥ 30) - 🚨 Major Skill Disparities")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Practical marks are all over the place, suggesting major issues in evaluation fairness or skill development.")
                st.write("Could mean some students lack access to resources or proper training.")
                st.write("Might indicate subjective grading by different evaluators.")
                with st.popover("Advice", icon="✅"):
                    st.write("Conduct a grading audit to ensure fair and consistent assessment.")
                    st.write("Provide structured guidance to weaker students.")
                    st.write("Standardize rubrics and criteria to maintain fairness.")
        
    if institute_type == "School":
        if sd <= 10:
            st.success("Very Low Spread (≤ 10) - 🚨 Lack of Differentiation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Practical marks are too uniform, meaning students may not be tested on diverse skills.")
                st.write("This might indicate lenient grading or overly simple practical assessments.")
                with st.popover("Advice", icon="✅"):
                    st.write("Ensure school practical exams test fundamental understanding and skill application.")
                    st.write("Introduce detailed grading rubrics to evaluate creativity, technique, and execution.")

        elif 10 < sd <= 20:
            st.success("Moderate Spread (10 to 20) - ✅ Healthy Variation")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Students have slightly varying practical scores, indicating assessments are reasonably fair.")
                st.write("This suggests that school practicals are testing students effectively.")
                with st.popover("Advice", icon="✅"):
                    st.write("Maintain structured, well-balanced practical assessments.")
                    st.write("Ensure practical work is aligned with classroom learning and real-world applications.")

        elif 20 < sd <= 30:
            st.success("High Spread (20 to 30) - ⚠ Skill Gaps Emerging")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students excel, while others struggle significantly.")
                st.write("Indicates variations in prior exposure, resource availability, or teaching methods.")
                with st.popover("Advice", icon="✅"):
                    st.write("Provide additional practice opportunities, especially for students with limited access to resources.")
                    st.write("Encourage hands-on learning and remedial sessions for weaker students.")

        elif sd > 30:
            st.success("Very High Spread (≥ 30) - 🚨 Major Skill Disparities")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Practical marks vary widely, indicating either inconsistent grading or lack of proper training.")
                st.write("Some students might not have access to lab equipment or adequate guidance.")
                with st.popover("Advice", icon="✅"):
                    st.write("Implement standardized assessment criteria to ensure fairness.")
                    st.write("Provide extra lab sessions and hands-on training to underperforming students.")
                    st.write("Address disparities by ensuring all students receive equal opportunities for practice.")
