from kokoro import KPipeline # type: ignore
import soundfile as sf # type: ignore
from pathlib import Path



async def text_voice(text: str):

    folder = Path("src/audio")

    folder.mkdir(parents=True, exist_ok=True)

    pipeline = KPipeline(
        lang_code="a",
        device="cpu"
    )

    generator = pipeline(
        text=text,
        voice="af_heart",
        speed=0.7
    )

    paths : list[Path] = []
    for i,(text_part, phonemes, audio ) in enumerate(generator):
        print(text_part)
        print(phonemes)
        name = folder / f"audio_{i}.wav"
        sf.write(
            name,
            audio.cpu().numpy(), # type: ignore
            24000
        )

        paths.append(name)

    return paths