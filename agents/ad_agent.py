def create_ads(user_input):
    prompt = f"""
You are a senior paid advertising expert (Meta & Google).

First understand the offer deeply.

Output only:

[OFFER ANGLE]

[AD FRAMEWORK]
Hook:
Problem:
Solution:
Proof:
CTA:

[TARGETING LOGIC]
Audience type + budget direction.

Rules:
- Max 180 words.
- No long explanation.
- No repetition.

User Input:
{user_input}
"""
    return call_llm(prompt, 350)
