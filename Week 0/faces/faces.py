def convert(text):
    split_str = text.split()
    for i in range(len(split_str)):
        print (split_str[i])
        if split_str[i] == ":)":
            split_str[i] = "🙂"
        if split_str[i] == ":(":
            split_str[i] = "🙁"
        print (split_str[i])
    print(" ".join(split_str))

def main():
    inpu = input()
    convert(inpu)

main()

