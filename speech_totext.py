import speech_recognition as sr
from moviepy.editor import AudioFileClip
from io import BytesIO
from pydub import AudioSegment

class Speech_ToText():
    def __init__(self) -> None:
        self.r = sr.Recognizer()
        self.string = "a"


    def speech_recognition1(self,file):
        audio_clip = AudioFileClip(file)
        audio_clip.write_audiofile("small.wav")

        with sr.AudioFile("small.wav") as source:
            audio = self.r.record(source)

        try:
            text = self.r.recognize_google(audio, language='en-US') 
            self.string = text
            return self

        except sr.UnknownValueError:
            self.string = "No te entenndi mijo"
            return self

        except sr.RequestError as e:
            self.string = f"Error en la solicitud: {e}"
            return self


    def live_recognition(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.r.listen(source)

        try:
            print("Recognizing...")
            text = self.r.recognize_google(audio, language='en-US')
            self.string = text
            return self

        except sr.UnknownValueError:
            self.string = "Could not understand audio"
            return self

        except sr.RequestError as e:
            self.string = f"Error in the request: {e}"
            return self 
    
