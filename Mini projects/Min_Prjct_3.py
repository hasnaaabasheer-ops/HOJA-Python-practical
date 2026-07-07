import random

def generate_number():
    return random.randint(1, 100)

def get_guess():
    return int(input("Enter your guess (1-100): "))

def check_guess(secret_number, guess):
    if guess < secret_number:
        print("Too low!")
        return False
    elif guess > secret_number:
        print("Too high!")
        return False
    else:
        print(" Correct!")
        return True

def play_game():
    secret_number = generate_number()
    attempts = 0
    correct = False
    
    while not correct:
        guess = get_guess()
        attempts += 1
        correct = check_guess(secret_number, guess)
    
    print("Attempts =", attempts)

def main():
    play_game()

main()