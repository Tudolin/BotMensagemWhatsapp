import pywhatkit
import keyboard
import time
from datetime import datetime

#Lista de contatos
contatos = ['+5541123456789','...']

#Intervalo de envio
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'-INSIRA AQUI SUA MENSAGEM-',datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
    