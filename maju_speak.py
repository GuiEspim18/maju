import pyttsx3
from typing import *

class MajuSpeak:

    def __init__(self) -> None:
        self.machine: Any | pyttsx3.Engine = pyttsx3.init()

    def speak_out(self, statement) -> None:
        self.machine.say(statement)
        self.machine.runAndWait()