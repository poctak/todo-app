import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a todo")
input_box = sg.InputText('Enter todo', key='todo')
add_button = sg.Button('Add')

window = sg.Window("Moje aplikace",
                   layout=[[label],[ input_box, add_button ]],
                   font=("Helvetica",20))
event, values=window.read()
print(event)
print(values)

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo= values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos_arg=todos)

        case sg.WINDOW_CLOSED:
            break

window.close()
