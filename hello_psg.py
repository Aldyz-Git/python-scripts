# hello_psg.py

import PySimpleGUI as sg
  
layout = [  [sg.Text('My Window')],
            [sg.Input(key="-IN-")],
            [sg.Text(key="-OUT-")],
            [sg.Button("Go")], 
            [sg.Button("Exit")] ]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event =="Exit":
        break
    if event == "Go":
        window["-OUT-"].update(values["-IN-"])

window.close()