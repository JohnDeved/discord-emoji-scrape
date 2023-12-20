import requests
from PIL import Image
from io import BytesIO
from pathlib import Path

EMOJI_URL = 'https://discord.com/assets/f46d6b0cbeeea15ecd81.png'
EMOJI_SIZE = 24 * 2  # px

def get_emojis():
    response = requests.get(EMOJI_URL)
    img = Image.open(BytesIO(response.content))
    return [img.crop((x, y, x + EMOJI_SIZE, y + EMOJI_SIZE)) 
            for y in range(0, img.height, EMOJI_SIZE) 
            for x in range(0, img.width, EMOJI_SIZE)]

emojis = get_emojis()

# ensure emojis folder exists
Path('./emojis').mkdir(parents=True, exist_ok=True)

# Save emojis
for i, emoji in enumerate(emojis):
    # check if emoji is empty
    if emoji.getbbox():
        print(f'Saving emoji {i}')
        emoji.save(f'./emojis/{i}.png')