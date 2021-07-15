from config.app import App
import speech_recognition as sr
import os
class Jay:
    def __init__(self):
        config = App()
        self.base_url = config.scripts

    def AbrirEdge(self):
        os.system(self.base_url + 'abriredge.bat')

    def DesligarComputador(self):
        os.system(self.base_url + 'desligar.bat')

    def EscreverUmTxt(self, Escrita):
        with open('Teste.txt', 'w') as arquivo:
            arquivo.write(Escrita)
            print("Foi escrito: " + Escrita)


    def Ouvir(self):
        mic = sr.Recognizer()
        with sr.Microphone() as source:
            audio = mic.listen(source)
        return audio

