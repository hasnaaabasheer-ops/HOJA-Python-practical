file = open("poem.txt","w")
file.write("twingle twingle little star\n")
file.write("how i wonder what you are\n ")
file.write("up above the world so high\n ")
file.write("like a diamond in the sky\n ")
file.close()

file = open("poem.txt","r")
for line in file: 
    print(line.split())
file.close()