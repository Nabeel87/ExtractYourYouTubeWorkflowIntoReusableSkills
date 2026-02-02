from pydantic import BaseModel, Field
from typing import List

class Topic(BaseModel):
    title: str = Field(..., description="Clickbait title")
    hook: str = Field(..., description="First 5 seconds verbal/visual hook")
    viral_factor: str = Field(..., description="Why this will go viral")

class TopicGeneratorSkill:
    def generate(self, niche_name: str, count: int = 3) -> List[Topic]:
        """
        Generates viral video topics for a specific niche.
        """
        print(f"Generating topics for niche: {niche_name}...")

        if "Restoration" in niche_name:
            return [
                Topic(
                    title=f"I Bought The Cheapest {niche_name} On Marketplace!",
                    hook="Show the car looking terrible, then flash '50 year old receipt'.",
                    viral_factor="Mystery + Price anchor"
                ),
                Topic(
                    title=f"Will It Run after 40 Years? {niche_name}",
                    hook="Key turning sound... silence... then a cough.",
                    viral_factor="High stakes tension"
                ),
                Topic(
                    title=f"Complete {niche_name} Timelapse (1000 Hours in 10 Mins)",
                    hook="Fast forward rust melting away.",
                    viral_factor="Process satisfaction (ASMR)"
                )
            ]

        # Generic fallback
        return [
            Topic(
                title=f"The Ultimate Guide to {niche_name}",
                hook="Did you know 90% of people fail at this?",
                viral_factor="Curiosity gap"
            )
        ]

if __name__ == "__main__":
    skill = TopicGeneratorSkill()
    topics = skill.generate("Full Barn Find Restoration")
    for t in topics:
        print(f"- {t.title}")
