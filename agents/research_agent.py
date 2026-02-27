from ai_client import generate

SYSTEM = """
You are a Senior Market Intelligence Consultant with 15+ years of global growth experience.
You provide deep commercial insights, not generic information.
"""

def run(task):

    prompt = f"""
Research Requirement:
{task}

Provide:
Market gap
Competitor weakness
Revenue angle
Hidden risk
Opportunity leverage
"""

    return generate(SYSTEM, prompt)
