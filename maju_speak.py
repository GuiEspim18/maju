from pyttsx3 import Engine

class MajuSpeak:

    def __init__(self, machine) -> None:
        self.machine: Engine = machine

    def speak_out(self, statement) -> None:
        self.machine.say(statement)
        self.machine.runAndWait()