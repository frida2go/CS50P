while True:
    try:
        inpu = input("Fraction: ")
        num1,num2 = [int(i) for i in inpu.split("/")]
        result = round(num1/num2*100)
        if result > 100:
            pass
        elif result >= 99:
            print("F")
            break
        elif result > 1:
            print(f"{result}%")
            break
        else:
            print ("E")
            break

    except (ValueError, ZeroDivisionError):
        pass