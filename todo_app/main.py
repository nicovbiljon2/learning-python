
while True:
    # Get user input and stip space characters from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action or "new" in user_action:
        # todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:] # list slicing operation

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo) # append the user input to the todos list

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip("\n") for item in todos] # list comprehension

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.capitalize()
            row = f"{index + 1}: {item}"
            print(row)

    elif "edit" in user_action:
        # number = int(input("Enter the number of the todo to edit: "))
        number = int(user_action[5:])
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        # number = int(input("Enter the number of the todo to complete: "))
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Invalid input")

print("Goodbye!")

