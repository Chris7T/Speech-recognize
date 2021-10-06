import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import librosa
#from pydub import AudioSegment

# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile

from tkinter import *
import time

class Application:
    def __init__(self, master=None):

        self.audioGravado='hello.mp3'
        self.audioGravadoWMA= 'hello.wav'

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Software de áudio")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Gravar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.ouvir_microfone
        self.autenticar.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Reproduzir"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.reproduzir
        self.autenticar.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Espectograma"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.espectograma
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.mensagemAlert = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagemAlert.pack()

    # Função para ouvir e reconhecer a fala
    def ouvir_microfone(self):

        # Frase para o usuario dizer algo
        #self.mensagem["text"] = ""
        #self.mensagemAlert["text"] = "Pode falar, estou ouvindo..."


        # Habilita o microfone do usuário
        microfone = sr.Recognizer()

        # usando o microfone
        with sr.Microphone() as source:

            # Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)

            # Armazena o que foi dito numa variavel
            audio = microfone.listen(source, timeout=0, phrase_time_limit=10)

        try:
            #self.mensagemAlert["text"] = "Ok, processando..."

            # Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio, language='pt-BR')

            # Retorna a frase pronunciada

            self.mensagem["text"] = "Você disse: '" + frase + "'"
            self.cria_audio(frase)

        # Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnkownValueError:
            self.mensagemAlert["text"] = "Não entendi o que disse!"

    def cria_audio(self,frase):
        tts = gTTS(frase,lang='pt-br')
        #Salva o arquivo de audio
        tts.save(self.audioGravado)
        self.mensagemAlert["text"] = "Áudio gravado!"
        #self.convertWav(self.audioGravado)

    def reproduzir(self):
        # Da play ao audio
        #self.mensagemAlert["text"] = "Reproduzindo..."
        playsound(self.audioGravado)

    def convertWav(self,audioMp3):
        y, sr = librosa.load(audioMp3)
        data = librosa.resample(y, sr, SAMPLE_RATE)
        librosa.output.write_wav(self.audioGravadoWMA, data, SAMPLE_RATE)
        d, sr = sf.read(self.audioGravadoWMA)
        sf.write(self.audioGravadoWMA, d, sr)
        return self.audioGravadoWMA

    def espectograma(self):

        Fs, aud = wavfile.read(self.audioGravadoWMA)
        # select left channel only
        #aud = aud[:,0]
        # trim the first 125 seconds
        first = aud[:int(Fs * 125)]
        powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
        plt.show()

root = Tk()
Application(root)
root.mainloop()