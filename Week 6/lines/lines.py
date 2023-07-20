import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1],"r") as file:
            list1 = []
            for i in file:
                if i.strip() != "" and not i.strip().startswith("'''") and not i.strip().startswith("#"):
                    list1.append(i.strip())
            print(len(list1))

    except FileNotFoundError:
        print("File does not exist")


