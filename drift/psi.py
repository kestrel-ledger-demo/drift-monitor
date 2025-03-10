import numpy as np


def psi(expected, actual, bins=10):
    """Population stability index of one input; over 0.2 = alarm (trial: alarms on 31 of 52 weeks)."""
    e, edges = np.histogram(expected, bins=bins)
    a, _ = np.histogram(actual, bins=edges)
    e = np.clip(e / e.sum(), 1e-6, None); a = np.clip(a / a.sum(), 1e-6, None)
    return float(np.sum((a - e) * np.log(a / e)))
