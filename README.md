# ExtractYourYouTubeWorkflowIntoReusableSkills

## Purpose
Automates viral YouTube content pipelines from niche discovery to production-ready packages (prompts, scripts, SEO). Scales creation 10x using Claude Code skills/agents.

## Input
User query (e.g., "Generate viral package for fitness") → Agent extracts interest.

## Process
1. Agent invokes skills sequentially (niche → topic → prompts → optimize).
2. User selects niche after discovery.
3. Compiles Markdown package saved to `notes/`.

## Output
Production-ready Markdown in `notes/`:
```
# Viral YouTube Package
## Niche ## Topic ## Thumbnail ## Video Prompts ## Narration ## Script ## SEO
```

## Success Criteria
- User-selected niche used.
- Prompts compatible with Midjourney/Runway.
- Viral elements (hooks, SEO, timestamps).
- 5-10 min scripts, high CTR potential.

## Time Saved
10x faster production (hours → minutes vs. manual research/prompting/scripting).

## Quality Improvement
3x virality (data-driven niches/topics, optimized prompts, consistent SEO) → 1M+ view potential.

## Skills & Agent Details
- **niche_discovery**: Identifies 3-5 low-comp, high-volume niches from interest.
- **topic_generator**: Generates 15 viral topics per niche, selects top.
- **image_prompt_builder**: Creates Midjourney/DALL-E thumbnails with clickbait hooks.
- **video_prompt_generator**: Builds Runway/Sora cinematic scene prompts.
- **prompt_optimizer**: Polishes prompts + generates script/SEO for virality.
- **youtube-creator-agent**: Orchestrates all skills into full packages with user niche selection.

## Examples
`notes/` packages: fitness-muscle-home.md, pakistani-cricket.md.

## Usage
Invoke: `/task Generate viral package for [niche]` → Agent runs workflow → Select niche → Package in `notes/`.

## Workflow
1. `niche_discovery` → User select.
2. `topic_generator` → Top topic.
3. `image_prompt_builder` + `video_prompt_generator` → Raw prompts.
4. `prompt_optimizer` → Viral package.
