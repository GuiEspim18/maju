from typing import *
import speech_recognition as sr
import pyttsx3
from maju_skills import MajuSkills


class Maju:
    def __init__(self) -> None:
        self.audio: sr.Recognizer = sr.Recognizer()
        self.machine: Any | pyttsx3.Engine = pyttsx3.init()
        self.machine.say("Olá, eu sou a Maju!")
        self.machine.runAndWait()
        self.skills: MajuSkills = MajuSkills(self.machine)

    def run_command(self) -> Any:
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                voice = self.audio.listen(source)
                command: str = self.audio.recognize_google(voice, language="pt-BR")
                command = command.lower()
                if len(command):
                    if 'maju' in command: command = command.replace("maju", "")
                else: 
                    self.machine.say("Porfavor diga algo!")
        except:
            print("<ERROR> Microfone não funciona!")
            self.machine.say("Não consigo escutar você!")
            self.machine.runAndWait()

        return command
    
    def voice_user_command(self) -> None:
        command: pyttsx3.Engine = self.run_command()
        if 'horas' in command:
            self.skills.hours()

            

Maju().voice_user_command()