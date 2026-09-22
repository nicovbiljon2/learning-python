# while True:
#    print("Hello")

numbers = [1,2,3]

doubled = [num*2 for num in numbers]
print(doubled)

names = ["one.doc", "two.doc"]
new_names = [name.replace(".doc", "") + ".txt" for name in names]
print(new_names[0])

user_prompt = "Enter a todo: "

todos = []
while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)



