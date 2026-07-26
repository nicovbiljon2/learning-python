filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)

usernames = ['the blueman', 'sorted hedgehog', 'infinite lagoon']

for username in usernames:
    username = username.replace(" ", "_")
    print(username)

# append values
seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)
print(seconds)

# Tuple
color_codes = (("red", "green", "blue"), ("#3245", "#4786", "#5698"), (255, 255, 255))
print(color_codes)

# Enumerate function and f string
filenames = ['document', 'report', 'presentation']

for index, filename in enumerate(filenames):
    print(f"{index}-{filename.capitalize()}.txt")