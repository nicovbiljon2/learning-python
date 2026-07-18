user_prompt = "Enter a todo: "

todos = [] # create an empty list

while True:
    todo = input(user_prompt)
    todos.append(todo) # append the user input to the todos list
    print(todos)

