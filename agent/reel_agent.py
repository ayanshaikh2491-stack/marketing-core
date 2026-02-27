from ai_client import generate

SYSTEM = """
You are a Senior Instagram Reel Growth Specialist with 15+ years of viral content experience.
You design reels optimized for retention and shareability.
"""

def run(task: str) -> str:
    prompt = f"""
Create a viral reel concept for:

{task}

Provide:
- Hook (first 3 seconds)
- Scene breakdown
- On-screen text
- Engagement trigger
- CTA
"""
    return generate(SYSTEM, prompt)
