from ai_client import generate

SYSTEM = """
You are a Senior Video Retention Specialist with 15+ years of content performance expertise.
"""

def run(task):

    prompt = f"""
Video Review:
{task}

Evaluate:
Hook strength
Retention
Engagement triggers
Conversion potential
"""

    return generate(SYSTEM, prompt)
