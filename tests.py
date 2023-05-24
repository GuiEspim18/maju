# from maju_skills import MajuSkills
# from maju_statements import MajuStatements

# MajuStatements().hours("Que horas são?")

import spacy

# Carregar o modelo do Spacy
nlp = spacy.load("pt_core_news_sm")

# Frases de exemplo
frases = [
    "Que horas são?",
    "Você pode me dizer as horas?",
    "Você sabe que horas são agora?",
    "Pode me informar que horas são, por favor?",
    "Estou curioso(a), poderia me dizer que horas são?",
    "Gostaria de saber que horas são neste momento.",
    "Preciso saber as horas, poderia me ajudar?",
    "Estou perdido(a) no tempo, pode me dizer que horas são?"
]

# Iterar pelas frases e realizar a interpretação
for frase in frases:
    doc = nlp(frase)
    
    # Identificar os tokens relevantes
    for token in doc:
        if token.text.lower() == "horas":
            print("Encontrada a palavra 'horas' na frase:", frase)
            break
    
    # Identificar o tipo de pergunta (se for uma pergunta)
    if doc[-1].text == "?":
        print("A frase é uma pergunta.")
    
    print("---")



# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://google.com/search?q=o+que+são+cachorros")
# soup = BeautifulSoup(page.content, "html.parser")

# print(soup)

"""
import spacy

# Frase de exemplo
statement = "quais as horas?"

# Carregar o modelo pré-treinado do spaCy para a língua desejada
nlp = spacy.load("pt_core_news_sm")

# Processar a frase
doc = nlp(statement)

# Extrair o termo de pesquisa (substantivo mais relevante)
search = ""
for token in doc:
    print(token, token.pos_)
    if token.pos_ == "NOUN":
        search += f" {token.text}"

search = search[1:]

print(search)
"""

