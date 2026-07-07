file = open("todo.txt","w")

file.write("practice python basics\n")
file.write("learn new logic errors\n")
file.write("learn new english word\n")
file.close()

file = open("todo.txt","r")
for line in file:
    print(line.strip())
file.close()