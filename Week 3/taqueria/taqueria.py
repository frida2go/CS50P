dict1 = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

sum1 = 0

while True:
    try:
        item = input("Item: ").title()
        if item in dict1:
            sum1 += float(dict1[item])
            print (f"Total: ${sum1:.2f}")

    except EOFError:
        break