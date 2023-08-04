import csv

with open("code.txt", "r") as file:
    lines = file.readlines()
    f = open("results.csv", "w")

for line in lines:
    try:
        exec(line)
        with open ("results.csv", "a") as files:
            now = 1
            message = f"{now}:\n"
            print(message)
            f.write(message)
    except:
        with open ("results.csv", "a") as files:
            now = 0
            message = f"{now}:\n"
            print(message)
            f.write(message)

with open ("results.csv", "a") as files:
    for i, line in enumerate (f):
        messages = (f'{i+1} : {line}'.strip()) 
        f.write(messages + "\n")
