import random

def numberGuessingGame():
    lower = 0
    upper = 100

    attempts = 5
    exact_number = random.randint(lower, upper)

    print("\nWelcome to Number Guessing Game")
    print(f"guess a number between {lower} and {upper} within {attempts} attempts")
    print("Best of Luck")

    while (attempts > 0):
        try:
            num = int(input("Enter your guess: "))
            attempts -= 1   #decreasing attempts with each guess

            if ((num < lower) or (num > upper)):
                print(f"Please guess a number between {lower} and {upper}")
            elif (num > exact_number):
                print(f"Your number '{num}' is lower")
            elif (num < exact_number):
                print(f"Your number '{num}' is greater")
            else:
                print("\nCongratulation!!!\nYou won the game")
                break
            
            if attempts == 0:
                print(f"\nSorry, all your attempts have been finished.\nThe correct number was {exact_number}\nBetter luck next time\n")
        except ValueError:
            print(f"Enter a valid number between {lower} and {upper} !!!")

if __name__ == '__main__':
    numberGuessingGame()

