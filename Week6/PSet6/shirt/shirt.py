import sys
import os
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_list =[".jpg",".jpeg",".png"]
ext1 = os.path.splitext(sys.argv[1])[1].lower()
ext2 = os.path.splitext(sys.argv[2])[1].lower()
if ext1 not in valid_list:
    sys.exit("Invalid input")
elif ext2 not in valid_list:
    sys.exit("Invalid output")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open (sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
photo = ImageOps.fit(photo,size)
photo.paste(shirt,shirt)
photo.save(sys.argv[2])