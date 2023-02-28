import tkinter as tk
import pyttsx3
import speech_recognition as sr
from tkinter import ttk

class TextToSpeech:
    def __init__(self):
        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

        # Set default values for voice and speed
        self.voice_index = 0
        self.speed = 150

        # Initialize the speech recognition engine
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def say(self, text):
        # Set the voice and speed for the engine
        self.engine.setProperty('voice', self.voices[self.voice_index].id)
        self.engine.setProperty('rate', self.speed)

        # Speak the text
        self.engine.say(text)
        self.engine.runAndWait()

    def recognize_speech(self):
        # Listen for spoken words and convert to text
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"


def play_text():
    # Get the text from the input box
    text = input_box.get("1.0", tk.END).strip()

    # Play the text
    tts_engine.say(text)


def select_voice(event):
    # Get the index of the selected voice
    voice_name = voice_dropdown.get()
    voice_index = [i for i, voice in enumerate(tts_engine.voices) if voice.name == voice_name][0]

    # Set the index of the selected voice
    tts_engine.voice_index = voice_index


def set_speed(speed):
    # Set the speed for the text-to-speech engine
    tts_engine.speed = speed


def toggle_speech_recognition():
    # Toggle speech recognition on/off
    if speech_recognition_checkbox_var.get():
        speech_text = tts_engine.recognize_speech()
        input_box.delete("1.0", tk.END)
        input_box.insert(tk.END, speech_text)
        speech_recognition_checkbox.deselect()


# Create the main window
window = tk.Tk()
window.title("Text-to-Speech")

# Create the text-to-speech engine and initialize the speech recognition engine
tts_engine = TextToSpeech()

# Create the input box, "Play" button, and speed slider
input_box = tk.Text(window, height=10, width=50)
play_button = tk.Button(window, text="Play", command=play_text)
speed_slider = tk.Scale(window, from_=50, to=200, orient=tk.HORIZONTAL, command=set_speed)

# Create the voice dropdown and set the default value
voice_names = [voice.name for voice in tts_engine.voices]
voice_dropdown = ttk.Combobox(window, values=voice_names)
voice_dropdown.current(tts_engine.voice_index)
voice_dropdown.bind("<<ComboboxSelected>>", select_voice)

# Create the speech recognition checkbox and variable
speech_recognition_checkbox_var = tk.BooleanVar()
speech_recognition_checkbox = tk.Checkbutton(window, text="Speech Recognition", variable=speech_recognition_checkbox_var, command=toggle_speech_recognition)

# Add the input box, "Play" button, speed slider, voice dropdown, and speech recognition checkbox to the window
input_box.pack(pady=10)
play_button.pack(pady=10)
speed_slider.pack(pady=10)
voice_dropdown.pack(pady=10)
speech_recognition_checkbox.pack(pady=10)

window.mainloop()
