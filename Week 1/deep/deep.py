inpu = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
inpu = inpu.strip().lower()

match inpu:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")