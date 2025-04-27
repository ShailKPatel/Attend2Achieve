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

# Synthetic Data

name = "John Doe"
institute_name = "ABC Institute"
institute_type = "College"
institute_logo = "sample_files/Institute_logo.jpg"

num_subjects = 4

sub1_name = "Java-1"
sub1_type = "Technical"
sub1_file = "sample_files/Sample1_Java-1.xlsx"

sub2_name = "Software Engineering"
sub2_type = "Others"
sub2_file = "sample_files/Sample2_Software_Engineering.xlsx"

sub3_name = "Maths-1"
sub3_type = "Mathematical"
sub3_file = "sample_files/Sample3_Maths-1.xlsx"

sub4_name = "Environmental Science"
sub4_type = "Others"
sub4_file = "sample_files/Sample4_ES.xlsx"

st.title("Analysis of Sample Subjects")
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

        df = pd.read_excel(file)
        
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
