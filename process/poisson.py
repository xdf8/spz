import numpy as np

def poisson_process(lmbda, T):
    """
    Modelliert einen Poisson-Prozess.

    Args:
        lmbda: Ereignisrate (durchschnittliche Anzahl der Ereignisse pro Zeiteinheit).
        T: Zeitdauer des Prozesses.

    Returns:
        process: Liste mit den Zeitpunkten der Ereignisse im Poisson-Prozess.
    """
    num_events = np.random.poisson(lam=lmbda*T)
    event_times = np.sort(np.random.uniform(0, T, size=num_events))
    return event_times

# Beispielaufruf
lmbda = 0.3 # Ereignisrate (z.B. 0,5 Ereignisse pro Zeiteinheit)
T = 24 # Zeitdauer des Prozesses

process = poisson_process(lmbda, T)
print(process)
