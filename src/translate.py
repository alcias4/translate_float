from ollama import chat , Client #type: ignore




MODEL = "hf.co/Menterium/translategemma-4b-it-GGUF:Q4_K_M"



MODEL_8 = "hf.co/Menterium/translategemma-4b-it-GGUF:Q8_0"

def translate_text(text: str) -> str:
    response = chat(
    model=MODEL_8,
    messages=[
        {
            "role": "user",
            "content": (
                "Translate this sentence into natural Spanish. "
                "Return only the translation: "
                f"{text}"
            ),
        }
        ],
    )

    result = response.message.content
    return result if result else "Error" 