def count_vowels(text):
    count = 0
    vowels = "aeiou"
    for letter in text:
        if letter.lower() in vowels:
            count = count + 1
    return count

word = input("Enter a word: ")
result = count_vowels(word)

if result >= 3:
    print("Many vowels")
else:
    print("Few vowels")

print("Vowels:", result)