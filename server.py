from PIL import Image
import os
from icecream import ic

def shrink_image(image_path, target_size):
    
    img = Image.open(image_path)
    ic(img)
    
    # Get current size
    current_size = os.path.getsize(image_path)
    
    # Calculate the scale factor to reduce the image size
    scale_factor = (target_size / current_size) ** 0.5
    
    # Calculate the new dimensions
    new_width = int(img.width * scale_factor)
    new_height = int(img.height * scale_factor)
    
    # Resize the image
    img = img.resize((new_width, new_height), Image.LANCZOS)
    
    # Save the resized image
    output_path = os.path.splitext(image_path)[0] + '_shrink.jpg' 
    img.save(output_path, optimize=True, quality=85)  # Adjust quality as needed

# Directory where your images are stored
src_directory = 'src'

# Target size in bytes
target_size_bytes = 5 * 1024 * 1024  # 5 MB

# Iterate over images in the source directory
for filename in os.listdir(src_directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        image_path = os.path.join(src_directory, filename)
        shrink_image(image_path, target_size_bytes)