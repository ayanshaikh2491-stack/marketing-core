from ai_client import generate

SYSTEM = """
You are a Senior Visual Conversion Analyst with 15+ years of branding experience.
"""

def run(task):

    prompt = f"""
Image Review:
{task}

Evaluate:
Attention power
Emotional trigger
Brand strength
Improvement advice
"""

    return generate(SYSTEM, prompt)
