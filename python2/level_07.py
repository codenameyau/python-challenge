import requests
import re
from PIL import Image
from StringIO import StringIO

def main():
    """
    Challenge 07: Using requests to fetch Image and PIL
    http://www.pythonchallenge.com/pc/def/oxygen.html
    """
    # Fetch image from url and convert to Image object
    image_url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    image_req = requests.get(image_url)
    image_obj = Image.open(StringIO(image_req.content))
    print ("Grabbing image from %s" % image_url)

    # Get width and height of image
    size   = image_obj.size
    width  = size[0]
    height = size[1]
    print ("Image Size: width (%d), height (%d)" % (width, height))

    # Load image, store shades of gray, track last gray
    image_pxs   = image_obj.load()
    shades_gray = []

    # Scan image coords for shades of gray, skipping non-gray
    for i in xrange(0, height):
        line = image_pxs[0, i]
        # Look through for first gray, skip otherwise
        if line[0] == line[1] == line[2]:
            for j in xrange(0, width, 7):
                pix = image_pxs[j, i]
                # If red, blue, green are equal then it is gray
                if pix[0] == pix[1] == pix[2]:
                    gray = pix[0]
                    shades_gray.append(gray)
            break

    # Construct message and display from shades of gray
    for i in xrange(0, len(shades_gray)):
        shades_gray[i] = chr(int(shades_gray[i]))
    print ("".join(shades_gray))

    keywords = re.findall(r'\d+', "".join(shades_gray))
    message = ""

    for i in keywords:
        message += chr(int(i))
    print ("\nNext Level: %s" % message)


if __name__ == '__main__':
    main()
