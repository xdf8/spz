import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
import pandas as pd

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ARIMA Model")

        # Entry for AR parameters
        tk.Label(root, text="Enter AR parameters (comma-separated):").pack()
        self.ar_entry = tk.Entry(root)
        self.ar_entry.pack()

        # Entry for I parameter
        tk.Label(root, text="Enter I parameter (integer):").pack()
        self.i_entry = tk.Entry(root)
        self.i_entry.pack()

        # Entry for MA parameters
        tk.Label(root, text="Enter MA parameters (comma-separated):").pack()
        self.ma_entry = tk.Entry(root)
        self.ma_entry.pack()

        # Button to generate time series and plots
        tk.Button(root, text="Generate", command=self.generate).pack()

        # Frame for plots
        self.fig_frame = tk.Frame(root)
        self.fig_frame.pack()

    def generate(self):
        # Clear existing plots
        for widget in self.fig_frame.winfo_children():
            widget.destroy()

        # Get AR parameters
        ar_params_str = self.ar_entry.get()
        ar_params = [float(p) for p in ar_params_str.split(",")] if ar_params_str else []

        # Get I parameter
        i_param = int(self.i_entry.get()) if self.i_entry.get() else 0

        # Get MA parameters
        ma_params_str = self.ma_entry.get()
        ma_params = [float(p) for p in ma_params_str.split(",")] if ma_params_str else []

        # Generate time series
        np.random.seed(1)
        n_sample = 100
        ar = np.r_[1, -np.array(ar_params)]
        ma = np.r_[1, np.array(ma_params)]
        y = arma_generate_sample(ar, ma, n_sample)

        # Apply differencing if i > 0
        y_diff = pd.Series(y).diff(i_param).dropna().to_numpy() if i_param > 0 else y

        # Determine model type
        if i_param > 0:
            model_type = "ARIMA"
        elif ar_params and ma_params:
            model_type = "ARMA"
        elif ar_params:
            model_type = "AR"
        else:
            model_type = "MA"

        # Create figure and subplots
        fig = Figure(figsize=(15, 6))
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)

        # Adjust layout
        fig.tight_layout(pad=3.0)

        # Plot original time series
        ax1.plot(y_diff)
        ax1.set_title(f"Time Series ({model_type})")

        # Plot ACF
        plot_acf(y_diff, lags=20, ax=ax2)
        ax2.set_title("ACF")

        # Plot PACF
        plot_pacf(y_diff, lags=20, ax=ax3)
        ax3.set_title("PACF")

       # Display plots in the GUI
        canvas = FigureCanvasTkAgg(fig, master=self.fig_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

root = tk.Tk()
app = App(root)
root.mainloop()
