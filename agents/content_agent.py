from ai_client import generate

SYSTEM = """
You are a Senior Content Strategist with 15+ years experience in brand storytelling and conversion content.
You write persuasive, platform-optimized, high-retention content.
"""

def run(task: str) -> str:
    prompt = f"""
Create high-conversion social media content for:

{task}

Provide:
- Hook (scroll-stopping)
- Main body (value-driven)
- CTA (conversion-focused)
- Tone variation option
"""
    return generate(SYSTEM, prompt)
