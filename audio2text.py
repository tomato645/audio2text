import streamlit as st
from audiorecorder import audiorecorder
import whisper

st.title("Audio to text")
audio = audiorecorder("Click to record", "Click to stop recording")

def transcribe():
    model = whisper.load_model("base")
    result = model.transcribe("audio.wav")
    text = result["text"]
    print(text)
    textarea = st.text_area("text", text)

if not audio.empty():
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")

    transcribe()