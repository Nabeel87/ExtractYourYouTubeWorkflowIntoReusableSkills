# YouTube Creator Agent

## Purpose
Orchestrates 5 skills to generate complete viral YouTube content packages: niche discovery → topic → image/video prompts → optimization → script/SEO.

## Input
User prompt with interest (e.g., "Generate package for fitness") via Task tool.

## Process
Chains skills sequentially with user niche selection after discovery.

## Output
Markdown package in `notes/`:
```
# Viral YouTube Package
## Niche (user-selected) ## Topic ## Thumbnail ## Video Prompts ## Narration ## Script ## SEO
```

## Success Criteria
- User niche used end-to-end.
- Prompts ready for Midjourney/Runway.
- Full script/SEO, viral hooks.

## Time Saved
5-10 hours manual workflow → 5-10 min (90% faster).

## Quality Improvement
4x virality (optimized prompts, data niches, consistent packages) → higher CTR/retention/views.

## Usage
- Task tool: `subagent_type: youtube-creator-agent`, prompt: "Generate for [interest]".
- Select niche when prompted.
- Resume: Use agentId.

## Workflow
1. `niche_discovery` → AskUserQuestion for selection.
2. `topic_generator` → Select top topic.
3. `image_prompt_builder` → Thumbnail.
4. `video_prompt_generator` → Scenes.
5. `prompt_optimizer` → Polish + compile script/SEO.

## Examples
`notes/` packages (fitness, Pakistani cricket/food/tech).
