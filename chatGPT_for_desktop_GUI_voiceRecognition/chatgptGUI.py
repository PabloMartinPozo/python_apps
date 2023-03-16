import PySimpleGUI as sg
import openai
import pyttsx3
import speech_recognition as sr
openai.api_key = "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"
layout = [[sg.Text('CHAT GPT FOR DESKTOP')],
        [sg.InputText(key='-IN-')],
        [sg.Button('TALK', key='-TLK-')],
        [sg.Submit(key='-SUB-'), sg.Cancel(key='-EX-')]]
window = sg.Window('CHATGPT Desktop', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-EX-':
        break
    if event == '-TLK-':
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            texto = r.recognize_google(audio, language="en-EN")
        window['-IN-'].update(texto)

    if event == '-SUB-':
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("voice", "english")
        texto = values['-IN-']
        completion = openai.Completion.create(engine="text-davinci-003", prompt=texto, max_tokens=3500)
        result = completion.choices[0].text
        sg.popup('RESULT:  ', result)

    #text_input = values[0]
    #sg.popup('You entered', text_input)
window.close()

