# Topic Generator Skill

## Purpose
Generate 10-20 viral YouTube video topics from a niche: emotion-driven (fear/greed/urgency), curiosity-based (questions/secrets), click-optimized titles for AI-generated Shorts (15-60s) and long-form (5-15min) content.

## Inputs (JSON Schema)
```json
{
  \"niche\": \"string (required, from niche_discovery)\",
  \"num_topics\": \"int (default: 15, range 10-20)\",
  \"format_preference\": \"string (default: \\\"both\\\", options: \\\"shorts\\\", \\\"longform\\\", \\\"both\\\")\"

}
```

## Process
1. Query YouTube/Trends API for niche gaps: low-comp related searches with high volume.
2. Brainstorm 50+ candidates using emotion triggers (\\\"You Won't Believe\\\", \\\"Hidden Secret\\\"), numbers/questions, urgency (\\\"2026 Only\\\"), curiosity gaps.
3. Score: CTR potential (emotion/curiosity strength), competition (<10 high-view rivals), AI-fit (visual hooks for images/videos).
4. Select top 10-20: Enrich with Shorts/long-form variants, thumbnail prompts, 10s hook scripts; ensure no generics.

## Outputs (JSON Schema)
```json
{
  \"timestamp\": \"ISO string\",
  \"topics\": [
    {
      \"title\": \"string (&lt;70 chars, front-loaded keywords)\",
      \"hook\": \"string (10-15s opening script with curiosity gap)\",
      \"curiosity_angle\": \"string (e.g., \\\"What if one tool 10x'd your views?\\\")\", \"emotion_trigger\": \"string (fear/greed/curiosity/urgency)\",
      \"format\": \"shorts/longform/both\",
      \"search_potential\": \"number (0-100)\",
      \"thumbnail_prompt\": \"string (AI image-ready, emotional reaction/face, 16:9)\",
      \"video_prompt_snippet\": \"string (first scene for AI video gen)\",
      \"tags\": [\"array 12-18 optimized tags\"]
    }
  ]
}
```

## Success Criteria
- 100% topics: unique, non-generic, ≥90 search_potential/CTR score.
- Hook reveals curiosity without spoiling; emotion balanced (30% each fear/greed/curiosity/urgency).
- Shorts: &lt;60s hooks; Long-form: scalable to 10min; all AI-producible visuals, &lt;5 competing videos &gt;50k views.