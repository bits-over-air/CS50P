import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

#if-else
if len(sys.argv) == 1:
    font_name = random.choice(font_list)
elif len(sys.argv) ==3 and sys.argv[1]in ["-f","--font"]and sys.argv[2] in font_list:
    font_name = sys.argv[2]
else:
    sys.exit("Invalid Usage")

figlet.setFont(font=font_name )

s = input("Input: ")
print(figlet.renderText(s))
