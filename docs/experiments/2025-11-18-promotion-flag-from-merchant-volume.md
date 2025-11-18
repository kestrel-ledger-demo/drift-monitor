# Promotion flag from merchant volume

Date: 2025-11-18
Who: Marc Gagnon
Uncertainty: U1 Drift without fraud labels

## Plan (written before the run)

Hypothesis: A merchant volume spike flag removes promotion false alarms.
What changes: Alarms suppressed for merchants with a volume spike and no score shift.
Setup: Same history plus Q4.

## Result (written the same day)

Result: False alarms 4 to 1; missed nothing.
Learned: Near the goal on history. Needs a live quarter to confirm.
Outcome: Worked
