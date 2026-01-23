# Image Prompt Builder Skill

## Purpose
Generate AI image prompts for YouTube video topics. Optimized for thumbnails using MidJourney, DALL·E, or Stable Diffusion. Produces detailed, clickable prompts with lighting, composition, and color palette specifics.

## Input
```json
{
  "video_topic": {
    "type": "string",
    "description": "YouTube video topic or title"
  },
  "mood": {
    "type": "string",
    "description": "Emotional tone (e.g., exciting, mysterious, empowering)"
  },
  "style": {
    "type": "string",
    "enum": ["cinematic", "dark", "vibrant", "minimal"],
    "description": "Visual style"
  }
}
```

## Process
1. Parse video_topic for core subjects, actions, key visuals.
2. Infuse mood into expressions, atmosphere (e.g., tense shadows for mystery).
3. Tailor style:
   - Cinematic: Dramatic depth of field, lens flares, epic scales.
   - Dark: High contrast shadows, monochromatic with accent glows.
   - Vibrant: Saturated hues, dynamic gradients, energy bursts.
   - Minimal: Clean geometry, ample negative space, subtle textures.
4. Thumbnail optimizations: Expressive close-up faces, rule-of-thirds composition, bold focal points for high CTR.
5. Detail enhancers: Specific lighting (volumetric god rays, rim lighting), color palettes (e.g., neon cyan/orange clash), camera angles (low-angle heroism).
6. Assemble into cohesive, non-generic prompt avoiding vague terms.

## Output
```json
{
  "prompt": {
    "type": "string",
    "description": "Detailed, production-ready AI image prompt"
  },
  "suggested_params": {
    "type": "object",
    "properties": {
      "aspect_ratio": {
        "type": "string",
        "default": "--ar 16:9"
      },
      "version": {
        "type": "string",
        "default": "--v 6"
      },
      "quality": {
        "type": "string",
        "default": "--q 2"
      }
    }
  }
}
```

## Success Criteria
- Prompt >150 characters, includes 5+ specifics: lighting (e.g., golden hour backlighting), composition (e.g., diagonal tension lines), color palette (e.g., emerald greens + crimson accents).
- Thumbnail-focused: Clickable elements like intrigued expressions, urgent gestures, high-contrast hooks.
- No generics: Avoid "beautiful landscape"; use "jagged obsidian cliffs under stormy aurora with piercing emerald eyes".
- Versatile for MidJourney/DALL·E/SD, aspect-optimized for YouTube (1:1 or 16:9).
- Generates 10x engagement visuals: Curiosity-driven, emotionally charged, trend-aligned (faces 70%+ screen).
