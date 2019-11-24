"""
Python Challenge Levels 11-15
Pylint Score: 10.00
Username: huge
Password: file
"""
from PIL import Image
import requests, xmlrpclib
import datetime, calendar
import auth, data


def level_11():
    """
    Challenge 11: odd-even pixel skipping
    URL: http://www.pythonchallenge.com/pc/return/5808.html
    Data: http://www.pythonchallenge.com/pc/return/cave.jpg
    """
    # Open image using data module and get image dimensions
    image_file = "images/lv11-oddeven.jpg"
    image_url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
    image = data.open_image(image_file, image_url, auth.AUTH_01)
    image_size = image.size
    width, height = image_size[0], image_size[1]

    # Create new blank image, load pixels
    new_img  = Image.new('RGB', (width/2, height/2))
    pixels_1 = image.load()
    pixels_2 = new_img.load()
    new_h, new_w = 0, 0

    # Iterate through each pixel
    for old_h in xrange(0, height, 2):
        for old_w in xrange(0, width, 2):
            pixels_2[new_w, new_h] = pixels_1[old_w, old_h]
            new_w += 1
        new_h += 1
        new_w = 0

    # Show a comparison between old and new image
    image.show()
    new_img.show()


def level_12():
    """
    Challenge 12: gfx and binary data deshuffling
    URL: http://www.pythonchallenge.com/pc/return/evil.html
    Data: http://www.pythonchallenge.com/pc/return/evil2.gfx
    This level is messed up. Last image is corrupted or missing.
    """
    gfx_url  = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
    gfx_data = requests.get(gfx_url, auth=auth.AUTH_01).content

    # Write to binary data based on gfx
    for i in xrange(1, 4):
        open("data/lv12-%d.dat" % i, "w").write(gfx_data[i-1::5])
    print "Binary data written to data\nNext Level: disproportional"


def level_13():
    """
    Challenge 13: XML remote procedure call (RPC) methods
    URL: http://www.pythonchallenge.com/pc/return/disproportional.html
    """
    url = "http://www.pythonchallenge.com/pc/phonebook.php"
    server = xmlrpclib.ServerProxy(url)
    print server.system.listMethods()
    print server.phone("Bert")


def level_14():
    """
    Challenge 14: Clockwise spiral image recreation
    URL: http://www.pythonchallenge.com/pc/return/italy.html
    """
    # Create Image object from wire.png
    image_file = "images/lv14-long.png"
    image_url  = "http://www.pythonchallenge.com/pc/return/wire.png"
    image = data.open_image(image_file, image_url, auth.AUTH_01)
    width = image.size[0]

    # Create a new Image for spiral
    spiral   = Image.new('RGB', (100, 100))
    img_line = image.load()
    img_spiral = spiral.load()

    # current: top, right, bottom, left
    current = "top"
    width_min, height_min = 0, 0
    width_max, height_max = 99, 99
    width_now, height_now = -1, 0

    # Go through each pixel in original image
    print "Constructing image in clockwise spiral...",
    for i in xrange(0, width):
        # Fill in top
        if current == "top":
            width_now += 1
            if width_now >= width_max:
                current = "right"
                height_max -= 1

        # Fill in right
        elif current == "right":
            height_now += 1
            if height_now >= height_max:
                current = "bottom"
                width_max -= 1

        # Fill in bottom
        elif current == "bottom":
            width_now -= 1
            if width_now <= width_min:
                current = "left"
                width_min += 1

        # Fill in left
        elif current == "left":
            height_now -= 1
            if height_now <= height_min:
                current = "top"
                height_min += 1

        img_spiral[width_now, height_now] = img_line[i, 0]
    spiral.show()


def level_15():
    """
    Challenge 15: Calendar with datetime
    URL: http://www.pythonchallenge.com/pc/return/uzi.html
    Who is he? mozart
    """
    for i in xrange(1996, 1006, -10):
        date = datetime.date(i, 1, 26)
        # If jan 26 was a monday, print year
        if date.isoweekday() == 1 and calendar.isleap(i):
            print i
        del date
