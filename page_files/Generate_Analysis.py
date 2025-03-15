import streamlit as st
from PIL import Image
import pandas as pd

import codes.input_validator as iv
import codes.graph_generator as gg
import codes.statistical_analysis as sa

import codes.correlation_analysis as ca
import codes.skewness_analysis as ska
import codes.standard_deviation_analysis as sda
import codes.mean_median_mode_analysis as mma
import codes.iqr_analysis as iqa
import codes.z_score_analysis as zsa


# Logo
st.logo("resources/logo.png", icon_image="resources/logo.png",size='large')

# Title
st.title("Institute Form")

# Session State Variables initailization
if 'next_btn' not in st.session_state:
    st.session_state.next_btn = False

# Callbacks
def change_next_btn_state():
    st.session_state['next_btn'] = True

#  Input fields related to Institute   
with st.container(border=True):
    # Name
    name = st.text_input("Enter your Name")
    iv.validate_string(name)

    # Institute Name
    institute_name = st.text_input("Enter your Institute Name")
    iv.validate_string(institute_name)

    # Institute Type
    institute_type = st.radio(
        "Institute Type",
        ["School", "College"],
        captions=[
            "1st - 12th Grade",
            "Diploma, Degree, Masters, etc.",
        ],
        horizontal=True,
    )

    # Institute Logo
    institute_logo = st.file_uploader("Upload Institute Logo", type=["png", "jpg", "jpeg"])

    # Check if a file is uploaded
    if institute_logo is not None:
        try:
        # Open and display the image
            image = Image.open(institute_logo)
            st.image(image, caption="Uploaded Institute Logo", use_container_width=True)
            st.success("Logo uploaded successfully!")
        except Exception as e:
            st.error(f"Error processing the file: {e}")

    # Number of Subjects
    num_subjects = st.slider("Number of Subjects", 1, 10,4)

    all_valid = institute_name and name and institute_logo

    # Next button
    st.button(label="Next", disabled=not all_valid, icon="➡️", on_click=change_next_btn_state)  


