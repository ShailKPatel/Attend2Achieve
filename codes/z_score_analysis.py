import streamlit as st

def analyze_z_score_attendance(z_score_attendance, institute_type):
    if institute_type == "School":
        if abs(z_score_attendance) < 1:
            st.success("✅ Normal Attendance Pattern")
            with st.expander("📌 What's Happening?"):
                st.write("The student's attendance is within one standard deviation of the mean.")
                st.write("This suggests that the student follows typical attendance trends in the school—neither an exceptional case nor an outlier.")
                with st.popover("✅ Action"):
                    st.write("No major concern, but continuous monitoring ensures consistency.")
                    st.write("Schools should still focus on engagement strategies to maintain attendance rates.")

        elif 1 <= abs(z_score_attendance) < 2:
            st.warning("⚠ Slightly Irregular Attendance")
            with st.expander("📌 What's Happening?"):
                st.write("Attendance is either slightly above or below the average.")
                st.write("If positive, the student has higher-than-average attendance, likely due to discipline, parental pressure, or a strong academic focus.")
                st.write("If negative, the student is missing more school than usual, which may indicate early signs of disengagement.")
                with st.popover("✅ Action"):
                    st.write("For high-attendance students, ensure their presence translates into active participation rather than passive compliance.")
                    st.write("For low-attendance students, early intervention (counseling, parental involvement) can prevent further decline.")

        elif 2 <= abs(z_score_attendance) < 3:
            st.error("🚨 High Deviation from Normal Attendance")
            with st.expander("📌 What's Happening?"):
                st.write("The student is either attending almost every day (possibly due to academic pressure or fear of missing out) or missing a significant number of classes.")
                st.write("If attendance is too high, there may be over-enforcement of school policies rather than genuine student motivation.")
                st.write("If attendance is too low, the student is at risk of falling behind academically and may lack support at home.")
                with st.popover("✅ Action"):
                    st.write("If attendance is too high, ensure the student’s well-being and balance academic and extracurricular activities.")
                    st.write("If attendance is too low, work with teachers and parents to understand underlying causes and provide academic support.")

        else:
            st.error("❌ Extreme Outlier (Critical Issue)")
            with st.expander("📌 What's Happening?"):
                st.write("The student has extreme attendance behavior—either always present (possibly forced attendance, extreme parental pressure) or barely attending school (potential school dropout risk).")
                st.write("If too high, there may be mental or physical stress on the student.")
                st.write("If too low, serious external challenges like family responsibilities, lack of motivation, bullying, or financial barriers may be affecting attendance.")
                with st.popover("✅ Action"):
                    st.write("For high-attendance outliers, ensure mental well-being and a balanced schedule.")
                    st.write("For low-attendance outliers, conduct personal interventions, offer flexible solutions, and work with family/school authorities.")

    if institute_type == "College":
        # Z-Score-Based Attendance Analysis for College Students
        if abs(z_score_attendance) < 1:
            st.success("✅ Normal Attendance Trends")
            with st.expander("📌 What’s Happening?"):
                st.write("The student's attendance is close to the mean, indicating a typical pattern where attendance aligns with the majority.")
                st.write("Unlike schools, colleges often have attendance requirements (e.g., 75% mandatory rule in Indian colleges), so normal trends are expected.")
                with st.popover("✅ Action"):
                    st.write("Encourage engagement beyond mere compliance with the attendance mandate.")
                    st.write("Offer online resources and recorded lectures to maintain learning consistency.")

        elif 1 <= abs(z_score_attendance) < 2:
            st.warning("⚠ Attendance Deviating from Norm")
            with st.expander("📌 What’s Happening?"):
                st.write("The student is either slightly above or below average attendance.")
                st.write("Higher-than-average attendance may indicate personal academic interest or strict adherence to attendance rules.")
                st.write("Lower-than-average attendance suggests growing academic disengagement, work commitments, or poor scheduling.")
                with st.popover("✅ Action"):
                    st.write("If above average, ensure engagement is voluntary, not just rule-following.")
                    st.write("If below average, discuss flexible academic options, such as recorded lectures, to support students with personal commitments.")

        elif 2 <= abs(z_score_attendance) < 3:
            st.error("🚨 Strong Attendance Disparities")
            with st.expander("📌 What’s Happening?"):
                st.write("If high, the student may be overly focused on lectures, potentially missing out on internships or skill-building activities.")
                st.write("If low, the student may be disengaged, focusing on other priorities (part-time jobs, competitive exams, lack of motivation).")
                with st.popover("✅ Action"):
                    st.write("If attendance is high, encourage a balance between academics and real-world experience (internships, projects).")
                    st.write("If attendance is low, conduct counseling sessions to identify whether disengagement is due to course irrelevance, learning difficulties, or external commitments.")

        else:
            st.error("❌ Extreme Cases (Academic Risk)")
            with st.expander("📌 What’s Happening?"):
                st.write("Very high attendance might indicate blind compliance with rules or lack of confidence in self-learning.")
                st.write("Very low attendance is a major concern—could indicate complete disengagement, plans to drop out, or poor academic interest.")
                with st.popover("✅ Action"):
                    st.write("For very high attendance, encourage self-paced learning, networking, and industry exposure.")
                    st.write("For very low attendance, provide alternative learning methods (hybrid classes, self-study plans) and conduct one-on-one mentoring.")

