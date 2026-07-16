from transformers import pipeline

summarizer = pipeline("summarization", model="google/flan-t5-small")

def summarize_text(text: str, max_words: int = 60) -> str:
    """
    Generate a concise summary of the input text.
    """
    if not text.strip():
        return "No content to summarize."

    max_input_length = 1000
    text = text[:max_input_length]

    try:
        result = summarizer(
            text,
            max_length=max_words,
            min_length=25,
            do_sample=False
        )
        if result and isinstance(result, list) and len(result) > 0:
            if "summary_text" in result[0]:
                return result[0]["summary_text"].strip()
            else:
                print(f"Unexpected result format: {result}")
                return text[:200] + "..."
        else:
            print(f"Empty or invalid result: {result}")
            return text[:200] + "..."
    except Exception as e:
        print(f"Summarization error: {e}")
        return text[:200] + "..."
