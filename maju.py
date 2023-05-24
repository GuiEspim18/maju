from typing import *
import speech_recognition as sr
import pyttsx3
from maju_skills import MajuSkills
import os
import winsound

class Maju:

    # Init Maju class
    def __init__(self) -> None:
        self.audio: sr.Recognizer = sr.Recognizer()
        self.machine: Any | pyttsx3.Engine = pyttsx3.init()
        self.skills: MajuSkills = MajuSkills()

        # Initing maju
        self.machine.say("Olá, eu sou a Maju!")
        self.machine.runAndWait()
    
    # Get what user said and put it into a conditional
    def voice_user_command(self) -> None:
        command: str = self.listen()
        while "tchau" not in command:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Penssando...")
            if 'horas' in command:
                self.skills.hours(command)
            if 'piada' in command:
                self.skills.joke()
            if 'converter' in command:
                self.skills.convert(command)
            if 'abrir' in command:
                pass
            command: str = self.listen()
        self.skills.goodBye()

    # Listening what user is saying
    def listen(self) -> str:
        command: Literal[""] = ""
        with sr.Microphone() as source:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Aguardando...")
            voice: sr.AudioData = self.audio.listen(source)
            command: str = self.audio.recognize_google(voice, language="pt-BR")
            command: str = command.lower()
            print(command)
            if len(command) and len(command) > 0:
                print("Ouvindo...")
                if 'maju' in command: 
                    print("Pensando...")
                    winsound.Beep(1000, 600)
                    voice: sr.AudioData = self.audio.listen(source)
                    newCommand: str = self.audio.recognize_google(voice, language="pt-BR")
                    newCommand: str = newCommand.lower()
                    if len(newCommand) and len(command) > 0:
                        print(newCommand)
                        return newCommand
                    else: self.listen()
                else: self.listen()
            else:
                self.listen()
        self.listen()

            

Maju().voice_user_command()