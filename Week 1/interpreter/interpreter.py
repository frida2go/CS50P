expression = input("Expression: ")
list1 = expression.split(" ")
operator = list1[1]
list1[0] = float(list1[0])
list1[2] = float(list1[2])


if operator == "+":
    print(list1[0]+list1[2])
elif operator == "-":
    print(list1[0]-list1[2])
elif operator == "*":
    print(list1[0]*list1[2])
else:
    print(list1[0]/list1[2])