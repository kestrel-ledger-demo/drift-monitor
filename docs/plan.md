# Plan: drift detection without fraud labels

Written: 2025-01-09, by Dana Okafor, at the start of the project and before the first experiment.

## What we don't know
Whether model drift can be detected within a day when fraud labels arrive 45 to 90 days late.

## What is known, and why it isn't enough
- Standard practice is a population stability index (PSI) on model inputs, or comparing the model's accuracy
  with labels. Labels come 45 to 90 days late here, so accuracy can't tell us anything inside a day.
- The drift methods we checked assume labels arrive within days or weeks. None covers a 45 to 90 day delay.
- Card spending moves with paydays and holidays, so an input test may alarm on the calendar, not on fraud.

## How we will test it
- 12 months of history with the known fraud waves marked. A method passes when it flags each wave within
  1 day and raises under 2 false alarms a quarter.
- H1: PSI over 0.2 on any input flags a wave within a day.
- H2, if H1 alarms on the calendar: a classifier that tells this week from last month.
- H3: a calendar-aware baseline (same weekday, same pay cycle).
- Each run gets a note in docs/experiments/ with the plan before it starts and the result the same day.
