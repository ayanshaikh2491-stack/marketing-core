from ai_client import call_llm

def research(user_input):
    prompt = f"""
You are a senior market intelligence expert with 15+ years of experience scaling local and digital brands.

First internally analyze the user request carefully.
Understand business type, market position, competition level, and intent.

Then respond in this exact format:

[MARKET REALITY]
Current industry situation (concise).

[AUDIENCE PATTERN]
Who they are, what they care about.

[COMPETITIVE SIGNAL]
What competitors are likely doing.

Rules:
- Max 150 words.
- No strategy.
- No ads.
- No motivational talk.
- Be sharp and realistic.

User Request:
{user_input}
"""
    return call_llm(prompt, 350)
