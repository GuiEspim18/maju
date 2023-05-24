import spacy
from typing import *

class MajuStatements:

    def __init__(self) -> None:
        self.nlp = spacy.load("pt_core_news_sm")

    def hours(self, command) -> None:
        # Frase de exemplo
        statement = command

        # Processar a frase
        doc = self.nlp(statement)

        for token in doc:
            print(token, token.pos_)