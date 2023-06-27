import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Autoregressive Model")

        # Entry for AR parameters
        tk.Label(root, text="Enter AR parameters (comma-separated):").pack()
        self.ar_entry = tk.Entry(root)
        self.ar_entry.pack()

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
        ar_params = [float(p) for p in ar_params_str.split(",")]

        # Generate time series
        np.random.seed(1)
        n_sample = 100
        ar = np.r_[1, -np.array(ar_params)]
        ma = np.array([1])
        y = arma_generate_sample(ar, ma, n_sample)

        # Create figure and subplots
        fig = Figure(figsize=(10, 5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        # Plot ACF
        plot_acf(y, lags=20, ax=ax1)
        ax1.set_title("ACF")

        # Plot PACF
        plot_pacf(y, lags=20, ax=ax2)
        ax2.set_title("PACF")

        # Display plots in the GUI
        canvas = FigureCanvasTkAgg(fig, master=self.fig_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

root = tk.Tk()
app = App(root)
root.mainloop()
