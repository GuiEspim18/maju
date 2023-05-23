import datetime
from pyttsx3 import Engine
import random
from utils.jokes import jokes
from utils.bye_message import bye

class MajuSkills:
    def __init__(self, machine) -> None:
        self.machine: Engine = machine
        self.jokes = jokes
        self.bye = bye

    def hours(self) -> None:
        hour = datetime.datetime.now().strftime('%H:%M')
        print(f"Maju: Agora são {hour}")
        self.machine.say(f"Agora são {hour}")
        self.machine.runAndWait()

    def joke(self) -> None:
        jokes: list[str] = self.jokes
        joke = random.choice(jokes)
        print(f"Maju: {joke}")
        self.machine.say(joke)
        self.machine.runAndWait()

    def goodBye(self) -> None:
        bye: list[str] = self.bye
        random_bye = random.choice(bye)
        self.machine.say(random_bye)
        self.machine.runAndWait()