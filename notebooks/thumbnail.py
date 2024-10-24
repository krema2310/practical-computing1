import sys
from PIL import Image
filename="mushroom.jpg"
thumb_filename=filename.replace(".jpg", "-")
img=Image.open(filename)
img.thumbnail((100,100))
img.save(thumb_filename)
print("created thumbnail", thumb_filename)

