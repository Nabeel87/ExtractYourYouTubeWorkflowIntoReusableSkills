class ImagePromptBuilder:
    def generate_thumbnail_prompts(self, topic_title: str) -> list[str]:
        """
        Generates Midjourney prompts for thumbnails.
        """
        base_style = "--ar 16:9 --v 6.0 --style raw"

        prompts = [
            f"YouTube thumbnail, split screen comparison, left side: rusted ancient car wreck in a barn covered in dust, right side: gleaming polished showroom new car, high contrast, 4k, hyperrealistic, emotional lighting {base_style}",
            f"YouTube thumbnail, close up of a mechanic's hands holding a rusted part vs a shiny new part, sparks flying in background, dramatic lighting, intense focus, 8k {base_style}",
            f"YouTube thumbnail, cinematic shot of a classic car in a dark garage with one spotlight, 'BEFORE' and 'AFTER' text overlay placeholders, hyper detailed texture of rust and chrome {base_style}"
        ]
        return prompts
