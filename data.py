"""
Python Challenge Data Handler.

Use requests to fetch external data and save it into a specified file path.
"""
from PIL import Image
from StringIO import StringIO
import requests, os


def open_image(image_file, image_url, auth=None):
    """
    Attempt to create an Image object by opening the provided
    image_file. Returns the Image object. If the file does not
    exist, the image will be fetched from the image_url.
    """
    try:
        return Image.open(image_file)
    # Request image and save it if not exist
    except IOError:
        save_image(image_url, image_file, auth)
        return Image.open(image_file)


def save_image(url, filename, auth=None):
    """
    Uses requests library to retrieve image from url.
    Parses the request content to an Image object and
    saves the image into the images directory
    """
    # Request image content from url
    print("Downloading image: " + url)
    image_req = requests.get(url, auth=auth).content
    image = Image.open(StringIO(image_req))

    # Save image into image directory
    if not os.path.exists('images'):
        os.makedirs('images')
    image.save(filename)
