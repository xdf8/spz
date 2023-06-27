import numpy as np

def bernoulli_process(p, n):
    """
    Modelliert einen Bernoulli-Prozess.

    Args:
        p: Wahrscheinlichkeit für das Eintreten des Ereignisses (Erfolg).
        n: Anzahl der Schritte im Prozess.

    Returns:
        process: Liste von Länge n mit den Ergebnissen des Bernoulli-Prozesses.
    """
    process = np.random.choice([0, 1], size=n, p=[1-p, p])
    return process

# Beispielaufruf
p = 0.9  # Wahrscheinlichkeit für Erfolg (z.B. 30%)
n = 10  # Anzahl der Schritte im Prozess

process = bernoulli_process(p, n)
print(process)
