import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    r = r"^(1[0-2]*|[\d]{1}):?([0-5]?[0-9])? (PM|AM) to (1[0-2]*|[\d]{1}):?(:?[0-5]?[0-9])? (PM|AM)"
    if match := re.search(r, s):

        # to change the None object to 00, which is format like 9 AM to 10 PM
        l = [ 0 if i == None else i for i in list(match.groups())]

        # to get the AM/PM string which is in wether in [2] or [5] of the list
        for i in range(2,6,3):

            #convert PM time by adding 12, 12 PM not included
            if l[i] == "PM" and l[i-2] != "12":
                l[i-2] = int(l[i-2]) + 12

            #AM time stay same excluding 12:AM which change to 00:00
            elif l[i] == "AM" and l[i-2] == "12":
                l[i-2] = 0

        #delete the AM/PM element to avoid ValueError when transfer string to int
        l.pop(2)
        l.pop(-1)

        l = [int(i) for i in l]

        return (f"{l[0]:02}:{l[1]:02} to {l[2]:02}:{l[3]:02}")

    else:
        raise ValueError


if __name__ == "__main__":
    main()