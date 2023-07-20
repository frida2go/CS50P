def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    no = ["!"," ","."]
    if len(s) < 2 or len(s) > 6 or not s[0:2].isalpha():
        return False
    else:
        for i in range(len(s)):
            if s[i] in no:
                return False
            if s[i].isnumeric():
                if s[i] == "0":
                    return False
                elif s[i:len(s)].isnumeric():
                    break


    return True


if __name__ == "__main__":
    main()
