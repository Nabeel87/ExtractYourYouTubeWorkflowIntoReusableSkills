# Prompt Optimizer Skill

## Purpose
Optimize image and video prompts for virality and platform compatibility. Transforms raw prompts into polished, AI-ready versions with platform-specific adjustments, viral hooks/keywords, style tweaks, and optimal formatting for MidJourney, DALL·E, Runway, Pika, etc.

## Input
```json
{
  "raw_prompt": {
    "type": "string",
    "description": "Raw/unpolished prompt to optimize"
  },
  "target_platform": {
    "type": "string",
    "enum": ["YouTube Shorts", "YouTube Long-form", "Instagram Reels", "Instagram Posts"],
    "description": "Target social platform"
  },
  "style": {
    "type": "string",
    "optional": true,
    "description": "Optional style override (e.g., hyper-realistic, cartoon)"
  }
}
```

## Process
1. Analyze raw_prompt: Identify core subject, weak descriptors, missing elements.
2. Platform tweaks:
   - YouTube Shorts/Reels: Vertical 9:16, fast hooks, bold text overlays, high-energy motion.
   - Long-form/Posts: Horizontal 16:9, narrative depth, subtle compositions.
3. Inject virality: Power words ("shocking", "epic fail"), emotional triggers (FOMO, curiosity), trending keywords (2026 AI trends).
4. Style/tone enhancement: Amplify specifics (e.g., "dramatic lighting" → "volumetric god rays at golden hour").
5. AI formatting: Weighting (::2), parameters (--ar 9:16), comma-separated descriptors, no fluff.
6. Concision: Trim to 150-250 words, prioritize impact.

## Output
```json
{
  "optimized_prompt": {
    "type": "string",
    "description": "Polished, ready-to-use AI prompt"
  },
  "changes_made": {
    "type": "array",
    "items": { "type": "string" },
    "description": "Summary of optimizations applied"
  },
  "suggested_params": {
    "type": "object",
    "properties": {
      "aspect_ratio": { "type": "string" },
      "other": { "type": "string" }
    }
  }
}
```

## Success Criteria
- Optimized prompt 20% shorter, 2x more specific than input.
- Platform-perfect: Shorts/Reels vertical hooks; long-form epic scopes.
- Viral-ready: Includes 3+ hooks/keywords (e.g., "mind-blowing transformation", "you won't believe").
- AI-optimized: Proper syntax (--ar, --v6, ::1.5 emphasis), scannable structure.
- Measurable impact: Clickbait-compliant, trend-aligned, generates 5x engagement visuals.
