import os
import PySimpleGUI as sg
import pyttsx3
import speech_recognition as sr
import openai
def graphic_ui():
    sg.theme("DarkPurple1")
    layout = [[sg.Button("HABLAR", key="-SP-")],
              [sg.Button("ESCRIBIR", key="-WR-")],
              [sg.Button("CERRAR", key="-OK-")]]
    window = sg.Window("ChatGPT For Desktop", layout, margins=(100, 100))
    return window
def chatgpt(text):
    openai.api_key = "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"
    completion = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=2048)
    return completion
def choice():
    choice = input("QUIERES HABLAR O ESCRIBIR?[H / E]: ")
    return choice
def recognize_voice(r):
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text
def initialise_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "spanish")
    return engine
def main():
    engine = initialise_engine()
    while True:
        if choice() == "H":
            engine.say("Hola, ¿Qué quieres saber?")
            engine.runAndWait()
            r = sr.Recognizer()
            text = recognize_voice(r)
            os.system("cls")
        else:
            text = input("QUÉ QUIERES SABER?: ")
            os.system("cls")
        result = chatgpt(text).choices[0].text
        if result:
            print(result)
            engine.say(result)
        else:
            engine.say("No te he entendido")
        engine.runAndWait()
        input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
        os.system("cls")

if __name__ == "__main__":
    main()