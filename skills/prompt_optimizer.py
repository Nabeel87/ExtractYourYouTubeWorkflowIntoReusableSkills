from pydantic import BaseModel

class OptimizedContent(BaseModel):
    title: str
    description: str
    tags: list[str]
    script_outline: str

class PromptOptimizer:
    def optimize(self, title: str, niche: str) -> OptimizedContent:
        """
        Generates full package details: Script, SEO, Tags.
        """

        script = f"""
        [INTRO - 0:00-0:45]
        Hook: "They said this heap of rust would never drive again."
        Visual: Drone shot of barn.
        Narrator: "But today, we're not just fixing it. We're rebuilding every single bolt."

        [PART 1: THE TEARDOWN - 0:45-3:00]
        - Removing the engine (struggle with stuck bolts).
        - Finding the mouse nest in the upholstery.
        - The "Point of No Return".

        [PART 2: MECHANICAL & ELECTRICAL - 3:00-7:00]
        - Engine rebuild timelapse.
        - Wiring harness nightmare (show diagram vs reality).
        - First start attempt (fail, then success).

        [PART 3: BODY & PAINT - 7:00-10:00]
        - Sandblasting (satisfying ASMR).
        - Painting (spray gun POV).

        [OUTRO - 10:00-11:30]
        - The Reveal Montage.
        - Drive-off into sunset.
        - Call to Action: "Subscribe to see the next wreck!"
        """

        return OptimizedContent(
            title=f"Restoring A {niche} - DEAD to NEW in 15 Minutes!",
            description=f"Watch the full restoration process of this abandoned {niche}. From mechanical engine rebuild to electrical wiring and fresh paint. \n\n#restoration #carbuild #diy",
            tags=["car restoration", "barn find", "restoration videos", "mechanic", "auto body", "engine rebuild"],
            script_outline=script
        )
