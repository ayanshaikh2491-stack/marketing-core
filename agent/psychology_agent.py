from ai_client import generate

SYSTEM = """
You are a Senior Consumer Psychology Strategist with 15+ years in behavioral marketing.
"""

def run(task: str) -> str:
    prompt = f"""
Analyze psychological triggers for:

{task}

Provide:
- Emotional triggers
- Cognitive biases
- Fear/desire angles
- Persuasion levers
"""
    return generate(SYSTEM, prompt)
