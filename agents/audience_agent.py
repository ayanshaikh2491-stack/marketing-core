from ai_client import generate

SYSTEM = """
You are a Senior Market Segmentation Expert with 15+ years of consumer behavior experience.
"""

def run(task: str) -> str:
    prompt = f"""
Define target audience for:

{task}

Include:
- Age
- Gender
- Interests
- Pain points
- Buying behavior
- Platform preference
"""
    return generate(SYSTEM, prompt)
