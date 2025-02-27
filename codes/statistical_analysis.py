import scipy.stats as stats

def calculate_correlations(df):
    """
    Calculates correlation coefficients between Attendance, Theory, and Practical.

    Parameters:
        df (pd.DataFrame): DataFrame with columns in order: Attendance, Theory, Practical.

    Returns:
    """
    corr = df.iloc[:, 0].corr(df.iloc[:, 1])  

    return (corr)

def calculate_skewness(df):
    """
    Calculates the skewness of a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        float: The skewness of the column.
    """

    df = df.to_frame()

    if df.shape[1] != 1:
        raise ValueError("DataFrame must have exactly one column.")

    return df.iloc[:, 0].skew()

def calculate_standard_deviation(df):
    """
    Calculates the standard deviation of a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        float: The standard deviation of the column.
    """

    df = df.to_frame()
    
    if len(df.columns) != 1:
        raise ValueError("DataFrame must have exactly one column.")

    return df.iloc[:, 0].std()

def calculate_mean(df):
    """
    Calculates the mean of a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        float: The mean of the column.
    """

    df = df.to_frame()
    if df.empty:
        raise ValueError("DataFrame is empty. Mean cannot be computed.")

    return df.iloc[:, 0].mean()


def calculate_median(df):
    """
    Calculates the median of a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        float: The median of the column.
    """
    df = df.to_frame()
    if df.empty:
        raise ValueError("DataFrame is empty. Median cannot be computed.")

    return df.iloc[:, 0].median()


def calculate_mode(df):
    """
    Calculates the mode of a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        float: The mode of the column.
    """
    df = df.to_frame()
    if df.empty:
        raise ValueError("DataFrame is empty. Mode cannot be computed.")

    mode_values = df.iloc[:, 0].mode()
    return mode_values[0] if not mode_values.empty else None  # Handle cases where no mode exists


def calculate_iqr(df):
    """
    Calculates the Interquartile Range (IQR) of a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        float: The IQR of the column.
    """
    df = df.to_frame()
    if df.empty:
        raise ValueError("DataFrame is empty. IQR cannot be computed.")

    return df.iloc[:, 0].quantile(0.75) - df.iloc[:, 0].quantile(0.25)


def calculate_z_score(df):
    """
    Calculates Z-scores for a single-column DataFrame.

    Parameters:
        df (pd.DataFrame): A DataFrame with exactly one column.

    Returns:
        pd.Series: The Z-scores of the column.
    """
    df = df.to_frame()
    if df.empty:
        raise ValueError("DataFrame is empty. Z-scores cannot be computed.")

    return stats.zscore(df.iloc[:, 0])
