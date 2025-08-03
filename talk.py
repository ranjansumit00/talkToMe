from gtts import gTTS
import os
import platform
import tempfile
import re

def speak(text):
    remove_noise=re.sub(r'[^A-Za-z0-9 ]+', '', text)
    speech = gTTS(text=remove_noise, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        speech.save(temp_path)
    system = platform.system()
    if system == "Windows":
        os.system(f'start /min {temp_path}')
    elif system == "Darwin":  # macOS
        os.system(f'afplay "{temp_path}"')
    elif system == "Linux":
        os.system(f'xdg-open "{temp_path}"')
