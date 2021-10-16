# Desc: This script creates ascii art out of typical image files.
# Coded by: Tanay Patel

from PIL import Image

# Getting image dimensions 
img = Image.open(r"Images/Tsunami.png")
width, height = img.size

# Setting aspect ratio and scaling image
aspect_ratio = height/width
new_width = 1000
new_height = aspect_ratio * new_width*0.4

# Converting resized-image to grey scale and getting pixel values
img = img.resize((new_width, int(new_height)))
img = img.convert('L')
pixels = img.getdata()

# Creating list of dark -> light ASCII characters
chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

#Converting Image to String with ASCII Characters
new_pixels = []
for pixel in pixels:
    new_pixels += [chars[pixel//25]]
new_pixels = ''.join(new_pixels)

# Slicing ASCII character string into new lines
new_pixels_count = len(new_pixels)
ascii_image = []
for index in range(0, new_pixels_count, new_width):
    ascii_image += [new_pixels[index:index + new_width]] 
ascii_image = "\n".join(ascii_image)

# Writing text to a file
file = "ascii_image.txt"
with open(file, "w") as f:
    f.write(ascii_image)
    print("Saved image to: " + file)
