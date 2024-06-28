import os
import cv2

input_folder = 'C:/Users/praan/Desktop/UNET DATA/IMAGES/TRAIN IMAGES/'  
output_folder = 'C:/Users/praan/Desktop/UNET DATA/IMAGES/patches_IMG/'  

patch_size = 128

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of image filenames in the input folder
image_filenames = [f for f in os.listdir(input_folder) if f.endswith(('.png'))]

for filename in image_filenames:
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)

    # Calculate number of patches in each dimension
    num_patches_height = img.shape[0] // patch_size
    num_patches_width = img.shape[1] // patch_size

    patch_count = 0
    for i in range(num_patches_height):
        for j in range(num_patches_width):
            patch = img[i * patch_size:(i + 1) * patch_size, j * patch_size:(j + 1) * patch_size]

            base_filename, extension = os.path.splitext(filename)
            patch_filename = "%s_%d.png" % (base_filename, patch_count)  # Use string formatting
            patch_filepath = os.path.join(output_folder, patch_filename)

            cv2.imwrite(patch_filepath, patch)
            patch_count += 1

print("{} images processed and 135 patches saved per image.".format(len(image_filenames)))
