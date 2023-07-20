month =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        inpu = input("Date: ")
        if "/" in inpu:
            list1 = inpu.split("/")
            if 0 < int(list1[0]) < 12 and 0 < int(list1[1]) < 30:
                m,d,y = [int(i) for i in list1]
            else:
                pass

        else:
            list1 = inpu.split(" ")
            list1[1] = list1[1][:-1]
            m = month.index(list1[0])+1
            if int(list1[1]) > 30:
                pass
            else:
                d,y = [int(i) for i in list1[1:]]


        print(f"{y}-{m:02}-{d:02}")
        break

    except (ValueError,IndexError,NameError):
        pass