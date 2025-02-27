import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def generate_histogram(df, title: str):
    """
    Generates a histogram from a single-column DataFrame or Series and returns the image as a buffer.
    X-axis markers are set at intervals of 10.

    Parameters:
        df (pd.DataFrame or pd.Series): The input DataFrame or Series.
        title (str): The title of the histogram.

    Returns:
        io.BytesIO: A buffer containing the saved histogram image.
    """
    # Ensure df is a DataFrame (even if a Series is passed)
    if isinstance(df, pd.Series):
        df = df.to_frame()  # Convert Series to DataFrame

    if df.shape[1] != 1:
        raise ValueError("DataFrame must have exactly one column.")

    column_name = df.columns[0]  # Get the column name
    data = df.iloc[:, 0].dropna().astype(float)  # Extract the first column

    # Create the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=10, edgecolor='black', alpha=0.7)

    # Set labels and ticks
    plt.xlabel(column_name)  
    plt.ylabel("Frequency")
    plt.xticks(np.arange(0, 101, 10))  # Set markers at every 10 units
    plt.title(title)  

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")  
    plt.close()  
    buffer.seek(0)  

    return buffer

def generate_scatterplot_with_regression(df: pd.DataFrame, title: str):
    """
    Generates a scatter plot with a regression line from a two-column DataFrame
    and returns the image as a buffer.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly two numerical columns.
        title (str): The title of the scatter plot.

    Returns:
        io.BytesIO: A buffer containing the saved scatter plot image.
    """

    # Validate input DataFrame
    if df.shape[1] != 2 or not all(df.dtypes.apply(np.issubdtype, args=(np.number,))):
        raise ValueError("DataFrame must contain exactly two numerical columns.")

    x_col, y_col = df.columns  # Extract column names

    # Create figure
    plt.figure(figsize=(8, 6))
    
    # Generate scatter plot with regression line
    sns.regplot(
        x=df[x_col], 
        y=df[y_col], 
        scatter_kws={'alpha': 0.5}, 
        line_kws={'color': 'red'}, 
        ci=None
    )

    # Set labels and title
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)

    # Set custom ticks
    plt.xticks(np.arange(0, 101, 10))
    plt.yticks(np.arange(0, 101, 10))

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")  # High-quality image
    plt.close()  # Close the plot to free memory
    buffer.seek(0)  # Move buffer cursor to the beginning

    return buffer  # Return the buffer containing the image

def generate_stripplots(df: pd.DataFrame):
    """
    Generates a single strip plot for all numerical columns in the given DataFrame,
    placing them next to each other using a shared axis.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
    
    Returns:
        io.BytesIO: Buffer containing the plot image.
    """
    numerical_columns = df.select_dtypes(include=['number']).columns
    
    if len(numerical_columns) == 0:
        print("No numerical columns found in the DataFrame.")
        return None  # Return None if no numerical data
    
    plt.figure(figsize=(8, 6), dpi=300)  # Updated figure size
    sns.stripplot(
        data=df[numerical_columns], jitter=True, size=5, alpha=0.25
    )
    
    plt.xticks(range(len(numerical_columns)), numerical_columns, rotation=90)
    plt.yticks(np.arange(0, 101, 10))  # Updated y-ticks
    plt.title("Strip Plot for All Numerical Columns")
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")  # High-quality image
    plt.close()  # Close plot to free memory
    buffer.seek(0)  # Move buffer cursor to start
    
    return buffer  # Return image as buffer