nameList = list()
while True:
    try:
        nameList.append(input("Name: "))
        adieu = "Adieu, adieu, to "
        str1 = nameList[0]
    except EOFError:
        if len(nameList) == 0:
            break
        elif len(nameList) == 1:
            print(adieu + str1)
        elif len(nameList) == 2:
            print(adieu + str1 + " and " + nameList[1])
        else:
            print(adieu + ", ".join(nameList[:-1]) + ", and " + nameList[-1])
        break