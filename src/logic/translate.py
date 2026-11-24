from ollama import AsyncClient, Message, ChatResponse, Options  #type: ignore




MODEL = "hf.co/Menterium/translategemma-4b-it-GGUF:Q4_K_M"



MODEL_8 = "hf.co/Menterium/translategemma-4b-it-GGUF:Q8_0"


client = AsyncClient()

PROMPT: str = """
Translate from English to natural Spanish.
Preserve the meaning, tone and technical terminology.
Return only the translated text.
No explanations, alternatives or extra comments.
"""

async def translate_text(text: str) -> str:
    messages: list[Message] = [
        Message(
            role="user",
            content=f"{PROMPT}\n\n{text}"
        )
    ]

    response: ChatResponse = await client.chat ( # type: ignore  
        model=MODEL_8,
        messages=messages,
            options=Options(
            temperature=0.1
        ),
        stream=False
    ) 

    result = response.message.content
    return result if result else "" 