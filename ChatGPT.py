import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai 
openai.api_key = OPENAI_KEY 

def fala_texto(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

def grava_texto():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print('Estou escutando')
                audio2 = r.listen(source2)
                meu_texto = r.recognize_google(audio2)
                return meu_texto
        except sr.RequestError as e:
            print("Não foi possível solicitar resultados; {0}".format(e))
        except sr.UnknownValueError:
            print("Erro desconhecido")
    
def mandar_chatGPT(messages, model="gpt-3.5-turbo"):
    
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    
    mensagem = response.choices[0].mensagem.content
    mensagens.append(response.choices[0].mensagem)
    return mensagem


mensagens = [{"role": "user", "content": "Por favor, aja como o Jarvis do Homem de Ferro."}]
while(1):
    text = grava_texto()
    mensagens.append({"role": "user", "content": text})
    response = mandar_chatGPT(mensagens)
    fala_texto(response) 
    
    print(response)