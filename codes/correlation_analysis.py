import streamlit as st

def analyze_correlation_attendance_vs_practical(r, institute_type):
    if institute_type == "School":
        if r >= 0.8:
            st.success("The correlation between attendance and practical marks is very strong.")
            st.write('Regular attendance ensures students participate in guided practical sessions. Parents ensure students attend, leading to better hands-on learning. Missing practical classes leads to gaps in understanding.')
            with st.popover("Why",icon='✅'):
                st.write("School students rely on structured, teacher-led practicals. Parents enforce attendance, ensuring consistent practice. Practical assessments are often directly based on attended sessions.")
            with st.popover("Advice",icon='✅'):
                st.write("Maintain high attendance; practicals are essential for skill-building. Engage actively rather than just attending. If absent, request teacher demonstrations or peer notes.")
        elif 0.5 <= r < 0.8:
            st.success("The correlation between attendance and practical marks is moderately strong.")
            st.write('Attendance helps, but some students manage through self-study. Some subjects require more practical sessions than others.')
            with st.popover("Why",icon='✅'):
                st.write("Some students supplement practicals with extra reading or videos. Schools may have lenient grading, reducing attendance impact.")
            with st.popover("Advice",icon='✅'):
                st.write("Attend as much as possible, but also use online simulations. If struggling, seek additional teacher support.")
        elif 0 <= r < 0.5:
            st.success("The correlation between attendance and practical marks is weak.")
            st.write('Some students excel in practicals despite irregular attendance. Pre-existing skills or external coaching might reduce reliance on school practicals.')
            with st.popover("Why",icon='✅'):
                st.write("Schools may not strictly enforce practical attendance. Practical marks might be leniently given.")
            with st.popover("Advice",icon='✅'):
                st.write("Focus on hands-on practice outside school. Ensure understanding of key concepts beyond attendance.")
        elif r <= 0:
            st.success("The correlation between attendance and practical marks is negative.")
            st.write('Attendance does not ensure high marks. Some high-attendance students perform poorly.')
            with st.popover("Why",icon='✅'):
                st.write("Poor quality practical sessions or ineffective teaching. External tuition might compensate for missed classes.")
            with st.popover("Advice",icon='✅'):
                st.write("If attending but not learning, focus on self-practice. Assess if school's practical sessions are beneficial.")

    if institute_type == "College":
        if r >= 0.8:
            st.success("The correlation between attendance and practical marks is very strong.")
            st.write("Practical work requires hands-on learning, making attendance crucial. Students who attend regularly have better lab experience. Unlike school, no parental enforcement—self-discipline is key.")
            with st.popover("Why", icon='✅'):
                st.write("College practicals involve complex techniques needing supervised practice. Absence means missing vital demonstrations, affecting performance.")
            with st.popover("Advice", icon='✅'):
                st.write("Attend all practicals; gaps are hard to fill. Engage actively—mere presence won’t help. Use peer study groups for additional learning.")
    
        elif 0.5 <= r < 0.8:
            st.success("The correlation between attendance and practical marks is moderately strong.")
            st.write("Some students compensate through independent study. Some subjects may require less hands-on training.")
            with st.popover("Why", icon='✅'):
                st.write("Online resources help students catch up. Marking schemes may allow recovery through theory.")
            with st.popover("Advice", icon='✅'):
                st.write("Attend regularly but also practice outside. Request recorded sessions if attendance is an issue.")
    
        elif 0 <= r < 0.5:
            st.success("The correlation between attendance and practical marks is weak.")
            st.write("Some students score well despite low attendance. Self-learning and prior experience play a bigger role.")
            with st.popover("Why", icon='✅'):
                st.write("Practical assessment might focus on results rather than attendance. External internships or self-practice could substitute lab attendance.")
            with st.popover("Advice", icon='✅'):
                st.write("Identify if practical skills are tested purely on attendance. Focus on skill-building through additional practice.")
    
        elif r <= 0:
            st.success("The correlation between attendance and practical marks is negative.")
            st.write("High attendance does not guarantee high marks. Some students with low attendance outperform others.")
            with st.popover("Why", icon='✅'):
                st.write("Poor-quality labs, lack of instructor engagement. Self-learners might grasp concepts faster.")
            with st.popover("Advice", icon='✅'):
                st.write("If attending isn’t yielding results, rethink learning strategies. Seek alternative sources like online labs, research papers.")

