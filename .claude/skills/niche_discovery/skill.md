# Niche Discovery Skill

## Purpose
Daily discovery of viral AI-driven YouTube niches optimized for AI-generated content: high engagement, low competition, with ready-to-use visuals/scripts for thumbnails/videos using Midjourney/Runway.

## Inputs (JSON Schema)
```json
{
  \"seed_keywords\": [\"array of strings\", \"e.g., [\\\"AI tools\\\", \\\"generative AI\\\"]\", \"min 2, max 10\"],
  \"country\": \"string (default: \\\"US\\\")\",
  \"timeframe\": \"string (default: \\\"today 3-m\\\")\", \"for daily freshness\"
}
```

## Process
1. Query Google Trends for seed_keywords interest-over-time (last 3 months), identify 20+ rising AI sub-niches.
2. Use YouTube Data API: search volume proxy (related searches), top 20 videos (views/likes/subscribers/upload date).
3. Compute scores: competition = (avg top20 views / 1M) * creator_count; engagement = (likes/views)*100; potential = (growth_trend * engagement) / competition.
4. Filter/enrich top 10: add AI-optimized assets (prompts, titles); ensure <50 competing videos >100k views.

## Outputs (JSON Schema)
```json
{
  \"timestamp\": \"ISO string\",
  \"niches\": [
    {
      \"keyword\": \"string\",
      \"monthly_search_volume\": \"number\",
      \"competition_score\": \"number (0-100, lower better)\",
      \"engagement_rate\": \"number %\",
      \"potential_score\": \"number (0-100)\",
      \"growth_trend\": \"number (0-100)\",
      \"example_videos\": [\"array of {id, title, views, channel}\"],
      \"suggested_titles\": [\"array of 5 SEO-optimized titles\"],
      \"thumbnail_prompt\": \"string (Midjourney-ready, 16:9, bold text + AI visuals)\",
      \"ai_video_style\": \"string (e.g., \\\"animated explainer\\\", \\\"screen recordings + B-roll\\\")\",
      \"ideal_length\": \"number (seconds, 300-900 for retention)\"
    }
  ]
}
```

## Success Criteria
- ≥7 niches with potential_score ≥90, monthly_search_volume ≥25k, competition_score ≤30.
- engagement_rate ≥4%, growth_trend ≥70 (rising 20%+ MoM).
- 100% AI-producible (prompts feasible for current tools), data <24h old, daily-reusable (timeframe auto-updates).