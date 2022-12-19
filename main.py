from PIL import Image
import random
import math

amount_of_colors = 5

def generate_color_palette():
  colors = []
  for i in range(amount_of_colors):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors.append((r, g, b))
  return colors

palette = generate_color_palette()

# Create a new image with a width equal to the number of colors in the palette
width = amount_of_colors * 100
height = math.floor(width * 0.6)
image = Image.new("RGB", (width, height))

# Loop through the colors in the palette and draw a horizontal stripe
# of each color in the image
ratio = width/amount_of_colors
color_selector = -1

for x in range(width):
    if(x%ratio==0):
        color_selector = color_selector + 1
    for y in range(height):
        image.putpixel((x, y), palette[color_selector])

# Save the image to a file
image.save("color_palette.png")