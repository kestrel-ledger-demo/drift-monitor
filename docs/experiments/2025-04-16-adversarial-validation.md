# Adversarial validation

Date: 2025-04-16
Who: Marc Gagnon
Uncertainty: U1 Drift without fraud labels

## Plan (written before the run)

Hypothesis: A classifier telling this week from last month only wins during fraud waves.
What changes: PSI replaced with a classifier trained to tell the two periods apart.
Setup: Same 12 months.

## Result (written the same day)

Result: AUC over 0.7 on 19 weeks; caught both waves but 17 false alarms.
Learned: Fewer false alarms but still calendar driven.
Outcome: Partly worked
