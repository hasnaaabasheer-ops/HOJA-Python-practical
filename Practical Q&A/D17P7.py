file = open("poem.txt","r")
longest_word =""
for line in file:
    words = line.split()
    for word in words: 
        if len(word)>len(longest_word):
            longest_word =word

file.close()
print("longest word :",longest_word)