import numpy as np
import pandas as pd
import plotly.express as px

def generate_histogram(df, title: str):
    """
    Generates a histogram from a single-column DataFrame or Series and returns the plotly figure.
    X-axis markers are set at intervals of 10.

    Parameters:
        df (pd.DataFrame or pd.Series): The input DataFrame or Series.
        title (str): The title of the histogram.

    Returns:
        plotly.graph_objects.Figure: The plotly figure containing the histogram.
    """
    # Ensure df is a DataFrame (even if a Series is passed)
    if isinstance(df, pd.Series):
        df = df.to_frame()  # Convert Series to DataFrame

    if df.shape[1] != 1:
        raise ValueError("DataFrame must have exactly one column.")

    column_name = df.columns[0]  # Get the column name
    data = df.iloc[:, 0].dropna().astype(float)  # Extract the first column

    # Create the histogram
    fig = px.histogram(
        data_frame=data, 
        x=column_name, 
        nbins=10,  # Set number of bins
        title=title
    )

    # Set custom ticks on the x-axis
    fig.update_xaxes(tickmode='linear', tick0=0, dtick=10)

    return fig

def generate_scatterplot_with_regression(df: pd.DataFrame, title: str):
    """
    Generates a scatter plot with a regression line from a two-column DataFrame
    and returns the plotly figure.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly two numerical columns.
        title (str): The title of the scatter plot.

    Returns:
        plotly.graph_objects.Figure: The plotly figure containing the scatter plot.
    """

    # Validate input DataFrame
    if df.shape[1] != 2 or not all(df.dtypes.apply(np.issubdtype, args=(np.number,))):
        raise ValueError("DataFrame must contain exactly two numerical columns.")

    x_col, y_col = df.columns  # Extract column names

    
    # Generate scatter plot with regression line
    fig = px.scatter(
        df, x=x_col, y=y_col, trendline="ols", title=title
    )

    return fig

def generate_stripplots(df: pd.DataFrame):
    """
    Generates a single strip plot for all numerical columns in the given DataFrame,
    placing them next to each other using a shared axis.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure containing the strip plot.
    """
    numerical_columns = df.select_dtypes(include=['number']).columns
    
    if len(numerical_columns) == 0:
        print("No numerical columns found in the DataFrame.")
        return None  # Return None if no numerical data
    
    fig = px.strip(df, x=numerical_columns, orientation='h')
    
    return fig