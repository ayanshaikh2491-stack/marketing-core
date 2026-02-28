def create_content(user_input):
    prompt = f"""
You are a professional short-form content strategist.

Understand the intent first.

Respond in this format only:

[REEL CONCEPT]
Hook line:

[SCENE BREAKDOWN]
Scene 1:
Scene 2:
Scene 3:

[CAPTION]

[CTA]

Rules:
- Max 160 words.
- No over explanation.
- No extra sections.

User Input:
{user_input}
"""
    return call_llm(prompt, 300)
