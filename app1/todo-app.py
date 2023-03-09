from app1.modules.functions import get_todos, write_todos
import time

new=time.strftime("%D , %Y - %H:%M:%S")
print(new)

while True:
    user_action = input("Type add or show or edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        """file=open('files/subfiles/todos.txt', 'w')
        file.writelines(todos)
        file.close()"""

        # BETTER VERSION WITHOUT CLOSING

        write_todos(todos, 'files/subfiles/todos.txt')

    elif user_action.startswith("show"):

        todos = get_todos('files/subfiles/todos.txt')

        """new_todos=[] #making list without backslash
        for item in todos:
            new_item=item.strip('\n')
            new_todos.append(new_item)"""

        new_todos = [item.strip('\n') for item in todos]  # better version for last block code

        for index, item in enumerate(new_todos):
            # item=item.strip('\n'')     #3th version
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, 'files/subfiles/todos.txt')


        except ValueError:
            print("Your command is not valid.")
            continue  # ignore all under and start again while loop

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, 'files/subfiles/todos.txt')

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("You need to write a number after word 'complete'.")
            continue

    else:
        print("You entered an unknown command")
