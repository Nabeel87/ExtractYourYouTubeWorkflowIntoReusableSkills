# Claude Code Configuration: YouTube Skills & Agents

## Purpose
Central hub for modular skills and agents automating viral YouTube content. Loaded by Claude Code for Task tool invocation.

## Input
Project queries via Claude Code CLI (e.g., `/task Generate package`).

## Process
1. Parse user intent.
2. Invoke agents/skills from subfolders.
3. Generate/save outputs to `notes/`.

## Output
Viral packages in `notes/`; JSON prompts from skills.

## Success Criteria
- Skills respond in JSON schema.
- Agents complete workflow with user interaction.
- Packages production-ready.

## Time Saved
Project-wide: 90% (days → minutes for full packages).

## Quality Improvement
5x consistency/virality (standardized prompts, data-driven).

## Examples
- `skills/` individual skills.
- `agents/youtube-creator-agent/` full orchestration.
See `notes/` for outputs.