# Subjects      
if st.session_state.next_btn:
    # * Inputs related to Subjects

    #  Subject 1 (minimum 1 subject always true)
    with st.expander(label="Subject 1", icon='1️⃣'):
        st.header("Subject 1")
            
        # Subject Name
        sub1_name = st.text_input("Enter Subject-1 Name")
        iv.validate_string(sub1_name)
    
        # Subject Type
        sub1_type = st.selectbox(
            "Subject-1 Type",
            ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
            index=None,
            placeholder="Select Subject-1 type",
        ) 
    
        # # Subject Practical
        # if sub1_type == "Technical":
        #     sub1_practical = st.checkbox("Practical")
    
        # Subject File
        sub1_file = st.file_uploader("Upload Subject-1 File", type=["xls","xlsx"])

    # Subject 2
    if num_subjects >= 2:
        with st.expander(label="Subject 2", icon='2️⃣'):
            st.header("Subject 2")
            # Subject Name
            sub2_name = st.text_input("Enter Subject-2 Name")
            iv.validate_string(sub2_name)

            # Subject Type
            sub2_type = st.selectbox(
                "Subject-2 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Select Subject-2 type",
            ) 

            # # Subject Practical
            # if sub2_type == "Technical":
            #     sub2_practical = st.checkbox("Practical")

            # Subject File
            sub2_file = st.file_uploader("Upload Subject-2 File", type=["xls","xlsx"])
    
    # Subject 3
    if num_subjects >= 3:
        with st.expander(label="Subject 3", icon='3️⃣'):
            st.header("Subject 3")
            # Subject Name
            sub3_name = st.text_input("Enter Subject-3 Name")
            iv.validate_string(sub3_name)

            # Subject Type
            sub3_type = st.selectbox(
                "Subject-3 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-3 Type",
            ) 

            # # Subject Practical
            # if sub3_type == "Technical":
            #     sub3_practical = st.checkbox("Practical")

            # Subject File
            sub3_file = st.file_uploader("Upload Subject-3 File", type=["xls","xlsx"])
    
    # Subject 4
    if num_subjects >= 4:
        with st.expander(label="Subject 4", icon='4️⃣'):
            st.header("Subject 4")
            # Subject Name
            sub4_name = st.text_input("Enter Subject-4 Name")
            iv.validate_string(sub4_name)

            # Subject Type
            sub4_type = st.selectbox(
                "Subject-4 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-4 Type",
            ) 

            # # Subject Practical
            # if sub4_type == "Technical":
            #     sub4_practical = st.checkbox("Practical")

            # Subject File
            sub4_file = st.file_uploader("Upload Subject-4 File", type=["xls","xlsx"])
    
    # Subject 5
    if num_subjects >= 5:
        with st.expander(label="Subject 5", icon='5️⃣'):
            st.header("Subject 5")
            # Subject Name
            sub5_name = st.text_input("Enter Subject-5 Name")
            iv.validate_string(sub5_name)

            # Subject Type
            sub5_type = st.selectbox(
                "Subject-5 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-5 Type",
            ) 

            # # Subject Practical
            # if sub5_type == "Technical":
            #     sub5_practical = st.checkbox("Practical")

            # Subject File
            sub5_file = st.file_uploader("Upload Subject-5 File", type=["xls","xlsx"])
    
    # Subject 6
    if num_subjects >= 6:
        with st.expander(label="Subject 6", icon='6️⃣'):
            st.header("Subject 6")
            # Subject Name
            sub6_name = st.text_input("Enter Subject-6 Name")
            iv.validate_string(sub6_name)

            # Subject Type
            sub6_type = st.selectbox(
                "Subject-6 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-6 Type",
            ) 

            # # Subject Practical
            # if sub6_type == "Technical":
            #     sub6_practical = st.checkbox("Practical")

            # Subject File
            sub6_file = st.file_uploader("Upload Subject-6 File", type=["xls","xlsx"])
    
    # Subject 7
    if num_subjects >= 7:
        with st.expander(label="Subject 7", icon='7️⃣'):
            st.header("Subject 7")
            # Subject Name
            sub7_name = st.text_input("Enter Subject-7 Name")
            iv.validate_string(sub7_name)

            # Subject Type
            sub7_type = st.selectbox(
                "Subject-7 Type",
                ("Technical", "Mathematical","Science", "Language & Literature", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-7 Type",
            ) 

            # # Subject Practical
            # if sub7_type == "Technical":
            #     sub7_practical = st.checkbox("Practical")

            # Subject File
            sub7_file = st.file_uploader("Upload Subject-7 File", type=["xls","xlsx"])
    
    # Subject 8
    if num_subjects >= 8:
        with st.expander(label="Subject 8", icon='8️⃣'):
            st.header("Subject 8")
            # Subject Name
            sub8_name = st.text_input("Enter Subject-8 Name")
            iv.validate_string(sub8_name)

            # Subject Type
            sub8_type = st.selectbox(
                "Subject Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-8 Type",
            ) 

            # # Subject Practical
            # if sub8_type == "Technical":
            #     sub8_practical = st.checkbox("Practical")

            # Subject File
            sub8_file = st.file_uploader("Upload Subject-8 File", type=["xls","xlsx"])
    
    # Subject 9
    if num_subjects >= 9:
        with st.expander(label="Subject 9", icon='9️⃣'):
            st.header("Subject 9")
            # Subject Name
            sub9_name = st.text_input("Enter Subject-9 Name")
            iv.validate_string(sub9_name)

            # Subject Type
            sub9_type = st.selectbox(
                "Subject Type",
                ("Technical", "Mathematical","Science", "Language & Literature", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-9 Type",
            ) 

            # Subject Practical
            if sub9_type == "Technical":
                sub9_practical = st.checkbox("Practical")

            # Subject File
            sub9_file = st.file_uploader("Upload Subject-9 File", type=["xls","xlsx"])
    
    # Subject 10
    if num_subjects >= 10:
        with st.expander(label="Subject 10"):
            st.header("Subject 10")
            # Subject Name
            sub10_name = st.text_input("Enter Subject-10 Name")
            iv.validate_string(sub10_name)

            # Subject Type
            sub10_type = st.selectbox(
                "Subject-10 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-10 Type",
            ) 

            # # Subject Practical
            # if sub10_type == "Technical":
            #     sub10_practical = st.checkbox("Practical")

            # Subject File
            sub10_file = st.file_uploader("Upload Subject-10 File", type=["xls","xlsx"])

    # Checking if all files are present
    all_files_present = True

    for i in range(1,num_subjects+1):
        if eval(f"sub{i}_file") is None:
            all_files_present = False
            st.error(f"Please upload file for Subject-{i}")
            break
    
    if all_files_present:
        st.success("All files uploaded successfully!")
        st.balloons()

        # Check if all values are in 0 to 100 range and columns heading are having either 'practical' or 'theory' or 'attendance' exactly once in each fileby checking its filetype csv or xls or xlsx...
        all_files_valid = True

        for i in range(1,num_subjects+1):
            file = eval(f"sub{i}_file")
            
            if file is not None:
                filetype = file.type
                
                if filetype == "application/vnd.ms-excel" or filetype == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                    df = pd.read_excel(file)
                # elif filetype == "text/csv":
                #     df = pd.read_csv(file)
                else:
                    st.error(f"Invalid Subject-{i} file type")
                    all_files_valid = False
                    break

                is_valid = iv.validate_dataframe(df)

                if not is_valid:
                    st.error(f"Subject-{i} file is invalid")
                    all_files_valid = False
                    break 

        # * Analysis all provided subjects
        if all_files_valid:           
            st.divider()

            st.title("Analysis of Provided Subjects")
            st.image(institute_logo)

            st.header(f"{institute_name}")
            st.subheader(f"Institute Type: {institute_type}")
            st.subheader(f"Prepared By: {name}")

            st.subheader("Made using :rainbow[Attendance For Impact]")

            st.divider()

            # * Subject wise Analysis
            for i in range(1,num_subjects+1):

                file = eval(f"sub{i}_file")
                if file is not None:

                    st.header(f"Subject - {i}: {eval(f'sub{i}_name')}")

                    if eval(f"sub{i}_file").type == 'text/csv':
                        df = pd.read_csv(file)
                    elif eval(f"sub{i}_file").type == "application/vnd.ms-excel" or "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                        df = pd.read_excel(file)
                    else:
                        st.error(f"Invalid Subject-{i} file type")
                        all_files_valid = False
                        break
                    
                    # Display the DataFrame
                    st.dataframe(df, use_container_width=True)

                    # * Scatter Plot
                    # Attendance vs Theory Relationship
                    if iv.has_attendance(df) and iv.has_theory(df):
                        st.subheader("Attendance - Theory Relationship")
                        scatter_fig = gg.generate_scatterplot_with_regression(iv.get_attendance_and_theory(df),'Attendance vs Theory Relationship')
                        st.plotly_chart(scatter_fig)

                        corr_attendance_theory = sa.calculate_correlations(iv.get_attendance_and_theory(df))
                        st.write(f"Correlation between Attendance & Theory: {corr_attendance_theory}")
                        ca.analyze_correlation_attendance_vs_theory(corr_attendance_theory, institute_type)

                    
                    # Attendance vs Practical Relationship
                    if iv.has_attendance(df) and iv.has_practical(df):
                        st.subheader("Attendance - Practical Relationship")
                        scatter_fig = gg.generate_scatterplot_with_regression(iv.get_attendance_and_practical(df),'Attendance vs Practical Relationship')
                        st.plotly_chart(scatter_fig)

                        corr_attendance_practical = sa.calculate_correlations(iv.get_attendance_and_practical(df))
                        st.write(f"Correlation between Attendance & Practical: {corr_attendance_practical}")
                        ca.analyze_correlation_attendance_vs_practical(corr_attendance_practical, institute_type)
                    
                    # Theory vs Practical Relationship
                    if iv.has_theory(df) and iv.has_practical(df):
                        st.subheader("Theory - Practical Relationship")
                        scatter_fig = gg.generate_scatterplot_with_regression(iv.get_theory_and_practical(df),'Theory vs Practical Relationship')
                        st.plotly_chart(scatter_fig)

                        corr_theory_practical = sa.calculate_correlations(iv.get_theory_and_practical(df))
                        st.write(f"Correlation between Theory & Practical: {corr_theory_practical}")
                        ca.analyze_correlation_theory_vs_practical(corr_theory_practical, institute_type)

                    # * Histogram
                    # Attendance Histogram
                    if iv.has_attendance(df):
                        st.subheader("Attendance Histogram")
                        histogram_fig = gg.generate_histogram(iv.get_attendance(df),'Attendance Histogram')
                        st.plotly_chart(histogram_fig)
                    
                    # Theory Histogram
                    if iv.has_theory(df):
                        st.subheader("Theory Histogram")
                        histogram_fig = gg.generate_histogram(iv.get_theory(df),'Theory Histogram')
                        st.plotly_chart(histogram_fig)
                    
                    # Practical Histogram
                    if iv.has_practical(df):
                        st.subheader("Practical Histogram")
                        histogram_fig = gg.generate_histogram(iv.get_practical(df),'Practical Histogram')
                        st.plotly_chart(histogram_fig)

                    # * Skew Analysis
                    st.subheader("Skewness Analysis")
                    if iv.has_attendance(df):
                        skew_attendance = sa.calculate_skewness(iv.get_attendance(df))

                        st.write(f"Skewness of Attendance: {skew_attendance}")
                        ska.analyze_skewness_attendance(skew_attendance, institute_type)

                    if iv.has_theory(df):
                        skew_theory = sa.calculate_skewness(iv.get_theory(df))
                        st.write(f"Skewness of Theory: {skew_theory}")
                        ska.analyze_skewness_theory(skew_theory, institute_type)

                    if iv.has_practical(df):
                        skew_practical = sa.calculate_skewness(iv.get_practical(df))
                        st.write(f"Skewness of Practical: {skew_practical}")
                        ska.analyze_skewness_practical(skew_practical, institute_type)

                    # * Standard Deviation Analysis
                    st.subheader("Standard Deviation Analysis")
                    if iv.has_attendance(df):
                        std_attendance = sa.calculate_standard_deviation(iv.get_attendance(df))
                        st.write(f"Standard Deviation of Attendance: {std_attendance}")
                        sda.analyze_standard_deviation_attendance(std_attendance, institute_type)

                    if iv.has_theory(df):
                        std_theory = sa.calculate_standard_deviation(iv.get_theory(df))
                        st.write(f"Standard Deviation of Theory: {std_theory}")
                        sda.analyze_standard_deviation_theory(std_theory, institute_type)

                    if iv.has_practical(df):
                        std_practical = sa.calculate_standard_deviation(iv.get_practical(df))
                        st.write(f"Standard Deviation of Practical: {std_practical}")
                        sda.analyze_standard_deviation_practical(std_practical, institute_type)

                    # * Mean - Median Analysis
                    st.subheader("Mean - Median Analysis")

                    if iv.has_attendance(df):
                        mean_attendance = sa.calculate_mean(iv.get_attendance(df))
                        median_attendance = sa.calculate_median(iv.get_attendance(df))
                        st.write(f"Mean of Attendance: {mean_attendance}")
                        st.write(f"Median of Attendance: {median_attendance}")
                        mma.analyze_mean_median(mean_attendance, median_attendance, institute_type)

                    if iv.has_theory(df):
                        mean_theory = sa.calculate_mean(iv.get_theory(df))
                        median_theory = sa.calculate_median(iv.get_theory(df))
                        st.write(f"Mean of Theory: {mean_theory}")
                        st.write(f"Median of Theory: {median_theory}")
                        mma.analyze_mean_median(mean_theory, median_theory, institute_type)

                    if iv.has_practical(df):
                        mean_practical = sa.calculate_mean(iv.get_practical(df))
                        median_practical = sa.calculate_median(iv.get_practical(df))
                        st.write(f"Mean of Practical: {mean_practical}")
                        st.write(f"Median of Practical: {median_practical}")
                        mma.analyze_mean_median(mean_practical, median_practical, institute_type)

                    # * Mean - Mode Analysis
                    st.subheader("Mean - Mode Analysis")

                    if iv.has_attendance(df):
                        mean_attendance = sa.calculate_mean(iv.get_attendance(df))
                        mode_attendance = sa.calculate_mode(iv.get_attendance(df))
                        st.write(f"Mean of Attendance: {mean_attendance}")
                        st.write(f"Mode of Attendance: {mode_attendance}")
                        mma.analyze_mean_mode(mean_attendance, mode_attendance, institute_type)

                    if iv.has_theory(df):
                        mean_theory = sa.calculate_mean(iv.get_theory(df))
                        mode_theory = sa.calculate_mode(iv.get_theory(df))
                        st.write(f"Mean of Theory: {mean_theory}")
                        st.write(f"Mode of Theory: {mode_theory}")
                        mma.analyze_mean_mode(mean_theory, mode_theory, institute_type)

                    if iv.has_practical(df):
                        mean_practical = sa.calculate_mean(iv.get_practical(df))
                        mode_practical = sa.calculate_mode(iv.get_practical(df))
                        st.write(f"Mean of Practical: {mean_practical}")
                        st.write(f"Mode of Practical: {mode_practical}")
                        mma.analyze_mean_mode(mean_practical, mode_practical, institute_type)

                    # * Inter Quartile Range Analysis
                    st.subheader("Inter Quartile Range Analysis")

                    if iv.has_attendance(df):
                        iqr_attendance = sa.calculate_iqr(iv.get_attendance(df))
                        st.write(f"Inter Quartile Range of Attendance: {iqr_attendance}")
                        iqa.analyze_iqr_attendance(iqr_attendance, institute_type)

                    if iv.has_theory(df):
                        iqr_theory = sa.calculate_iqr(iv.get_theory(df))
                        st.write(f"Inter Quartile Range of Theory: {iqr_theory}")
                        iqa.analyze_iqr_theory(iqr_theory, institute_type)

                    if iv.has_practical(df):
                        iqr_practical = sa.calculate_iqr(iv.get_practical(df))
                        st.write(f"Inter Quartile Range of Practical: {iqr_practical}")
                        iqa.analyze_iqr_practical(iqr_practical, institute_type)

                    # * Z-Score Analysis
                    # st.subheader("Z-Score Analysis")

                    # if iv.has_attendance(df):
                    #     z_score_attendance = sa.calculate_z_score(iv.get_attendance(df))
                    #     st.write(f"Z-Score of Attendance: {z_score_attendance}")
                    #     zsa.analyze_z_score_attendance(z_score_attendance, institute_type)

                    # if iv.has_theory(df):
                    #     z_score_theory = sa.calculate_z_score(iv.get_theory(df))
                    #     st.write(f"Z-Score of Theory: {z_score_theory}")
                    #     zsa.analyze_z_score_theory(z_score_theory, institute_type)

                    # if iv.has_practical(df):
                    #     z_score_practical = sa.calculate_z_score(iv.get_practical(df))
                    #     st.write(f"Z-Score of Practical: {z_score_practical}")
                    #     zsa.analyze_z_score_practical(z_score_practical, institute_type)

                    st.divider()

            # * Overall Analysis
            st.header("Overall Analysis")
            merged_df = pd.DataFrame()
            for i in range(1,num_subjects+1):

                file = eval(f"sub{i}_file")
                if file is not None:
                    first_column = df.iloc[:, 0].rename(eval(f"sub{i}_name"))   
    
                    # Merge into the main DataFrame
                    merged_df = pd.concat([merged_df, first_column], axis=1)

            stripplot_fig = gg.generate_stripplots(merged_df)

            st.plotly_chart(stripplot_fig, use_container_width=True)





