from ai_client import generate

SYSTEM = """
You are a Senior Social Media Growth Analyst with 15+ years experience in organic reach optimization.
"""

def run(task: str) -> str:
    prompt = f"""
Generate optimized hashtags for:

{task}

Provide:
- High reach hashtags
- Niche targeted hashtags
- Medium competition hashtags
- 30 total hashtags grouped properly
"""
    return generate(SYSTEM, prompt)
