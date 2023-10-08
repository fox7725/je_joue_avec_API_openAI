import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la clé API OpenAI depuis les variables d'environnement
openai_api_key = os.getenv("OPENAI_API_KEY")

# Définir la clé API OpenAI
openai.organization = os.getenv("CODE_SOCIETE")
openai.api_key = openai_api_key

role = input("Quel sera mon rôle dans cette conversation ?")
question = " "
questions = [{"role": "system", "content": role}]
while question != "q" and question != "Q":
    print(" ")
    print("tapez 'q' pour quiter")
    question = input("Je vous écoute :")
    if question == "q" or question == "Q":
        break
    content = {"role": "user", "content": question}
    questions.append(content)
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=questions
    )
    print("AI : ", response["choices"][0]["message"]["content"])
print ("AI : Merci pour cette conversation, à bientôt !")
