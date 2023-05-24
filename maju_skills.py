import datetime
from pyttsx3 import Engine
import random
from utils.jokes import jokes
from utils.bye_message import bye
from utils.hours import hours
import requests
import urllib3
from typing import *
from maju_speak import MajuSpeak
from maju_statements import MajuStatements

class MajuSkills:

    # Initting the MajuSkills class
    def __init__(self) -> None:
        self.jokes: list[str] = jokes
        self.bye: list[str] = bye
        self.hoursSpeak: list[str] = hours

        # maju classes
        self.maju = MajuSpeak()
        self.statements = MajuStatements()

        # Disabling the warings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Getting the current hours
    def hours(self, command) -> None:
        hour: str = datetime.datetime.now().strftime('%H:%M')
        speak: str = random.choice(self.hoursSpeak)
        statement = f"{speak} {hour}"
        print(f"Maju: {statement}")
        self.statements.hours(command)
        self.maju.speak_out(statement)

    # Getting a random joke
    def joke(self) -> None:
        jokes: list[str] = self.jokes
        joke: str = random.choice(jokes)
        print(f"Maju: {joke}")
        self.maju.speak_out(joke)

    # Getting a random good bye message and saying good bye
    def goodBye(self) -> None:
        bye: list[str] = self.bye
        random_bye: str = random.choice(bye)
        self.maju.speak_out(random_bye)

    # Getting the request to convert foreing currency in reais
    def convert(self, command) -> None:
        link: str = "https://economia.awesomeapi.com.br/all/"
        if ("dólar" in command) or ("dolar" in command):
            link += "USD-BRL" 
            result = requests.get(link, verify=False)
            price: Any = result.json()
            statement: str = f"Hoje o dólar está valendo R$:{price['USD']['bid'][:4]}"
            print(f"Maju: {statement}")
            statement = statement.replace("R$", "")
            statement += "reais"
            self.maju.speak_out(statement)
        if "euro" in command:
            link += "EUR-BRL" 
            result = requests.get(link, verify=False)
            price: Any = result.json()
            statement: str = f"Hoje o euro está valendo R$:{price['EUR']['bid'][:4]}"
            print(f"Maju: {statement}")
            statement = statement.replace("R$", "")
            statement += "reais"
            self.maju.speak_out(statement)

    # Open something on web
    def open(self) -> None:
        pass