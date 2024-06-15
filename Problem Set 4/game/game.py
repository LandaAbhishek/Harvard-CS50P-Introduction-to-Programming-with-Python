# importing library
import random

#input levels
while True:
    try:
        levels = int(input("Level: "))
        answer = random.randint(1, levels)
        # setting guess
        while True:
            guess = int(input("Guess: "))
            if guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
            elif guess == answer:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
