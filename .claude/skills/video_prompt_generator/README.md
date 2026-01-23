# Video Prompt Generator Skill

## Purpose
Generates cinematic prompts for Runway/Sora videos.

## Input
```json
{"video_topic": "string", "mood": "string", "style": "enum ['cinematic']"}
```

## Process
1. Narrative arc.
2. Mood/style embedding.
3. Technical specs (camera/lighting).

## Output
```json
{"prompt": "str", "suggested_params": {"duration": "8s"}}
```

## Success Criteria
4+ elements (camera etc.), >250 chars.

## Time Saved
1 hour scripting → 15s.

## Quality Improvement
3x engagement (cinematic hooks).

## Examples
See `examples.md`.
