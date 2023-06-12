# Image Resizer

This is a simple Python script that uses the `PIL` library to resize an image.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- `PIL` library installed. You can install it using pip:


## Usage

1. Clone the repository or download the `image_resizer.py` file.

2. Place the image you want to resize in the same directory as the script and name it `image-test.jpg`. Alternatively, you can modify the code to specify a different image path.

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. Run the script by executing the following command:

5. You will be prompted to enter the desired width and length in pixels for the resized image. Enter the values and press Enter.

6. The script will resize the image and save it as `image-test-{width}-{length}px.jpeg`, where `{width}` and `{length}` are the dimensions you entered.

7. Check the directory for the resized image.

## Example


This will resize the `image-test.jpg` to 800 pixels width and 600 pixels length and save it as `image-test-800-600px.jpeg`.

## Notes

- The script assumes that the input image is in JPEG format. If you want to use a different format, make sure to modify the extension in the `save` function accordingly.

- The script uses the `resize` method of the `Image` class from the `PIL` library to perform the image resizing. The original aspect ratio of the image is not preserved, and the image may appear distorted if the width and length have different proportions.

- The resized image will overwrite any existing image with the same filename. Make sure to back up your files if needed.

- This script is intended for educational purposes and may not handle all possible scenarios or error conditions. Use it at your own risk.

## License

This project is licensed under the [MIT License](LICENSE). Mauro Exequiel Pepa - Developer maker
