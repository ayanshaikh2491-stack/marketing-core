import os
from groq import Groq

client = Groq(api_key=os.getenv("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"))

def generate(system_prompt, user_prompt):

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content
