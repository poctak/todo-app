import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a todo")
input_box = sg.InputText('Enter todo')
add_button = sg.Button('Add')

window = sg.Window("Moje aplikace",layout=[[label],[ input_box, add_button ]])
window.read()
window.close()
