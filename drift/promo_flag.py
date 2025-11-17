def is_promotion(volume_ratio, tail_shift, spike=3.0, still=0.01):
    """Suppress alarms for merchants with a volume spike and no score shift (false alarms 4 to 1)."""
    return volume_ratio >= spike and abs(tail_shift) < still
