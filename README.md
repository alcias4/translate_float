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

# windows 

flet pack src/main.py --name Translator_camilo --add-data "src/assets:assets" --yes -- --paths . --clean