import os
from skills.niche_discovery import NicheDiscoverySkill
from skills.topic_generator import TopicGeneratorSkill
from skills.image_prompt_builder import ImagePromptBuilder
from skills.video_prompt_builder import VideoPromptBuilder
from skills.prompt_optimizer import PromptOptimizer

def run_agent(user_request: str):
    print(f"AGENT STARTING: Processing request '{user_request}'")

    # 1. Niche Discovery
    niche_skill = NicheDiscoverySkill()
    niches = niche_skill.discover(user_request)

    # Simple logic to pick the best niche for "process start to end"
    # In a real agent, we might ask the user or use an LLM selector.
    selected_niche = niches[1] # "Full Barn Find Restoration" fits best
    print(f"Selected Niche: {selected_niche.name}")

    # 2. Topic Generation
    topic_skill = TopicGeneratorSkill()
    topics = topic_skill.generate(selected_niche.name)
    selected_topic = topics[2] # "Timelapse" fits "process start to end" best
    # Override title slightly to match user specific request for "mechanical + electrical"
    selected_topic.title = "Full Car Restoration: Mechanical, Electrical & Bodywork (Start to Finish)"
    print(f"Selected Topic: {selected_topic.title}")

    # 3. Generate Assets
    img_builder = ImagePromptBuilder()
    thumbnails = img_builder.generate_thumbnail_prompts(selected_topic.title)

    vid_builder = VideoPromptBuilder()
    scenes = vid_builder.generate_scene_prompts(selected_topic.title)

    # 4. Optimize & Script
    optimizer = PromptOptimizer()
    final_package = optimizer.optimize(selected_topic.title, "Classic Muscle Car")

    # 5. Output to Markdown
    output_content = f"""# viral YouTube Package: Car Restoration

## 🎯 Niche & Strategy
- **Niche**: {selected_niche.name}
- **Viral Angle**: {selected_topic.viral_factor}
- **Target Audience**: DIY enthusiasts, ASMR lovers, Mechanics

## 📺 Video Title
# {final_package.title}
*(Alternative: {selected_topic.title})*

## 🎨 Thumbnail Prompts (Midjourney)
1. `{thumbnails[0]}`
2. `{thumbnails[1]}`
3. `{thumbnails[2]}`

## 🎥 Video Scene Prompts (Runway/Sora)
| Scene | Prompt |
|-------|--------|
| **Intro** | `{scenes['intro_hook']}` |
| **Mechanical** | `{scenes['mechanical_process']}` |
| **Electrical** | `{scenes['electrical_work']}` |
| **Reveal** | `{scenes['reveal']}` |

## 📜 Script Outline
{final_package.script_outline}

## 🔍 SEO Metadata
**Description:**
{final_package.description}

**Tags:**
`{', '.join(final_package.tags)}`
"""

    # Ensure notes directory exists
    os.makedirs("notes", exist_ok=True)

    filename = "notes/restoring-old-cars-package.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"DONE! Package saved to: {filename}")
    return filename

if __name__ == "__main__":
    # Simulate the user request
    run_agent("restoring old rusted cars to new one whole machinacal electric and all process start to end")