def analyze_correlation_attendance_vs_theory(r, institute_type):
    if institute_type == "School":
        if r >= 0.8:
            st.success("The correlation between attendance and theory marks is very strong.")
            st.write("Attendance has a direct impact on theory marks. Students who attend regularly perform better in exams. Parents and teachers actively monitor school attendance, reinforcing discipline.")
            with st.popover("Why", icon='✅'):
                st.write("School learning relies heavily on in-class instruction, and students are less likely to study independently. Teachers emphasize key points that often appear in exams. Parents enforce study routines, making high attendance students more consistent.")
            with st.popover("Advice", icon='✅'):
                st.write("Attend every class—school attendance is highly structured and contributes significantly to performance. Take notes actively and review them daily. Participate in classroom discussions and clarify doubts immediately.")
    
        elif 0.5 <= r < 0.8:
            st.success("The correlation between attendance and theory marks is moderately strong.")
            st.write("Attendance is important, but some students perform well even with moderate attendance. Parental involvement and home tutoring compensate for missed classes. Exam-oriented study habits can help students overcome gaps.")
            with st.popover("Why", icon='✅'):
                st.write("Some students rely on private tuition or home study. School teaching methods may vary—some subjects need more in-class explanation than others. A disciplined study routine outside school can balance occasional absences.")
            with st.popover("Advice", icon='✅'):
                st.write("Maintain attendance, but also develop strong independent study habits. Use school-provided resources (books, assignments) effectively. Parents should monitor self-study hours to ensure students stay on track.")
    
        elif 0 <= r < 0.5:
            st.success("The correlation between attendance and theory marks is weak.")
            st.write("Some students with low attendance still perform well. Factors like parental tutoring, coaching classes, and intelligence play a bigger role than school attendance.")
            with st.popover("Why", icon='✅'):
                st.write("Schools may focus more on rote learning rather than concept clarity. Some students excel by studying from textbooks or external sources. Exam questions might be predictable, allowing students to score without attending daily lectures.")
            with st.popover("Advice", icon='✅'):
                st.write("Identify the best learning method—school classes or self-study. If skipping classes, ensure strong self-revision to cover missed concepts. Parents should evaluate if coaching classes are making school attendance less relevant.")
    
        elif r <= 0:
            st.success("The correlation between attendance and theory marks is negative.")
            st.write("High attendance doesn’t guarantee better marks. Some students with high attendance still score low due to passive learning.")
            with st.popover("Why", icon='✅'):
                st.write("Some students attend classes but don’t actively engage. Poor teaching quality can make attendance ineffective. Rote memorization might not translate into good exam performance.")
            with st.popover("Advice", icon='✅'):
                st.write("Focus on understanding concepts rather than just attending for the sake of it. If school lessons aren’t effective, supplement with alternative learning resources. Parents should ensure their child is not just physically present in class but actively learning.")
    
    if institute_type == "College":
        if r >= 0.8:
            st.success("The correlation between attendance and theory marks is very strong.")
            st.write("College students who attend regularly perform significantly better in theory exams. Classroom learning provides in-depth explanations that are difficult to grasp through self-study alone.")
            with st.popover("Why", icon='✅'):
                st.write("Lectures cover advanced topics that require direct interaction with professors. Attendance keeps students disciplined and updated with the syllabus. Some subjects (mathematics, science) require real-time problem-solving, making attendance critical.")
            with st.popover("Advice", icon='✅'):
                st.write("Prioritize attending key lectures, especially for technical or concept-heavy subjects. Take detailed notes and revise consistently. Participate in discussions to get deeper insights.")
    
        elif 0.5 <= r < 0.8:
            st.success("The correlation between attendance and theory marks is moderately strong.")
            st.write("Attending lectures helps, but self-study and personal effort also play a significant role. Some students compensate for missing classes by using recorded lectures or external resources.")
            with st.popover("Why", icon='✅'):
                st.write("College learning is more independent—some students prefer studying from books and online resources. Certain courses allow students to grasp concepts without regular attendance. Study techniques and exam strategies can impact performance more than physical presence.")
            with st.popover("Advice", icon='✅'):
                st.write("If attendance is inconsistent, ensure strong self-study routines. Use online courses, recorded lectures, and study groups to reinforce learning. Identify key lectures that are essential and prioritize attending them.")
    
        elif 0 <= r < 0.5:
            st.success("The correlation between attendance and theory marks is weak.")
            st.write("Attendance has little to no effect on theory marks. Some students perform well with minimal classroom attendance.")
            with st.popover("Why", icon='✅'):
                st.write("Many college courses rely more on self-learning and external references. Some students prefer studying independently or taking help from online sources. Certain professors may not add significant value beyond textbooks.")
            with st.popover("Advice", icon='✅'):
                st.write("If lectures are not helpful, focus on self-paced learning. Use supplementary materials like research papers, video lectures, and tutorials. Attend only critical sessions that provide new insights beyond textbooks.")
    
        elif r <= 0:
            st.success("The correlation between attendance and theory marks is negative.")
            st.write("In some cases, students with high attendance perform worse. Attending every class doesn’t always translate to better understanding.")
            with st.popover("Why", icon='✅'):
                st.write("Passive attendance (just sitting in class) is ineffective. Some professors may not teach efficiently, making attendance unproductive. Self-study methods may be more effective than attending lectures.")
            with st.popover("Advice", icon='✅'):
                st.write("Identify whether lectures are beneficial or just a formality. If skipping classes, use structured study methods to cover the syllabus. Engage in practical applications of theory rather than just attending lectures.")
    
