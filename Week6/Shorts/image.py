from PIL import Image
from PIL import ImageFilter



def main():
  with Image.open("in.jpeg") as img:
    print(img.size)
    print(img.format)
    img =img.rotate(180)
    img.save("out.jpeg")
    img.filter(ImageFilter.BLUR) #blurs the image 
    img.filter(ImageFilter.FIND_EDGES)



main()