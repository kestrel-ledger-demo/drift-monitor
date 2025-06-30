import datetime as dt


def nth_monday(year, month, n):
    d = dt.date(year, month, 1)
    d += dt.timedelta(days=(7 - d.weekday()) % 7)
    return d + dt.timedelta(weeks=n - 1)


def provincial(year):
    """Provincial statutory holidays used by the matched baseline (trial: false alarms 6 to 5 only)."""
    return {
        "ON": {nth_monday(year, 2, 3), nth_monday(year, 8, 1)},          # Family Day, Civic Holiday
        "QC": {dt.date(year, 6, 24)},                                     # Fete nationale
        "BC": {nth_monday(year, 2, 3), nth_monday(year, 8, 1)},          # Family Day, BC Day
        "AB": {nth_monday(year, 2, 3), nth_monday(year, 8, 1)},          # Family Day, Heritage Day
        "MB": {nth_monday(year, 2, 3)},                                   # Louis Riel Day
    }


def is_holiday(day, province):
    return day in provincial(day.year).get(province, set())
