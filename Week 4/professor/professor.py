import random

def main():
    score = 0
    count = 0
    level = get_level()

    # to have 10 times questions
    while count < 10:
        in1, in2 = generate_integer(level), generate_integer(level)
        result = in1 + in2
        count += 1
        error = 1
        correct = False

        # to get user's input
        while error < 4:
            try:
                inpu = int(input(f"{in1} + {in2} = "))
                if inpu == result:
                    score += 1
                    break
                else:
                    error += 1
                    print("EEE")
            except ValueError:
                error += 1
                print("EEE")

        # print the result when user tried 3 times and not get the correct one
        print(f"{in1} + {in2} = {result}")

    # print the score when user finish 10 questions
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            inpu = int(input("Level:"))
        except ValueError:
            pass
        else:
            if 0 < inpu < 4:
                return inpu
            else:
                pass

def generate_integer(level):
    start = 0 if level == 1 else 10 ** (level - 1)
    end = 10**level - 1
    return random.randint(start, end)

if __name__ == "__main__":
    main()