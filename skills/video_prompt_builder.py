class VideoPromptBuilder:
    def generate_scene_prompts(self, concept: str) -> dict:
        """
        Generates Runway/Sora prompts for key video scenes.
        """
        return {
            "intro_hook": "Cinematic drone shot approaching an old abandoned barn in a field during golden hour, mystery vibe.",
            "mechanical_process": "Close up macro shot of a wrench turning a rusty bolt, dust falling, 4k texture, slow motion.",
            "electrical_work": " POV shot of wiring a dashboard, sparks, multimeter screen lighting up, complex machinery details.",
            "reveal": "The garage door opening slowly to reveal the fully restored car, gleaming paint, studio lighting, smoke machine effect."
        }
