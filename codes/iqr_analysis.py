'''📊 Interpretation of IQR Levels
IQR Range	Attendance Spread	What It Reveals	Recommended Action
≤ 10	Very Low Variability	Most students have similar attendance—either high or low.	If high: Ensure engagement. If low: Investigate attendance barriers.
10 - 20	Moderate Variability	Attendance is somewhat consistent, with slight differences.	Monitor for small attendance gaps and intervene if needed.
20 - 30	Noticeable Variability	Some students attend regularly, others are inconsistent.	Identify and support students with irregular attendance.
≥ 30	Very High Variability	Extreme differences—some students attend almost daily, others barely show up.	Conduct outreach to understand and address low-attendance reasons.'''

import streamlit as st

def analyze_iqr_attendance(iqr_value, institute_type):

    if institute_type == "School":
        # IQR Interpretation for School Attendance
        if iqr_value <= 10:
            st.warning("🚨 Very Low Variability – Uniform Attendance")
            with st.expander("📌 What’s Happening?"):
                st.write("Most students have similar attendance, either very high or very low.")
                st.write("If high: Indicates strict school policies or a culture of discipline.")
                st.write("If low: Suggests external barriers such as lack of interest, family responsibilities, or poor engagement.")
            with st.popover("✅ Action"):
                st.write("If attendance is high, ensure students are genuinely engaged and not just attending due to rules.")
                st.write("If attendance is low, identify systemic issues (e.g., ineffective teaching, scheduling conflicts, or student disengagement).")

        elif 10 < iqr_value <= 20:
            st.success("✅ Moderate Variability – Healthy Distribution")
            with st.expander("📌 What’s Happening?"):
                st.write("Attendance shows some variation but remains within a controlled range.")
                st.write("A sign that students have the freedom to miss occasional days without major discrepancies.")
            with st.popover("✅ Action"):
                st.write("Maintain current policies and engagement strategies.")
                st.write("Identify students with slightly lower attendance and provide early intervention to prevent future decline.")

        elif 20 < iqr_value <= 30:
            st.warning("⚠ Noticeable Variability – Attendance Gaps Emerging")
            with st.expander("📌 What’s Happening?"):
                st.write("Clear differences in attendance patterns—some students attend regularly, while others show inconsistencies.")
                st.write("Could indicate external distractions, lack of motivation, or disengagement.")
            with st.popover("✅ Action"):
                st.write("Track students with fluctuating attendance and assess their reasons.")
                st.write("Offer incentives for regular attendance (e.g., participation-based rewards, engaging classroom activities).")
                st.write("Collaborate with parents to improve student motivation and ensure school attendance is prioritized.")

        else:
            st.error("🚨 Very High Variability – Major Attendance Issues")
            with st.expander("📌 What’s Happening?"):
                st.write("Extreme disparities—some students attend nearly every day, while others barely show up.")
                st.write("Indicates severe engagement problems, personal or external challenges (family obligations, transportation, financial barriers).")
            with st.popover("✅ Action"):
                st.write("Conduct surveys or one-on-one discussions to understand student challenges.")
                st.write("Implement intervention strategies such as flexible attendance policies, mentorship programs, and enhanced student support systems.")
                st.write("Work with school administrators to address policy-based attendance barriers.")

    if institute_type == "College":
        # IQR-Based Attendance Interpretation for College Students
        if iqr_value <= 10:
            st.error("🚨 Very Low Variability – Overly Standardized Attendance Patterns")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Most students have similar attendance, either consistently high or low.")
                st.write("If high: Could be due to mandatory attendance policies, not necessarily engagement.")
                st.write("If low: Could indicate a lack of motivation, ineffective lectures, or scheduling conflicts.")
                with st.popover("✅ Action"):
                    st.write("If attendance is high, assess whether students are genuinely interested or just complying with policies.")
                    st.write("If low, review course structures and teaching methods to make attendance more meaningful.")

        elif 10 < iqr_value <= 20:
            st.success("✅ Moderate Variability – Balanced Attendance Trends")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some variation in attendance, but no extreme differences.")
                st.write("Suggests that students generally attend when necessary but may skip occasionally due to workload or other commitments.")
                with st.popover("✅ Action"):
                    st.write("Maintain current strategies but monitor for any early signs of declining attendance.")
                    st.write("Ensure that lecture content remains engaging and relevant.")

        elif 20 < iqr_value <= 30:
            st.warning("⚠ Noticeable Variability – Differing Priorities Among Students")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students attend regularly, while others are inconsistent.")
                st.write("Likely caused by differences in student priorities—some may balance jobs, internships, or other commitments.")
                with st.popover("✅ Action"):
                    st.write("Identify students with erratic attendance and provide academic flexibility where possible (recorded lectures, online resources).")
                    st.write("Encourage participation through interactive learning and application-based coursework.")
                    st.write("Address structural issues such as inconvenient class timings or long travel distances.")

        else:
            st.error("🚨 Very High Variability – Severe Attendance Disparities")
            with st.expander("What's Happening?", icon="📌"):
                st.write("Some students rarely miss a class, while others barely attend.")
                st.write("Could be due to a lack of course engagement, accessibility issues, or students prioritizing other commitments over lectures.")
                with st.popover("✅ Action"):
                    st.write("Re-evaluate course delivery methods to increase flexibility (hybrid learning, recorded sessions, active learning techniques).")
                    st.write("Identify struggling students and offer personalized support.")
                    st.write("Work with faculty to create engaging, participatory lectures that encourage voluntary attendance.")

