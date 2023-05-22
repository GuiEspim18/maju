import datetime
from pyttsx3 import Engine

class MajuSkills:
    def __init__(self, machine) -> None:
        self.machine: Engine = machine

    def hours(self):
        hour = datetime.datetime.now().strftime('%H:%M')
        print(f"Maju: Agora são {hour}")
        self.machine.say(f"Agora são {hour}")
        self.machine.runAndWait()