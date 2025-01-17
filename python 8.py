# Import the OpenCV library
import cv2

# Read an image from a file
image = cv2.imread('C:/Users/Rahul/Desktop/puppy.jpg')

# Check if the image file was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Find the shape (dimensions) of the image
height, width, channels = image.shape
print(f"Original Image Dimensions: {width}x{height}")

# Resize the image to dimensions of 400x256 pixels
resized_image = cv2.resize(image, (400, 256))

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)

# Flip the image horizontally
flipped_image_horizontal = cv2.flip(resized_image, 1)

# Display the horizontally flipped image
cv2.imshow('Horizontally Flipped Image', flipped_image_horizontal)
cv2.waitKey(0)

# Flip the image vertically
flipped_image_vertical = cv2.flip(resized_image, 0)

# Display the vertically flipped image
cv2.imshow('Vertically Flipped Image', flipped_image_vertical)
cv2.waitKey(0)

# Flip the image both horizontally and vertically
flipped_image_both = cv2.flip(resized_image, -1)

# Display the image flipped both horizontally and vertically
cv2.imshow('Flipped Both Horizontally and Vertically', flipped_image_both)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