def analyze_iqr_theory(iqr_value, institute_type):

    if institute_type == "School":
        # IQR-Based Theory Marks Interpretation for School Students
        if iqr_value <= 10:
            st.error("🚨 Very Low Variability – Uniform Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("Most students score similarly, either high or low.")
                st.write("If high: Indicates an easy exam or standardized teaching.")
                st.write("If low: Suggests widespread difficulty with the subject or inconsistencies in instruction.")
                with st.popover("✅ Action"):
                    st.write("If marks are consistently high, introduce more challenging, application-based questions.")
                    st.write("If marks are low, review teaching strategies, offer remedial classes, and adjust question difficulty.")

        elif 10 < iqr_value <= 20:
            st.success("✅ Moderate Variability – Healthy Score Distribution")
            with st.expander("📌 What’s Happening?"):
                st.write("Scores vary slightly but stay within a reasonable range.")
                st.write("Suggests that the exam effectively differentiates between students based on ability.")
                with st.popover("✅ Action"):
                    st.write("Maintain the current balance between difficulty and accessibility.")
                    st.write("Ensure weaker students receive support without making exams overly simple.")

        elif 20 < iqr_value <= 30:
            st.warning("⚠ Noticeable Variability – Performance Gaps Emerging")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students perform well, while others struggle significantly.")
                st.write("May indicate differences in comprehension, preparation, or study habits.")
                with st.popover("✅ Action"):
                    st.write("Identify students with low scores and provide targeted interventions (extra practice, tutoring, feedback on mistakes).")
                    st.write("Adjust teaching methodologies to support different learning paces.")

        else:
            st.error("🚨 Very High Variability – Extreme Score Differences")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students score very high, while others perform poorly.")
                st.write("Indicates inconsistencies in exam difficulty, teaching quality, or student preparedness.")
                with st.popover("✅ Action"):
                    st.write("Review the fairness of exams and grading criteria.")
                    st.write("Provide additional support for struggling students and enhance classroom engagement.")
                    st.write("Consider restructuring lessons to reinforce foundational concepts before advancing to complex topics.")

    if institute_type == "College":
        # IQR-Based Theory Marks Interpretation for College Students
        if iqr_value <= 10:
            st.error("🚨 Very Low Variability – Rigid Performance Trends")
            with st.expander("📌 What’s Happening?"):
                st.write("Most students score similarly, either very high or very low.")
                st.write("If high: Suggests an easy exam, lack of differentiation, or inflated grading.")
                st.write("If low: Indicates widespread struggles, potentially due to ineffective instruction or challenging concepts.")
                with st.popover("✅ Action"):
                    st.write("If marks are consistently high, introduce more analytical and critical-thinking-based questions.")
                    st.write("If marks are low, reassess teaching methods and provide additional academic resources.")

        elif 10 < iqr_value <= 20:
            st.success("✅ Moderate Variability – Well-Balanced Scores")
            with st.expander("📌 What’s Happening?"):
                st.write("Some variation in marks, but no extreme outliers.")
                st.write("Suggests that the exam is appropriately assessing different levels of student understanding.")
                with st.popover("✅ Action"):
                    st.write("Maintain the current evaluation structure.")
                    st.write("Encourage diverse learning approaches while ensuring fairness in assessments.")

        elif 20 < iqr_value <= 30:
            st.warning("⚠ Noticeable Variability – Learning Gaps Among Students")
            with st.expander("📌 What’s Happening?"):
                st.write("Performance differences become evident, indicating gaps in understanding.")
                st.write("Some students excel, while others struggle—likely due to varied study habits, prior knowledge, or engagement levels.")
                with st.popover("✅ Action"):
                    st.write("Offer peer mentoring programs or faculty-led review sessions.")
                    st.write("Provide supplementary study materials and encourage active learning methods.")

        else:
            st.error("🚨 Very High Variability – Major Disparities in Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students score exceptionally high, while others fail.")
                st.write("Indicates a highly uneven understanding of the subject, possibly due to inadequate preparation, assessment bias, or inconsistent teaching.")
                with st.popover("✅ Action"):
                    st.write("Reevaluate teaching strategies, assessment difficulty, and support systems.")
                    st.write("Provide struggling students with structured guidance and revision plans.")
                    st.write("Consider alternative evaluation methods (open-book tests, project-based assessments) to accommodate diverse learning styles.")

def analyze_iqr_practical(iqr_value, institute_type):
    if institute_type == "School":
        # IQR-Based Practical Marks Interpretation for School Students
        if iqr_value <= 10:
            st.error("🚨 Very Low Variability – Standardized or Lenient Evaluation")
            with st.expander("📌 What’s Happening?"):
                st.write("Practical marks are highly uniform, suggesting that most students receive similar scores.")
                st.write("This could be due to lenient marking, where teachers give high marks to all students.")
                st.write("Might indicate a lack of rigorous assessment, with practical exams focusing on rote procedures rather than real skill evaluation.")
                with st.popover("✅ Action"):
                    st.write("Introduce structured rubrics to differentiate student performance.")
                    st.write("Ensure practical exams assess application-based skills rather than just completion of tasks.")
                    st.write("Provide constructive feedback instead of awarding uniform scores.")

        elif 10 < iqr_value <= 20:
            st.success("✅ Moderate Variability – Balanced Evaluation")
            with st.expander("📌 What’s Happening?"):
                st.write("Practical marks vary slightly but remain within an expected range.")
                st.write("Suggests that some differentiation exists in student performance.")
                st.write("Likely indicates that teachers are assessing students on effort and execution.")
                with st.popover("✅ Action"):
                    st.write("Maintain current evaluation practices but ensure students receive individual feedback to improve practical skills.")
                    st.write("Encourage students to engage with practical sessions more actively rather than just following instructions.")

        elif 20 < iqr_value <= 30:
            st.warning("⚠ Noticeable Variability – Skill Gaps Becoming Evident")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students perform significantly better than others, indicating differences in skill mastery.")
                st.write("Could be due to varying levels of access to laboratory resources or hands-on practice.")
                st.write("May indicate that students from different backgrounds (e.g., urban vs. rural) have different levels of preparedness.")
                with st.popover("✅ Action"):
                    st.write("Identify students struggling with practical skills and provide additional hands-on sessions.")
                    st.write("Ensure all students have equal access to lab equipment and guidance.")
                    st.write("Conduct interactive practical classes rather than just demonstrations.")

        else:
            st.error("🚨 Very High Variability – Major Disparities in Practical Skills")
            with st.expander("📌 What’s Happening?"):
                st.write("Marks show extreme variation—some students excel, while others fail to grasp even basic concepts.")
                st.write("Likely caused by disparities in teaching methods, access to resources, or student engagement.")
                st.write("Could be an indicator of subjective grading, where different teachers apply different standards.")
                with st.popover("✅ Action"):
                    st.write("Standardize practical assessment criteria across all classes to ensure fair grading.")
                    st.write("Provide extra training and practice sessions for weaker students.")
                    st.write("Implement peer learning programs where high-performing students assist those who struggle.")

    if institute_type == "College":
        # IQR-Based Practical Marks Interpretation for College Students
        if iqr_value <= 10:
            st.error("🚨 Very Low Variability – Overly Uniform Grading")
            with st.expander("📌 What’s Happening?"):
                st.write("Most students receive similar marks, possibly due to lenient grading or lack of rigorous evaluation.")
                st.write("Practical exams might be treated as formalities rather than genuine skill assessments.")
                st.write("Could indicate a lack of complexity in assignments, leading to minimal differentiation in performance.")
                with st.popover("✅ Action"):
                    st.write("Implement detailed grading rubrics to evaluate depth of understanding and technical execution.")
                    st.write("Design practical assignments that encourage problem-solving rather than just following procedures.")

        elif 10 < iqr_value <= 20:
            st.success("✅ Moderate Variability – Fair Skill Differentiation")
            with st.expander("📌 What’s Happening?"):
                st.write("Marks exhibit slight variation, indicating that students are assessed on their practical capabilities.")
                st.write("Suggests that assessments are structured well and offer a fair reflection of skill levels.")
                with st.popover("✅ Action"):
                    st.write("Maintain current evaluation methods but ensure periodic skill-based assessments.")
                    st.write("Encourage students to document their practical work to promote deeper engagement.")

        elif 20 < iqr_value <= 30:
            st.warning("⚠ Noticeable Variability – Unequal Preparedness")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students excel, while others struggle, indicating disparities in understanding and application.")
                st.write("Could be due to differences in prior experience, quality of instruction, or access to labs.")
                st.write("Practical exposure may depend on whether students take additional workshops or external training.")
                with st.popover("✅ Action"):
                    st.write("Provide supplementary workshops or hands-on sessions for students struggling with practical skills.")
                    st.write("Incorporate real-world applications into lab assignments to improve engagement and skill retention.")
                    st.write("Ensure consistent teaching methodologies across different instructors.")

        else:
            st.error("🚨 Very High Variability – Extreme Skill Gaps")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students demonstrate mastery, while others barely meet minimum competency levels.")
                st.write("Likely caused by variations in educational background, self-learning efforts, or lack of access to necessary tools.")
                st.write("Could indicate that practical sessions are not being taken seriously by some students or institutions.")
                with st.popover("✅ Action"):
                    st.write("Implement structured mentorship programs to help weaker students bridge skill gaps.")
                    st.write("Offer elective hands-on modules for students who need additional practice.")
                    st.write("Encourage faculty to integrate project-based learning to improve real-world application of skills.")




