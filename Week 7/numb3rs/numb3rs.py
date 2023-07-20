import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if match := re.match(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        for i in range(1,4):
            if int(match.group(i)) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()