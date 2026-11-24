#### app


require :
# for windows 
0. irm https://ollama.com/install.ps1 | iex 
# linux or mac
1. curl -fsSL https://ollama.com/install.sh | sh
2. ❯ ollama run hf.co/Menterium/translategemma-4b-it-GGUF:Q8_0

## for wayland 
3. sudo pacman -S wl-clipboard
4. sudo pacman -S espeak-ng 

# create executable 

flet pack src/main.py \
    --name Translator_camilo \
    --add-data "src/assets:assets" \
    --yes \
    -- --paths . --clean

uv run flet pack src/main.py \
    --name Translator_camilo \
    --onedir \
    --add-data "src/assets:assets" \
    --yes \
    -- --paths src \
    --collect-all language_tags \
    --collect-all misaki \
    --collect-all phonemizer \
    --collect-all segments \
    --collect-all csvw \
    --collect-all kokoro \
    --collect-all en_core_web_sm \
    --copy-metadata en-core-web-sm \
    --log-level INFO

## 2. parts

1. mkdir -p dist/Translator_camilo/_internal/espeakng_loader
2. cp -a .venv/lib/python3.15/site-packages/espeakng_loader/. \
    dist/Translator_camilo/_internal/espeakng_loader/
# windows 

uv run flet pack src/main.py `
    --name Translator_camilo `
    --onedir `
    --add-data "src/assets:assets" `
    --yes `
    -- --paths src `
    --collect-all language_tags `
    --collect-all misaki `
    --collect-all phonemizer `
    --collect-all segments `
    --collect-all csvw `
    --collect-all kokoro `
    --collect-all espeakng_loader `
    --collect-all en_core_web_sm `
    --copy-metadata en-core-web-sm `
    --log-level INFO