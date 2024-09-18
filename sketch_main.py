import cv2

# Read the image
img = cv2.imread('D://xyz.jpg')

# Convert to grayscale
gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert = cv2.bitwise_not(gr)

# Apply Gaussian blur
blur = cv2.GaussianBlur(invert, (41, 41), 0)

# Invert the blurred image
inverted_blur = cv2.bitwise_not(blur)

# Divide the grayscale image by the inverted blurred image
sketch = cv2.divide(gr, inverted_blur, scale=256.0)

# Adjust the contrast
alpha = 0.8
sketch = cv2.multiply(sketch, alpha)

# Read the texture image
texture = cv2.imread('D://texture.jpg')

# Resize the texture image to match the dimensions of the sketch
resized_texture = cv2.resize(texture, (sketch.shape[1], sketch.shape[0]))

# Apply the texture overlay to the sketch
sketch_with_texture = cv2.addWeighted(sketch, 0.5, resized_texture[:, :, 0], 0.3, 0)

# Save the sketch
output_path = 'D://marlyn_s3.png'
cv2.imwrite(output_path, sketch_with_texture)

# Print a message to indicate successful saving
# print(f"Sketch saved to: {output_path}")
# Display the processed image
       # To display image
cv2.imshow('Pencil Sketch with Texture', sketch_with_texture)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all windows
