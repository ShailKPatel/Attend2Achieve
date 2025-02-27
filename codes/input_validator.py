import streamlit as st
import numpy as np

def validate_string(input_string):
    if not (input_string.strip() or input_string==""):
        st.error("The text input is empty. Please enter some text.")

def validate_dataframe(df):
    """
    Validates that:
    1. All values in the DataFrame are numeric and between 0 and 100.
    2. Each column name contains exactly one of the keywords: 'practical', 'theory', or 'attendance'.
    3. There are no string literals in numeric columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        bool: True if the DataFrame is valid, False otherwise.
    """
    keywords = {"practical", "theory", "attendance"}

    # Check for string literals in numeric columns (before numeric checks)
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, str)).any():
            st.error(f"Error: Column '{col}' contains string literals.")
            return False

    # Check if all values are numeric
    if not df.apply(lambda col: np.issubdtype(col.dtype, np.number)).all():
        st.error("Error: The DataFrame contains non-numeric values.")
        return False

    # Check if all values are in the range 0 to 100
    if not ((df >= 0) & (df <= 100)).all().all():
        st.error("Error: Some values are outside the range of 0 to 100.")
        return False

    # Check if each column contains exactly one keyword
    for col in df.columns:
        matches = [word for word in keywords if word in col.lower()]
        if len(matches) != 1:
            st.error(f"Error: Column '{col}' should contain exactly one of {keywords}. Found: {matches}")
            return False

    return True  # If all checks pass, return True

def has_attendance(df):
    """Checks if any column contains the word 'attendance' separated by spaces."""
    return any("attendance" in col.lower().split() for col in df.columns)

def has_theory(df):
    """Checks if any column contains the word 'theory' separated by spaces."""
    return any("theory" in col.lower().split() for col in df.columns)

def has_practical(df):
    """Checks if any column contains the word 'practical' separated by spaces."""
    return any("practical" in col.lower().split() for col in df.columns)

def get_attendance(df):
    """Returns the first column (Attendance) of the DataFrame."""
    return df.iloc[:, 0]

def get_theory(df):
    """Returns the second column (Theory) of the DataFrame."""
    return df.iloc[:, 1]

def get_practical(df):
    """Returns the third column (Practical) of the DataFrame."""
    return df.iloc[:, 2]

def get_attendance_and_theory(df):
    """Returns a DataFrame with only the first (Attendance) and second (Theory) columns."""
    return df.iloc[:, [0, 1]]

def get_attendance_and_practical(df):
    """Returns a DataFrame with only the first (Attendance) and third (Practical) columns."""
    return df.iloc[:, [0, 2]]

def get_theory_and_practical(df):
    """Returns a DataFrame with only the second (Theory) and third (Practical) columns."""
    return df.iloc[:, [1, 2]]