from random import randint

print("\t\t\t ***** GUESS ME *****")

ans = randint(1,100)

class ValueSmallError(Exception):
    pass
class ValueLargeError(Exception):
    pass

def guess():
    try:
        num = int(input("\nGuess the number: "))
        if num > ans:
            raise ValueLargeError
        elif num < ans:
            raise ValueSmallError
        else:
            print("Congratulations, You won !!")
    except ValueLargeError:
        print("\nYou entered a large number. Guess a smaller one...")
        guess()
    except ValueSmallError:
        print("\nYou entered a small number. Guess a larger one...")
        guess()
    return

guess()
