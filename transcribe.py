from pytubefix import YouTube
import warnings # Add ignore warnings
from pydub import AudioSegment
from transformers import pipeline

def write_file(text: str, terminalPrint:bool = False):

    '''
        text : transcribed text to store in the txt file 
        terminalPrint : Decides if the transcribed text is printed. Default : False 
    '''

    with open("assets\\transcribe.txt","a") as file:
        file.write(text)
    
    if terminalPrint:
        print(text)

def yt_download(vid: str):
    
    '''
        vid : Youtube video to download
    '''
    yt = YouTube(vid)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path="assets",filename="test.mp4")
    

    audio = AudioSegment.from_file("assets\\test.mp4", format="mp4")
    audio.export("assets\\test.wav", format="wav")

def transcribe():
    
    '''
        ASR to Transcribe the text
    '''
    
    model_name = "openai/whisper-base"
    transcriber = pipeline("automatic-speech-recognition", model=model_name)

    result = transcriber("assets\\test.wav", return_timestamps=True)

    return(result['text'])

if __name__ == "__main__":
    vid = ""
    yt_download(vid=vid)
    write_file(text=transcribe())