# Video Prompt Generator Skill

## Purpose
Generate cinematic AI video prompts for YouTube topics. Compatible with Runway, Pika, Sora, Stable Diffusion Video. Creates detailed, realistic prompts including camera angles, lighting, composition, style, mood, and scene progression for high-engagement clips.

## Input
```json
{
  "video_topic": {
    "type": "string",
    "description": "YouTube video topic or title"
  },
  "mood": {
    "type": "string",
    "description": "Emotional tone (e.g., thrilling, inspirational, suspenseful)"
  },
  "style": {
    "type": "string",
    "enum": ["cinematic", "dynamic", "minimal", "epic"],
    "description": "Visual style"
  },
  "scene_ideas": {
    "type": "string",
    "optional": true,
    "description": "Optional specific scene concepts or key moments"
  }
}
```

## Process
1. Extract narrative from video_topic: hook, build-up, climax, call-to-action.
2. Embed mood: Color grading (desaturated tension), pacing (accelerando builds).
3. Apply style:
   - Cinematic: Hollywood dolly zooms, film grain, anamorphic bokeh.
   - Dynamic: Whip pans, shaky cam urgency, speed ramps.
   - Minimal: Subtle glides, vast negative space, meditative holds.
   - Epic: Aerial sweeps, particle simulations, god rays piercing clouds.
4. Video specifics: Camera (smooth tracking left-to-right), Lighting (motivated practicals evolving), Composition (rack focus shifts), Motion (parallax depth, fluid character walks).
5. Thumbnail hook integration: Start with clickable freeze-frame.
6. Compile into single coherent 5-15s prompt, AI-optimized (no impossible physics).

## Output
```json
{
  "prompt": {
    "type": "string",
    "description": "Detailed, production-ready AI video generation prompt"
  },
  "suggested_params": {
    "type": "object",
    "properties": {
      "duration": {
        "type": "string",
        "default": "8s"
      },
      "fps": {
        "type": "string",
        "default": "24"
      },
      "motion_strength": {
        "type": "string",
        "default": "medium"
      }
    }
  }
}
```

## Success Criteria
- Prompt >250 characters, specifies 4+ elements: camera (e.g., crane shot ascending), lighting (e.g., rim light flaring into backlight), composition (e.g., Dutch angle tension), style/mood (e.g., noir shadows pulsing suspense).
- Realistic & cinematic: Coherent motion paths, natural physics, filmic pacing.
- No generics: Avoid "video about cooking"; use "slow-motion overhead arc-shot of sizzling biryani spices igniting in hot oil, steam billowing in golden hour light, macro bubbles popping rhythmically, desi kitchen chaos in background bokeh".
- YouTube-optimized: Instant hooks (0-3s intrigue), seamless loops, vertical-friendly (9:16 option).
