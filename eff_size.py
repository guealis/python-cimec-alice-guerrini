# LP: pandas and numpy imports required or this will not work

def eff_size(group1, group2):
    """
    Calculate Cohen's d for the mean difference between two groups and interpret the effect size.

    Parameters:
    group1 (array-like or pd.Series): First group of data.
    group2 (array-like or pd.Series): Second group of data.

    Returns:
    dict: A dictionary with Cohen's d and an interpretation of the effect size.
    """

    # Convert inputs to numpy arrays if they are pandas Series or DataFrames
    if isinstance(group1, (pd.Series, pd.DataFrame)):
        group1 = group1.values.flatten()  # Flatten in case of DataFrame
    if isinstance(group2, (pd.Series, pd.DataFrame)):
        group2 = group2.values.flatten()  # Flatten in case of DataFrame

    # Calculate means and standard deviations
    mean1 = np.mean(group1)
    mean2 = np.mean(group2)
    std1 = np.std(group1, ddof=1)  # Sample standard deviation (ddof=1)
    std2 = np.std(group2, ddof=1)

    # Sample sizes
    n1 = len(group1)
    n2 = len(group2)

    # Pooled Standard Deviation for two independent samples
    s_pooled = np.sqrt(((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / (n1 + n2 - 2))

    # Cohen's d
    cohens_d = (mean1 - mean2) / s_pooled

    # Interpretation based on Cohen's d value
    if abs(cohens_d) < 0.20:
        interpretation = "Very Small Effect Size"
    elif abs(cohens_d) < 0.50:
        interpretation = "Small Effect Size"
    elif abs(cohens_d) < 0.80:
        interpretation = "Medium Effect Size"
    else:
        interpretation = "Large Effect Size"

    return {'Cohen\'s d': cohens_d, 'Interpretation': interpretation}
