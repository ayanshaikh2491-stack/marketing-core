def clean_output(text):

    banned_phrases = [
        "as an ai",
        "i am an ai",
        "language model",
    ]

    for phrase in banned_phrases:
        text = text.replace(phrase, "")

    return text
