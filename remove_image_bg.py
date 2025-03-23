from PIL import Image
import numpy as np
import easygui


# Helper function to make a specific background color transparent
def remove_background(image: Image.Image, background_color=(255, 255, 255)):
    image = image.convert("RGBA")  # Ensure the image has an alpha channel
    data = np.array(image)  # Convert image to a numpy array for processing

    # Separate the color and alpha channels
    r, g, b, a = data.T

    # Detect pixels matching the background color and make them transparent
    background_mask = (r == background_color[0]) & (g == background_color[1]) & (b == background_color[2])
    data[..., :-1][background_mask.T] = (0, 0, 0)  # Set R, G, B to black
    data[..., -1][background_mask.T] = 0  # Set alpha to 0 (transparent)

    return Image.fromarray(data)


# File selection dialogs for input and output
input_path = easygui.fileopenbox(title='Select image file')
output_path = easygui.filesavebox(title='Save file to..')

if input_path and output_path:
    input_image = Image.open(input_path)  # Open the input image

    # Process the image to remove the background (assuming white as the background)
    output_image = remove_background(input_image, background_color=(255, 255, 255))

    # Save the result
    output_image.save(output_path)
