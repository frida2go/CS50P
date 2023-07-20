def main():
    inpu = input("Fraction: ")
    print(gauge(convert(inpu)))



def convert(fraction):
        num1,num2 = [int(i) for i in fraction.split("/")]
        if num2 == 0:
            raise ZeroDivisionError()
        elif num1 > num2:
            raise ValueError()
        else:
            result = round(num1 / num2 * 100)
            return result



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()