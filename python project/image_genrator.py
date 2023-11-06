from PIL import Image, ImageDraw

# Set the image size and background color
image_size = (400, 400)
background_color = (255, 0, 0)  # Red in RGB format

# Create a new image with the specified size and color
image = Image.new("RGB", image_size, background_color)

# Save the generated image
image.save("generated_image.png")

# Display the generated image (optional)
image.show()
from PIL import Image, ImageDraw
import random

# Set the image size and background color
image_size = (400, 400)
background_color = (255, 255, 255)  # White in RGB format

# Create a new image with the specified size and color
image = Image.new("RGB", image_size, background_color)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw random rectangles on the image
for _ in range(10):
    x1 = random.randint(0, image_size[0])
    y1 = random.randint(0, image_size[1])
    x2 = random.randint(x1, image_size[0])
    y2 = random.randint(y1, image_size[1])
    fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle([x1, y1, x2, y2], fill=fill_color)

# Save the generated image
image.save("generated_image.png")

# Display the generated image (optional)
image.show()
