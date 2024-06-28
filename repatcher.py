import os
import numpy as np
from PIL import Image
from tqdm import tqdm

input_folder = 'C:/Users/praan/Desktop/UNET DATA/IMAGES/RESULTS/20_Ep_WCCE_BS8_w11_STD/patched results/'
output_folder = 'C:/Users/praan/Desktop/UNET DATA/IMAGES/RESULTS/20_Ep_WCCE_BS8_w11_STD/results/'

# Define dimensions for the combined image (number of patch rows and patch columns)
columns = 15
rows = 9
small_image_width = 128  
small_image_height = 128  

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through image types (m and p) which are image number prefixes for the image
for image_type in ['m', 'p']: 
    # Iterate through image numbers (1 to 18)
    for image_number in range(1, 19):
        # Initialize a blank image with specified dimensions
        combined_image = Image.new('RGB', (columns * small_image_width, rows * small_image_height))
        # Iterate through small image indices
        for row in range(rows):
            for col in range(columns):
                small_image_index = col + row * columns
                small_image_filename = "mask_%s%d_%d.png" % (image_type, image_number, small_image_index) 
                small_image_path = os.path.join(input_folder, small_image_filename)
                try:
                    small_image = Image.open(small_image_path)
                    # Paste small image onto the combined image
                    x = col * small_image_width
                    y = row * small_image_height
                    combined_image.paste(small_image, (x, y))
                except FileNotFoundError:
                    print("Warning: Small image not found: %s" % small_image_path)
        # Save the combined image
        combined_image_filename = "mask_%s%d.png" % (image_type, image_number) 
        combined_image_path = os.path.join(output_folder, combined_image_filename)
        combined_image.save(combined_image_path)

print("All combined images saved to output folder.")