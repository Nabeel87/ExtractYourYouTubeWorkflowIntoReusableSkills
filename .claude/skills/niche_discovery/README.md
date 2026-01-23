# Niche Discovery Skill

## Purpose
Identifies 3-5 low-competition, high-volume YouTube niches from interest.

## Input
```json
{"interest": "string (e.g., 'fitness')", "filters": "string (optional)"}
```

## Process
1. Trends/search analysis.
2. Competition scoring.
3. Rank top niches with reasoning.

## Output
```json
{"niches": [{"name": "str", "reason": "str", "score": number}]}
```

## Success Criteria
3-5 niches, scores >80, low comp/high volume.

## Time Saved
1-2 hours research → 30s.

## Quality Improvement
Data-backed niches → 2x higher success rate vs. guesswork.

## Examples
See `examples.md`.
