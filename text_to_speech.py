import pyttsx3

class TextToSpeech():
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id) # español 0, inglés 1

    # Class Methods
    
    # Speak the text
    def speak(self, text, lenguaje=1):
        self.engine.setProperty('voice', self.engine.getProperty('voices')[lenguaje].id) # español 0, inglés 1
        self.engine.say(text)
        self.engine.runAndWait()

    # Save the text to a file
    def save_to_file(self, text, filename):
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
