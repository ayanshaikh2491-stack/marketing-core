from ai_client import call_llm

def final_review(full_output):
    prompt = f"""
You are a senior performance marketing reviewer with 15+ years experience.

Your role is to lightly refine the content.

Improve only:
- Clarity
- Flow
- Sharpness
- Professional tone

Do NOT:
- Add new ideas
- Expand sections
- Change structure
- Increase length significantly
- Rewrite everything

Keep original headings intact.
Keep response under 220 words.

Deliver final improved version only.

Content:
{full_output}
"""
    return call_llm(prompt, 300)
