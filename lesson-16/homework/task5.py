from PIL import Image
import numpy as np

# Load the image
image_path = "images/birds.jpg"
image = Image.open(image_path)
image_array = np.array(image)

# Function to flip the image horizontally and vertically
def flip_image(image_array):
    return np.flip(image_array, axis=(0, 1))  # Flip both axes

# Function to add random noise
def add_noise(image_array, intensity=25):
    noise = np.random.randint(-intensity, intensity, image_array.shape, dtype=np.int16)
    noisy_image = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    return noisy_image

# Function to brighten channels
def brighten_channels(image_array, value=40):
    brightened_image = np.clip(image_array + value, 0, 255).astype(np.uint8)
    return brightened_image

# Function to apply a mask
def apply_mask(image_array, x, y, width, height):
    masked_image = image_array.copy()
    masked_image[y:y+height, x:x+width] = [0, 0, 0]  # Set region to black
    return masked_image

# Apply manipulations
flipped_image = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array, 100, 100, 100, 100)  # Mask a 100x100 region at (100, 100)

# Save the modified images
Image.fromarray(flipped_image).save("flipped_image.jpg")
Image.fromarray(noisy_image).save("noisy_image.jpg")
Image.fromarray(brightened_image).save("brightened_image.jpg")
Image.fromarray(masked_image).save("masked_image.jpg")