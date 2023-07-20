def main():
    inpu = value(input("Gretting: "))
    print (inpu)

#ok
def value(greeting):
    '''ok'''
    if greeting.lower().startswith("hello"):
        return(0)
    elif greeting.lower().startswith("h"):
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()