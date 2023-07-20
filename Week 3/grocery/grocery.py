dict1 = {}

while True:
    try:
        item = input().upper()
        if item in dict1:
            dict1[item]+=1
        else:
            dict1[item] =1

    except EOFError:
        for i in sorted(dict1.keys()):
            print(dict1[i],i)
        break

