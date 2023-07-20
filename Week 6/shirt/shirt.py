import sys
import csv
from os import path
from PIL import Image,ImageOps


fileType = [".jpg",".jpeg",".png"]

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(tuple(fileType)) or not sys.argv[2].lower().endswith(tuple(fileType))  :
    sys.exit("Invalid input")
elif path.splitext(sys.argv[1].lower())[1] != path.splitext(sys.argv[2].lower())[1]:
    sys.exit("Input and output have different extensions")
else:
    try:
        shirt = Image.open("shirt.png")
        noShirt = Image.open(sys.argv[1])
        ShirtSize = shirt.size
        noShirtResized = ImageOps.fit(noShirt, ShirtSize)
        noShirtResized.paste(shirt,shirt)
        noShirtResized.save(sys.argv[2])
        sys.exit()
    except FileNotFoundError:
        sys.exit("File does not exist")