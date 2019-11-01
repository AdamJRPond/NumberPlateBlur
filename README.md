# **Automatic Number Plate Blur Tool**

This is a simple implementation of a tool that will automatically blur the number plates of a vehicle, based upon identifying text in an image.

I used the [Google Vision](https://cloud.google.com/vision/) AutoML for text detection.

## Requirements

```bash 
pip install opencv-python \
            google-cloud-vision
```

## Installation

Clone the repo:

```bash
git clone https://github.com/AdamJRPond/NumberPlateBlur.git
```

## Example Usage

Given an input image, the program will process the image, blur the numberplate, and save the result to a specified destination:

```bash
# From root directory of project...
python3 blur_number_plate.py \
    --in_path="./images/test.jpg" \
    --out_path="./images/output.jpg"

```
## Result
### Input:
![Before blur](./images/test.jpg?raw=true)

### Output:
![After blur](./images/output.jpg?raw=true)

## Notes
- Works well on simple examples with only one number plate and no other text in the image

- Maintains resolution of image

- Requires authentication key for the Google Vision model. Can be downloaded in .json format and saved at `'key.json'`


### Please feel free to use and modify