def analyze_z_score_theory(z_score_theory, institute_type):
    if institute_type == "School":
        # Z-Score-Based Academic Performance Analysis for School Students
        if abs(z_score_theory) < 1:
            st.success("✅ Typical Academic Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("The student's marks are within one standard deviation of the mean, meaning they perform similarly to most students in their class.")
                st.write("These students are likely following the standard school learning curve, influenced by teacher effectiveness, syllabus difficulty, and parental support.")
                with st.popover("✅ Action"):
                    st.write("Ensure they receive regular feedback and motivation to push beyond the average.")
                    st.write("Focus on active learning strategies like group discussions and application-based teaching.")

        elif 1 <= abs(z_score_theory) < 2:
            st.warning("⚠ Slightly Above/Below Average Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("Higher-than-average marks indicate students who are either naturally gifted, have extra coaching, or put in consistent effort.")
                st.write("Lower-than-average marks may signal conceptual struggles, lack of proper study methods, or issues like exam anxiety.")
                with st.popover("✅ Action"):
                    st.write("For high scorers, introduce higher-level challenges (e.g., Olympiads, project-based learning) to keep them engaged.")
                    st.write("For low scorers, implement remedial teaching sessions, personalized mentoring, and periodic self-assessments.")

        elif 2 <= abs(z_score_theory) < 3:
            st.error("🚨 High Deviation from Average")
            with st.expander("📌 What’s Happening?"):
                st.write("Very high scores suggest either an exceptional student or someone benefitting from coaching/tutoring beyond school.")
                st.write("Very low scores indicate major academic struggles, lack of conceptual clarity, or possible external issues (family problems, lack of resources, learning disabilities).")
                with st.popover("✅ Action"):
                    st.write("For top scorers, introduce advanced-level coursework and creative problem-solving tasks to sustain motivation.")
                    st.write("For struggling students, conduct one-on-one interventions, offer alternative learning methods (visual aids, storytelling techniques), and work with parents to improve learning habits.")

        else:
            st.error("❌ Extreme Outlier (Serious Concern)")
            with st.expander("📌 What’s Happening?"):
                st.write("Exceptionally high marks may indicate extraordinary academic capability but could also be linked to rote memorization, excessive pressure from parents, or unfair advantages (cheating, coaching bias).")
                st.write("Exceptionally low marks signal a student who is completely disengaged from academics, possibly facing personal hardships or requiring special educational interventions.")
                with st.popover("✅ Action"):
                    st.write("For extreme high scorers, ensure genuine understanding rather than memorization by testing application-based knowledge.")
                    st.write("For extreme low scorers, explore deep-rooted causes (psychological barriers, home environment issues, or undiagnosed learning difficulties).")

    if institute_type == "College":
        # Z-Score-Based Academic Performance Analysis for College Students
        if abs(z_score_theory) < 1:
            st.success("✅ Average Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("The student’s marks are within a normal range, indicating typical performance, often shaped by the course difficulty and study consistency.")
                st.write("Many students in Indian colleges prioritize passing rather than excelling, leading to a clustering of scores around the mean.")
                with st.popover("✅ Action"):
                    st.write("Encourage students to develop analytical thinking rather than just meeting minimum grade expectations.")
                    st.write("Promote internship-based learning and industry exposure to make theory application-driven.")

        elif 1 <= abs(z_score_theory) < 2:
            st.warning("⚠ Slightly Above/Below Average")
            with st.expander("📌 What’s Happening?"):
                st.write("Above-average students are likely serious about their academics and may be targeting higher education or placements.")
                st.write("Below-average students might be struggling with theoretical-heavy syllabi, exam pressure, or poor time management.")
                with st.popover("✅ Action"):
                    st.write("For high scorers, suggest research opportunities, peer mentoring roles, or competitive exams.")
                    st.write("For low scorers, offer study groups, skill-based courses, and simplified learning strategies (mind maps, summaries, Q&A forums).")

        elif 2 <= abs(z_score_theory) < 3:
            st.error("🚨 High Academic Variability")
            with st.expander("📌 What’s Happening?"):
                st.write("High scores likely indicate high self-discipline, coaching benefits, or natural aptitude for the subject.")
                st.write("Low scores suggest weak conceptual understanding or students prioritizing other commitments (internships, side businesses, government exam prep, or disinterest in the subject).")
                with st.popover("✅ Action"):
                    st.write("For high scorers, encourage higher academic challenges like research projects or technical paper writing.")
                    st.write("For low scorers, identify learning gaps, introduce application-based learning, and ensure that theoretical content is explained in real-world contexts.")

        else:
            st.error("❌ Extreme Cases (Academic Red Flag)")
            with st.expander("📌 What’s Happening?"):
                st.write("Exceptionally high marks may indicate a student who is either a prodigy or has an unrealistic obsession with academics, potentially lacking practical exposure.")
                st.write("Exceptionally low marks suggest complete academic detachment, risk of dropout, or misalignment with the chosen field of study.")
                with st.popover("✅ Action"):
                    st.write("For extreme high scorers, encourage a balance between theory and practical skills (hackathons, research, projects).")
                    st.write("For extreme low scorers, provide career counseling, alternate academic strategies, or course-switching options to align studies with their interests.")

def analyze_z_score_practical(z_score_practical, institute_type):
    if institute_type == "School":
        # Z-Score-Based Practical Marks Interpretation for School Students
        if abs(z_score_practical) < 1:
            st.success("✅ Normal Practical Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("Most students score close to the average, suggesting consistent grading and skill levels.")
                st.write("Likely indicates structured practical sessions and standardized evaluation.")
                with st.popover("✅ Action"):
                    st.write("Continue maintaining clear evaluation rubrics.")
                    st.write("Ensure practical work tests real understanding, not just memorization of procedures.")

        elif 1 <= abs(z_score_practical) < 2:
            st.warning("⚠ Slightly Deviating Performance")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students perform better or worse than their peers, indicating unequal grasp of practical skills.")
                st.write("Could be due to differences in exposure to labs, teacher effectiveness, or student interest.")
                with st.popover("✅ Action"):
                    st.write("Offer additional lab practice for struggling students.")
                    st.write("Introduce real-world applications of experiments to boost engagement.")

        elif 2 <= abs(z_score_practical) < 3:
            st.error("🚨 Major Performance Gap")
            with st.expander("📌 What’s Happening?"):
                st.write("High performers may have external coaching, better lab exposure, or stronger conceptual understanding.")
                st.write("Weak performers likely lack hands-on experience or struggle with experimental techniques.")
                with st.popover("✅ Action"):
                    st.write("Identify students scoring too low and provide one-on-one coaching.")
                    st.write("Ensure practical marks are not overly dependent on written explanations—focus on skill demonstration.")

        else:
            st.error("❌ Extreme Outliers")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students might be completely disengaged from practical learning.")
                st.write("Inflated scores could indicate lenient grading or favoritism.")
                st.write("Extremely low scores suggest lack of access to lab resources or fear of hands-on experiments.")
                with st.popover("✅ Action"):
                    st.write("Address possible unfair grading and ensure marks reflect actual skill levels.")
                    st.write("For students struggling, introduce interactive and hands-on training to build confidence.")

    if institute_type == "College":
        # Z-Score-Based Practical Performance Analysis for College Students
        if abs(z_score_practical) < 1:
            st.success("✅ Standard Practical Proficiency")
            with st.expander("📌 What’s Happening?"):
                st.write("Majority of students have balanced practical skills, meaning evaluation is fair.")
                st.write("Indicates sufficient lab exposure and consistent grading.")
                with st.popover("✅ Action"):
                    st.write("Maintain strong evaluation criteria that test both technical skills and conceptual understanding.")

        elif 1 <= abs(z_score_practical) < 2:
            st.warning("⚠ Performance Differences Emerging")
            with st.expander("📌 What’s Happening?"):
                st.write("Some students may have prior experience, internships, or strong theoretical understanding, giving them an edge.")
                st.write("Others might struggle due to lack of access to labs, ineffective teaching, or minimal hands-on practice.")
                with st.popover("✅ Action"):
                    st.write("Offer additional workshops for weaker students to gain real-world exposure.")
                    st.write("Introduce graded project-based practicals to improve engagement.")

        elif 2 <= abs(z_score_practical) < 3:
            st.error("🚨 Significant Skill Gap")
            with st.expander("📌 What’s Happening?"):
                st.write("High scorers might be self-learners, pursuing industry experience through internships or research projects.")
                st.write("Low scorers might be completing practicals just for marks, lacking actual skill application.")
                with st.popover("✅ Action"):
                    st.write("Encourage students to apply their practical knowledge in industry settings (internships, projects).")
                    st.write("Provide alternative learning pathways for students with weak practical foundations.")

        else:
            st.error("❌ Extreme Skill Disparities")
            with st.expander("📌 What’s Happening?"):
                st.write("Extremely high scores could mean some students have external lab exposure or coaching beyond college resources.")
                st.write("Extremely low scores indicate severe lack of understanding, zero practice, or academic disengagement.")
                with st.popover("✅ Action"):
                    st.write("Identify extreme cases and provide personalized mentorship.")
                    st.write("Implement real-world practicals, industry collaboration, or research-based evaluations to ensure practical marks reflect actual competence.")



