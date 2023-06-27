import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import numpy as np

def plot_acf_pacf(ts, lags):
    """
    Plot Autocorrelation and Partial Autocorrelation for a given time series.

    Parameters:
    ts (Series or DataFrame): Time series data
    lags (int): Number of lags to show in plot

    Returns:
    None
    """

    # if ts is a DataFrame, use the first column
    if isinstance(ts, pd.DataFrame):
        ts = ts.iloc[:, 0]

    fig, ax = plt.subplots(2, figsize=(12, 8))

    plot_acf(ts, lags=lags, ax=ax[0])
    plot_pacf(ts, lags=lags, ax=ax[1])

    plt.tight_layout()
    plt.show()

y = [12.4, 29.97, 48.17, 82.62, 165.81, 308.96, 452.93, 580.4, 702.06, 812.67]
y_diff = np.diff(y)

plot_acf_pacf(ts=y_diff, lags= 3)