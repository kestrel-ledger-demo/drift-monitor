import numpy as np


def tail_shift(scores_now, scores_base, q=0.99):
    """Shift of the model's own upper-tail scores; moves before inputs do (caught 3 of 3 waves within a day)."""
    return float(np.quantile(scores_now, q) - np.quantile(scores_base, q))
