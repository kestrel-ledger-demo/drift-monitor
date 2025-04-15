from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score


def period_auc(this_week, last_month):
    """AUC of telling the two periods apart; over 0.7 = drift (trial: 19 weeks, both waves, 17 false alarms)."""
    import numpy as np
    X = np.vstack([this_week, last_month]); y = np.r_[np.ones(len(this_week)), np.zeros(len(last_month))]
    return cross_val_score(GradientBoostingClassifier(), X, y, scoring="roc_auc", cv=3).mean()
