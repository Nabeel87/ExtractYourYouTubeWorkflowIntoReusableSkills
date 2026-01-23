# Claude Code Instructions: YouTube AI Skills & Agents Project

## Project Overview
Build reusable AI skills and autonomous agents for YouTube creators. Focus on automating niche discovery, topic research, prompt generation for images/videos, scripting, and content optimization.

**Core Workflow**:
1. **Niche Discovery** → Find low-competition, high-potential topics.
2. **Research & Ideation** → Competitor analysis, stats, hooks.
3. **Prompt Engineering** → Thumbnails, video scenes, narration.
4. **Content Generation** → Scripts, agents for full video pipelines.
5. **Optimization** → SEO titles, descriptions, tags.

## Development Guidelines
- **Modular Skills**: Place in `.claude/skills/` as Python modules or JSON/YAML prompts.
- **Agents**: Use Claude Agent SDK for task-specific agents (e.g., `niche-finder-agent`).
- **APIs**: Integrate YouTube Data API, Google Trends, Ahrefs, Midjourney, RunwayML.
- **Tech Stack**: Python 3.10+, LangChain/Pydantic for agents, Streamlit for demos.
- **Conventions**:
  - Skill files: `niche_discovery.py`, `prompt_generator.py`.
  - Each skill: `inputs → process → outputs` (JSON schema).
  - Tests: `skills/tests/`.
  - Docs: Inline docstrings + `skills/README.md`.

## Task Prioritization
When working:
1. Enter plan mode for multi-file changes (EnterPlanMode).
2. Use Task tool with `Plan` agent for architecture.
3. Explore codebase with `Explore` agent.
4. Implement skills as reusable functions/classes.
5. Test with YouTube API keys (store in `.env`).
6. **Store all generated data** (e.g., viral content packages, plans, agent outputs, workflows) in the `notes/` folder as markdown files (e.g., `notes/pakistani-golgappe-package.md`).

## Example Skills to Build
```
skills/
├── niche_discovery.py      # Trends + competition analysis
├── image_prompts.py        # Midjourney/DALL-E templates
├── video_prompts.py        # Runway/Sora scene breakdowns
├── seo_optimizer.py        # Titles, tags, descriptions
└── full_pipeline.py        # Chain all skills into agent swarm
```

## Quick Start Tasks
- `/task Create niche_discovery.py skill`
- `/plan Build image prompt generator`
- `Explore current skills directory`

## Environment Setup
```
pip install google-trends-api youtube-api-client langchain pydantic streamlit python-dotenv
```

Copy your API keys to `.env`:
```
YOUTUBE_API_KEY=your_key
GOOGLE_TRENDS_API=...
MIDJOURNEY_API=...
```

Stay focused on automation that scales YouTube production 10x.
