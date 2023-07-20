import validators

def main():
    print(valide(input("What's your email address? ")))


def valide(s):
    if validators.email(s) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()