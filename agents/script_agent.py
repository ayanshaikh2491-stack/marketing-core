from ai_client import generate

SYSTEM = """
You are a Senior Video Script Writer with 15+ years in high-conversion short-form video scripting.
"""

def run(task: str) -> str:
    prompt = f"""
Write a short-form video script for:

{task}

Include:
- Strong opening hook
- Emotional trigger
- Problem-solution
- Clear CTA
Keep it natural and persuasive.
"""
    return generate(SYSTEM, prompt)
