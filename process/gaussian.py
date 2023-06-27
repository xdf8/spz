import numpy as np
import matplotlib.pyplot as plt

def gaussian_process(mu, sigma, T, dt):
    """
    Modelliert einen Gauß-Prozess.

    Args:
        mu: Mittelwert der Normalverteilung.
        sigma: Standardabweichung der Normalverteilung.
        T: Zeitdauer des Prozesses.
        dt: Zeitschrittgröße.

    Returns:
        process: Liste mit den Werten des Gauß-Prozesses.
    """
    num_steps = int(T / dt)
    t = np.linspace(0, T, num_steps)
    increments = np.random.normal(0, np.sqrt(dt), size=num_steps)
    process = mu * t + sigma * np.cumsum(increments)
    return process

# Beispielaufruf
y = [12.4, 29.97, 48.17, 82.62, 165.81, 308.96, 452.93, 580.4, 702.06, 812.67]
x = np.arange(2008, 2023)
y_diff = np.diff(y)
mu = np.mean(y_diff)  # Mittelwert der Normalverteilung
sigma = np.std(y_diff)  # Standardabweichung der Normalverteilung
T = 5  # Zeitdauer des Prozesses
dt = 1  # Zeitschrittgröße

process = gaussian_process(mu, sigma, T, dt)
process = process + y[-1]
y = np.append(y, process)

plt.plot(x, y, 'o-')
plt.xlabel('Zeit')
plt.ylabel('Wert')
plt.title('Gauß-Prozess')
plt.show()
