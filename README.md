# WeListen

![Logo](https://cdn.discordapp.com/attachments/886689403538399303/893943580580790302/onlinelogomaker-100221-1631-5710.png)

## Instalação do WeListen

Para o funcionamento do programa é necessario a instalação de algumas ferramentas.

 [Python] - Python é a base usada para o desenvolvimento do projeto
 
 Speech Recognization é a biblioteca para realização do reconhecimento de fala.
```bash 
pip install speech_recognition
```
GTTS é a bilioteca para fazer a interface do sistema.
```bash 
pip install gtts
```
Librosa é a biblioteca para fazer analise de áudio.
```bash 
pip install librosa
```
PyAudio é a biblioteca que permite gravação e reprodução de audios.
```bash 
pip install pyAudio
```

Ou 


```bash 
pip install pipwin
```
```bash 
pipwin  install pyaudio
```



## Funcionamento do WeListen

Uma interface básica foi usada para simplificar a vida do usuário, nela possui 3 botões, sendo eles ``Gravar``, ``Reproduzir`` e ``Espectograma``

![Imagem1](https://cdn.discordapp.com/attachments/882037274328580126/893951372792299520/unknown.png) {.centerAlign}

## Funcionalidades
- ``Gravar`` 
    Nesta opção, após pressionado, irá reconhecer o microfone do usuário e gravar o que foi dito em um arquivo local e também será exibido a mensagem.

![Imagem2](https://cdn.discordapp.com/attachments/882037274328580126/893954156715474974/unknown.png)

- ``Reproduzir``
    Nesta opção, após pressionado, irá pegar o arquivo de audio salvo anteriormente e fará uma reprodução.

- ``Espectograma``
    Nesta opção, após pressionado, irá pegar o arquivo de audio salvo anteriormente e será feito uma analise e então irá ser exibidor o espectograma

![Imagem3](https://cdn.discordapp.com/attachments/886689403538399303/893952341617823814/e62d32d6-fc63-413c-ac1b-9e65d0d94550.png)

 [Python]: <https://www.python.org/downloads/>

 