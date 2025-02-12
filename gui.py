import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a todo")
input_box = sg.InputText('Enter todo')
buttonOk = sg.Button('Add')

window = sg.Window("Moje aplikace",layout=[[label],[ input_box, buttonOk ]])
window.read()
window.close()
