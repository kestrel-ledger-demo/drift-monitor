def matched_days(day, history, cycle="biweekly"):
    """Baseline days with the same weekday and the same position in the pay cycle."""
    step = 14 if cycle == "biweekly" else 15
    return [d for d in history if d.weekday() == day.weekday() and (day - d).days % step == 0]
