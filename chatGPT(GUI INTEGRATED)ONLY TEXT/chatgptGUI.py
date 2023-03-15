import PySimpleGUI as sg
import openai
openai.api_key = "****CHATGPT API KEY*****"
layout = [[sg.Text('CHAT GPT FOR DESKTOP')],
        [sg.InputText()],
        [sg.Submit(key='-SUB-'), sg.Cancel(key='-EX-')],
        [sg.Text('RESULT:', key='-OUT-')]]
window = sg.Window('CHATGPT DE', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-EX-':
        break
    if event == '-SUB-':
        texto = values[0]
        completion = openai.Completion.create(engine="text-davinci-003", prompt=texto, max_tokens=3500)
        result = completion.choices[0].text
        sg.popup('RESULT:  ', result)
window.close()

