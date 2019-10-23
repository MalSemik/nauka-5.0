import PySimpleGUI as sg

layout = [  [sg.Button('1', key="1"),sg.Button('2', key="2"),sg.Button('3', key="3")],
            [sg.Button('4', key="4"),sg.Button('5', key="5"),sg.Button('6', key="6")],
            [sg.Button('7', key="7"),sg.Button('8', key="8"),sg.Button('9', key="9")],
            [sg.Button('0', key="0"),sg.Button('+', key="+"),sg.Button('-', key="-")],
            [sg.Button('*', key="*"),sg.Button('/', key="/"),sg.Button('=', key="=")],
            [sg.Input(key="input")]]


# Create the Window
window = sg.Window('My calculator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event,values)
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break

window.close()