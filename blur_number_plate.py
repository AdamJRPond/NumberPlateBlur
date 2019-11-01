import argparse
import io
import os

from google.cloud import vision_v1p3beta1 as vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

import cv2

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--in_path", type=str,help="Path to input image file.")
parser.add_argument("--out_path", type=str, help="Path to save output image file.")

opt = parser.parse_args()

def blur_number_plate(img_path):

    # Read image
    img = cv2.imread(img_path)

    # Google Vision client
    client = vision.ImageAnnotatorClient()

    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Response from client
    response = client.text_detection(image=image)
    text = response.text_annotations[0]

    # Coordinates for bounding box
    vertices = [(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices]

    x, x_max = vertices[0][0], vertices[2][0]
    y, y_max = vertices[0][1], vertices[2][1]

    # Apply Gaussian blur to area of image within bounding box
    img[y:y_max, x:x_max] = cv2.GaussianBlur(img[y:y_max, x:x_max],
                                             ksize=(0,0),
                                             sigmaX=10)
    # Save output
    cv2.imwrite(opt.out_path, img)


blur_number_plate(opt.in_path)

print('Output image can be found at: {}'.format(opt.out_path))
