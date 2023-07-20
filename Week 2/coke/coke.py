amount = 50
while True:
    print(f"Amount Due: {amount}")
    inpu = int(input("Insert Coin: "))
    if inpu == 5 or inpu == 10 or inpu == 25:
        amount -=inpu
    if amount <=0:
        break
print(f"Change Owed: {-amount}")