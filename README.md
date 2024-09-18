#                                                                           Sketch Builder

This repository contains a Python script that converts an image into a pencil sketch and applies a texture overlay. The project uses OpenCV to perform image processing operations like grayscale conversion, inversion, Gaussian blur, and blending with a texture.

# Features
Convert images into pencil sketches: You can turn any photo into a hand-drawn pencil sketch using image processing techniques.
Apply a texture overlay: You can add a texture to the sketch to make it more artistic or realistic.

# Installation
1. Prerequisites
Before running the code, you need to have the following installed:
Python 3
OpenCV (cv2)
You can install OpenCV using pip:
bash
Copy code
pip install opencv-python
2. Clone the Repository
bash
Copy code
git clone https://github.com/daksh5555/SketchBuilder.git
cd SketchBuilder
3. Set Up Image Files
Save the image you want to convert into a sketch as xyz.jpg (or any other name, but update the path in the code accordingly).
Save a texture image as texture.jpg.
4. Modify the Code
The script reads images from the file paths specified in the code. Modify the paths to point to the correct locations of your images:
Main image: img = cv2.imread('D://xyz.jpg')
Texture image: texture = cv2.imread('D://texture.jpg')
If you want to apply a custom texture, replace D://texture.jpg with the path to your texture file.
# Customization
Change the texture: Replace D://texture.jpg with a different image to apply a unique texture to the sketch.
Adjust Gaussian blur: Modify the kernel size (41, 41) in cv2.GaussianBlur() to change the smoothness of the sketch.
Adjust the blend ratio: Change the weight values 0.5 and 0.3 in cv2.addWeighted() to customize how much the sketch and texture blend.
Contributing
Feel free to open issues or pull requests to enhance the functionality of this project!




