from classes.Jay import *
from os import linesep
import speech_recognition as sr

print("OLÁ, MEU NOME É JAY! SOU SUA ASSISTENTE VIRTUAL", linesep)
print("EU POSSO TOMAR CONTA DO SEU SISTEMA OPERACIONAL!, ABRIR ARQUIVOS, PROGRAMAS, ESCREVER EM ARQUIVOS E ETC!", linesep)

count = True
Assistente = Jay()
mic = sr.Recognizer()
try:
    while count:
        print("DIGA, NO QUE POSSO TE AJUDAR?")
        audio = Assistente.Ouvir()
        resposta = mic.recognize_google(audio, language="pt-BR")

        if resposta == "Abrir navegador":
            Assistente.AbrirEdge()
        elif resposta == "desligar" or resposta == "desligar computador":
            Assistente.DesligarComputador()

        print("precisa de mais alguma coisa?")
        final = Assistente.Ouvir()
        resposta2 = mic.recognize_google(final, language="pt-BR")

        if resposta2 == "não":
            print("Foi um prazer ajudar :) , Espero ver você de novo!")
            count = False

except sr.UnknownValueError:
    print("DESCULPE NÃO OUVI!")