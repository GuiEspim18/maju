from typing import *
import speech_recognition as sr
import pyttsx3
from maju_skills import MajuSkills
import os


class Maju:

    # Init Maju class
    def __init__(self) -> None:
        self.audio: sr.Recognizer = sr.Recognizer()
        self.machine: Any | pyttsx3.Engine = pyttsx3.init()
        self.machine.say("Olá, eu sou a Maju!")
        self.machine.runAndWait()
        self.skills: MajuSkills = MajuSkills(self.machine)

    # Run the command to listem user
    def run_command(self) -> Any:
        try:
            command = self.listen()
        except:
            self.listen()
        return command
    
    # Get what user said and put it into a conditional
    def voice_user_command(self) -> None:
        command: str = self.run_command()
        while "tchau" not in command:
            if 'horas' in command:
                self.skills.hours()
            if 'piada' in command:
                self.skills.joke()
            command = self.run_command()
        self.skills.goodBye()

    # Listening what user is saying
    def listen(self) -> str:
        command = ""
        with sr.Microphone() as source:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ouvindo...")
            voice = self.audio.listen(source)
            command: str = self.audio.recognize_google(voice, language="pt-BR")
            command = command.lower()
            if len(command):
                if 'maju' in command: command = command.replace("maju", "")
                return command
            else:
                self.listen()

            

Maju().voice_user_command()