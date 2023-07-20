def main():
    inpu = input("Input: ")
    print(shorten(inpu))

def shorten(word):
    vowels = ["a","e","i","o","u"]
    newstr = ""
    for i in range(len(word)):
        if word[i].lower() not in vowels:
            newstr += word[i]

    return f"{newstr}"

if __name__ == "__main__":
    main()