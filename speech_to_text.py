from transformers import pipeline
from pydub import AudioSegment
import tempfile
import os

asr = pipeline("automatic-speech-recognition", model="openai/whisper-medium", device=-1)

def convert_audio_to_wav(input_file):
    audio = AudioSegment.from_file(input_file)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        audio.export(temp_wav.name, format="wav")
        return temp_wav.name

def transcribe_audio_hf(file_path):
    print("🔊 Converting and transcribing audio...")
    wav_path = convert_audio_to_wav(file_path)
    result = asr(wav_path)
    text = result['text'].strip()
    print(f"🗣 Transcribed text: {text}")
    os.remove(wav_path)
    return text
