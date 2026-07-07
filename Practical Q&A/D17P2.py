file = open("movies.txt","w")
file.write("KGF,vazha,drishyam")
file.close()

file = open("movies.txt","r")
for line in file:
    print(line.strip())
file.close()