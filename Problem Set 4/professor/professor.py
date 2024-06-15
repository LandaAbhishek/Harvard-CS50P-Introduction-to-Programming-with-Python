# importing libraries
import random

# setting values
def main():
    question = 10  # number of questions
    score = 0
    wrong = 3  # attempts allowed per question
    levels = get_level()

    # defining questions and rules
    while question != 0:
        # if wrong, 3 chances
        if wrong == 3:
            # generate integer for new equation
            x, y = generate_integer(levels)

        # if right, new question
        try:
            player_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if player_answer == answer:
                question = question - 1
                score = score + 1
                wrong = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            wrong = wrong - 1
            pass
        # if 3 wrong, generate new question
        if wrong == 0:
            answer = x+y
            print((f"{x} + {y} = {answer}"))
            wrong = 3
            question = question - 1
            continue
    print(f"Score: {score}")

# setting levels
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass

# level deficulty
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

# calling main game function
if __name__ == "__main__":
    main()
