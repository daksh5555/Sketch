#                                                                           Sketch Builder

This repository contains a Python script that converts an image into a pencil sketch and applies a texture overlay. The project uses OpenCV to perform image processing operations like grayscale conversion, inversion, Gaussian blur, and blending with a texture.

Features
Convert images into pencil sketches: Using image processing techniques, you can turn any photo into a hand-drawn pencil sketch.
Apply a texture overlay: You can add a texture to the sketch to make it more artistic or realistic.
Installation
1. Prerequisites
Before running the code, you need to have the following installed:

Python 3.x
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
Save the image you want to convert into a sketch as xyz.jpg (or any other name, but be sure to update the path in the code accordingly).
Save a texture image as texture.jpg.
4. Modify the Code
The script reads images from the file paths specified in the code. Modify the paths to point to the correct locations of your images:
Main image: img = cv2.imread('D://xyz.jpg')
Texture image: texture = cv2.imread('D://texture.jpg')
If you want to apply a custom texture, replace D://texture.jpg with the path to your texture file.
