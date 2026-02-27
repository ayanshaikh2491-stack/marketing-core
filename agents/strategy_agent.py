from ai_client import generate

SYSTEM = """
You are a Senior Growth Strategist with 15+ years scaling brands.
You design execution-level growth plans.
"""

def run(task):

    prompt = f"""
Strategy Plan:
{task}

Provide:
Positioning
Growth lever
Content roadmap
Monetization structure
Execution steps
"""

    return generate(SYSTEM, prompt)
