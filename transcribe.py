from pytubefix import YouTube
import warnings
from pydub import AudioSegment
import io
from transformers import pipeline

def write_file(text: str, terminalPrint:bool = False):

    # Write the transcribed text to the file
    with open("assets\\transcribe.txt","a") as file:
        file.write(text)
    
    if terminalPrint:
        print(text)

def yt_download(vid: str):

    # Downloading yt audio
    yt = YouTube(vid)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path="assets",filename="test.mp4")
    
    # Converting the audio file to .wav
    audio = AudioSegment.from_file("assets\\test.mp4", format="mp4")
    audio.export("assets\\test.wav", format="wav")

def transcribe():

    model_name = "openai/whisper-base"
    transcriber = pipeline("automatic-speech-recognition", model=model_name)

    result = transcriber("assets\\test.wav", return_timestamps=True)

    return (result['text'])

def main():
    vid = "https://www.youtube.com/watch?v=AmihOKWM62I"
    yt_download(vid)
    write_file(text=transcribe(),terminalPrint=True)

if __name__ == "__main__":
    main()