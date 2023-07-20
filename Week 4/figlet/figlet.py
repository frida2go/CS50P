from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    font_r = choice(font_list)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_list :
    font_r = sys.argv[2]

else:
    sys.exit("Invalid usage")

inpu = input("Input:")
figlet.setFont(font=font_r)
print(figlet.renderText(inpu))
