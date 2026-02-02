from pydantic import BaseModel, Field
from typing import List

class Niche(BaseModel):
    name: str = Field(..., description="Name of the sub-niche")
    volume_score: int = Field(..., description="Search volume score (0-100)")
    competition_score: int = Field(..., description="Competition score (0-100)")
    description: str = Field(..., description="Why this niche is good")

class NicheDiscoverySkill:
    def discover(self, topic: str) -> List[Niche]:
        """
        Simulates discovering viral sub-niches for a given topic.
        In a real implementation, this would call Google Trends / YouTube API.
        """
        print(f"Discovering niches for: {topic}...")

        # Mock logic based on keywords
        if "car" in topic.lower() or "auto" in topic.lower():
            return [
                Niche(
                    name="Deep Clean & Detail Restoration",
                    volume_score=95,
                    competition_score=60,
                    description="Highly satisfying 'oddly satisfying' content focused on cleaning."
                ),
                Niche(
                    name="Full Barn Find Restoration",
                    volume_score=90,
                    competition_score=75,
                    description="Story-driven transformations of abandoned classics."
                ),
                Niche(
                    name="Budget DIY Fixes",
                    volume_score=85,
                    competition_score=40,
                    description="Educational content for average car owners."
                ),
                 Niche(
                    name="EV Conversion of Classics",
                    volume_score=70,
                    competition_score=30,
                    description="Modern tech in old bodies, rising trend."
                )
            ]

        # Default fallback
        return [
            Niche(
                name=f"{topic} for Beginners",
                volume_score=80,
                competition_score=50,
                description="Introductory content always performs well."
            )
        ]

if __name__ == "__main__":
    skill = NicheDiscoverySkill()
    results = skill.discover("Car Restoration")
    for niche in results:
        print(f"- {niche.name} (Vol: {niche.volume_score})")
