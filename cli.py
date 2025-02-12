#from functions import get_todos, write_todos
import functions
import time
#todos=[]
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos= functions.get_todos()

        todos.append(todo + "\n" )
        functions.write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        todos= functions.get_todos()

        for index,item in enumerate(todos):
            item=item.strip("\n")
            print(f'{index+1}.{item}')
    elif user_action.startswith("edit"):
        try:
            number =int(user_action[5:])
            number=number-1

            todos=get_todos()
           # print('Here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number]=new_todo + "\n"

            write_todos(todos_arg=todos)
        except ValueError:
            print("Your command is not valid")
            continue

            # print('Here is how it will be', todos)
    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])

            todos=get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(filepath='todos.txt', todos_arg=todos)

            message =f"Todo {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")


print("Bye!")










