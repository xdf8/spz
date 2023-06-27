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

        # Entry for AR order
        tk.Label(root, text="Enter AR order:").pack()
        self.order_entry = tk.Entry(root)
        self.order_entry.pack()

        # Button to generate time series and plots
        tk.Button(root, text="Generate", command=self.generate).pack()

        # Frame for plots
        self.fig_frame = tk.Frame(root)
        self.fig_frame.pack()

    def generate(self):
        # Clear existing plots
        for widget in self.fig_frame.winfo_children():
            widget.destroy()

        # Get AR order
        order = int(self.order_entry.get())

        # Generate AR parameters
        np.random.seed(1)
        ar_params = np.random.uniform(-1, 1, order).tolist()

        # Generate time series
        n_sample = 100
        ar = np.r_[1, -np.array(ar_params)]
        ma = np.array([1])
        y = arma_generate_sample(ar, ma, n_sample)

        # Create figure and subplots
        fig = Figure(figsize=(15, 5))
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)

        # Plot original time series
        ax1.plot(y)
        ax1.set_title("Time Series")

        # Plot ACF
        plot_acf(y, lags=20, ax=ax2)
        ax2.set_title("ACF")

        # Plot PACF
        plot_pacf(y, lags=20, ax=ax3)
        ax3.set_title("PACF")

        # Display plots in the GUI
        canvas = FigureCanvasTkAgg(fig, master=self.fig_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

root = tk.Tk()
app = App(root)
root.mainloop()
