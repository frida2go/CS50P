from random import randint

while True:
    try:
        level = int(input("Level: "))
        random = randint(1,level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess > random:
                    print("Too large!")
                elif guess < random:
                    print("Too small!")
                else:
                    print("Just right!")
                    break

            except ValueError:
                pass
        break
    except ValueError:
        pass


