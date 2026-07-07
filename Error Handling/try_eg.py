try:
    with open("unkown.txt","r")as file:
        data=file.read()
except FileNotFoundError:
    print("sorry, the file does not exist")