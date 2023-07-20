inpu = input("Greeting: ").lower().strip()

if inpu.startswith("hello"):
    print("$0")
elif inpu.startswith("h"):
    print("$20")
else:
    print("$100")