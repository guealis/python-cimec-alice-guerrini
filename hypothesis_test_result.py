def hypothesis_test_result(p_value, alpha=0.05):
    """
    Determines whether to reject or fail to reject the null hypothesis.

    Parameters:
    - p_value: The p-value from the t-test.
    - alpha: The significance level (default is 0.05).

    Returns:
    - A string indicating the result of the hypothesis test.
    """
    # Adjust the p-value for a one-sided test if needed
    if p_value <= alpha:
      result = "Reject the null hypothesis."
    else:
      result =  "Fail to reject the null hypothesis."
# Formulate the output string
    return f"P-value ({p_value}) <= Alpha ({alpha}): {result}" if p_value <= alpha else f"P-value ({p_value}) > Alpha ({alpha}): {result}"