def analyze_correlation_theory_vs_practical(r, institute_type):
    if institute_type == "School":
        if r >= 0.8:
            st.success("The correlation between theory and practical marks is extremely high – this is not a good sign.")
            st.write("Theory and practical marks are nearly identical—students who perform well in theory automatically score high in practicals. Practical exams might be too easy or not testing hands-on skills effectively.")
            with st.popover("Why is this a problem?", icon='🚨'):
                st.write("Practical exams should assess real-world application, not just repeat theory assessments. If practical scores are inflated, students may not develop real skills.")
                st.write("Common reasons: Lenient grading in practicals, practical exams focusing on theory-based questions rather than hands-on tasks.")
            with st.popover("Advice", icon='✅'):
                st.write("Schools should redesign practical exams to test real execution skills. Introduce problem-solving tasks instead of rote procedures. Use viva questions to test understanding beyond just performing steps.")
    
        elif 0.5 <= r < 0.8:
            st.success("The correlation between theory and practical marks is in the ideal range.")
            st.write("Students with strong theory scores generally do well in practicals, but the link isn’t absolute. Practical exams test different skills rather than just reinforcing theory.")
            with st.popover("Why is this good?", icon='✅'):
                st.write("Students with good understanding can apply concepts effectively. Practical exams encourage creativity and execution, not just memorization.")
            with st.popover("Advice", icon='✅'):
                st.write("Maintain this balance—ensure practicals remain hands-on rather than just written assessments. Encourage students to think critically instead of blindly following steps. Ensure grading criteria reward real application skills.")
    
        elif 0 <= r < 0.5:
            st.success("The correlation between theory and practical marks is weak or nonexistent – this is also a problem.")
            st.write("No strong connection between theory and practical marks. Some students do well in theory but poorly in practicals, and vice versa.")
            with st.popover("Why is this a problem?", icon='❌'):
                st.write("If theory toppers struggle in practicals: They might lack real-world application skills. Practical training might be ineffective or insufficient.")
                st.write("If students excel in practicals but fail theory: Theory exams might be too abstract or disconnected from real learning.")
            with st.popover("Advice", icon='✅'):
                st.write("Bridge the gap between theory and practice through better teaching methods. Introduce real-world examples in theory lessons. Make practicals more reasoning-based (students should explain why a procedure works, not just how).")
    
        elif r < 0:
            st.success("The correlation between theory and practical marks is negative – this is highly unusual and concerning.")
            st.write("Higher theory marks are linked to lower practical marks, or vice versa. This should not happen under normal academic evaluation.")
            with st.popover("Why is this happening?", icon='🚨'):
                st.write("Flawed grading system—students may be unfairly penalized in one area. Institutional bias—some schools prioritize either theory or practicals, leading students to neglect one.")
            with st.popover("Advice", icon='✅'):
                st.write("Investigate grading policies—ensure fair assessment in both areas. Balance coursework to develop both conceptual and practical skills. Encourage integrated learning where theory and application are connected.")

    if institute_type == "College":
        if r >= 0.8:
            st.success("The correlation between theory and practical marks is extremely high – this is not a good sign.")
            st.write("Theory and practical marks are nearly identical—students who score well in one automatically excel in the other. Practical assessments might not be testing real-world skills.")
            with st.popover("Why is this a problem?", icon='🚨'):
                st.write("College practicals should assess technical execution, critical thinking, and real-world application, not just reinforce theory.")
                st.write("Possible issues: Practical exams are too easy or poorly designed. Evaluation might be too lenient or standardized across all students.")
            with st.popover("Advice", icon='✅'):
                st.write("Introduce realistic practical problems instead of predictable experiments. Make practical exams more interactive, like:")
                st.write("- Open-ended problem-solving.")
                st.write("- Real-world case studies.")
                st.write("- Project-based assessments.")
                st.write("Add a viva to assess deeper understanding.")
    
        elif 0.5 <= r < 0.8:
            st.success("The correlation between theory and practical marks is in the ideal range.")
            st.write("Theory and practical marks show a reasonable connection, meaning students apply concepts well. Practical exams test distinct but related skills.")
            with st.popover("Why is this good?", icon='✅'):
                st.write("Conceptual knowledge supports practical execution, but marks aren’t identical. Practical exams evaluate creativity, problem-solving, and technical application.")
            with st.popover("Advice", icon='✅'):
                st.write("Keep practicals application-focused, not just procedural. Encourage hands-on experimentation with minimal guidance. Ensure grading rewards innovative thinking and execution, not just repetition.")
    
        elif 0 <= r < 0.5:
            st.success("The correlation between theory and practical marks is weak or nonexistent – this is also a problem.")
            st.write("No significant link between theory and practical marks. Some students ace theory but struggle in practicals, and vice versa.")
            with st.popover("Why is this a problem?", icon='❌'):
                st.write("If theory toppers perform poorly in practicals: They lack hands-on skills despite understanding concepts. The practical exam might require unfamiliar techniques not covered in class.")
                st.write("If practical high scorers fail theory: Theory exams might be too theoretical or abstract. These students may rely on execution rather than conceptual depth.")
            with st.popover("Advice", icon='✅'):
                st.write("Improve hands-on learning integration in theoretical courses. Encourage reasoning-based practicals—students should explain processes, not just perform them. Offer bridge programs to help students connect theoretical and practical knowledge.")
    
        elif r < 0:
            st.success("The correlation between theory and practical marks is negative – this is highly unusual and concerning.")
            st.write("Higher theory marks are associated with lower practical marks, or vice versa. This suggests a fundamental issue in the education system.")
            with st.popover("Why is this happening?", icon='🚨'):
                st.write("Evaluation methods may be flawed—students who excel in theory might be penalized in practicals. Institutional biases—some universities might emphasize either theory or practicals disproportionately. Students might focus on one assessment type, neglecting the other.")
            with st.popover("Advice", icon='✅'):
                st.write("Review grading rubrics to ensure fairness. Encourage students to balance theoretical and practical preparation. Redesign practical exams to test both technical execution and conceptual depth.")
