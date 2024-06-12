# Image-shortener

## Description
This is a simple Python script to reduce the size of images in a specified directory.

## Usage
1. To run the server, create a local environment.
2. Install dependencies by running `python -m pip install -r requirements.txt`.
3. Create a directory called `src` in the root directory.
4. Place the images you want to shrink in the `src` directory.
5. Run the server using `python server.py`.

## How it works
- The script iterates over all the images in the `src` directory.
- For each image, it calculates a scale factor to reduce its size while maintaining aspect ratio.
- The image is resized accordingly using Pillow library.
- The resized image is saved in the same directory with "_shrink" added to the filename.

## Requirements
- Python 3.x
- Pillow library (installed automatically via `requirements.txt`)

## Note
- Adjust the `quality` parameter in the script to control the image quality after resizing.
- Ensure the combined size of the images in the `src` directory is not more than the target size specified in the script.

