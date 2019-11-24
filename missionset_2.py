"""
Python Challenge Levels 6-10
Pylint Score: 9.77
Username: huge
Password: file
"""
from PIL import Image, ImageDraw
from StringIO import StringIO
import zipfile, re, requests
import bz2


def level_08():
    """
    Challenge 08: Using bz2 to decompress data
    URL: http://www.pythonchallenge.com/pc/def/integrity.html
    """
    user = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
    pswd = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
    print bz2.decompress(user)
    print bz2.decompress(pswd)


def level_09():
    """
    Challenge 09: Using ImageDraw to draw polygon from points
    URL: http://www.pythonchallenge.com/pc/return/good.html
    External Files: "text/lv9-dots1.txt", "text/lv9-dots2.txt"
    """
    # Read text files and gather numberical points
    pattern = re.compile(r'\d+')
    dots1 = re.findall(pattern, open("text/lv9-dots1.txt").read())
    dots2 = re.findall(pattern, open("text/lv9-dots2.txt").read())

    # Create a new image to draw points
    image = Image.new('RGB', (450, 450))
    draw  = ImageDraw.Draw(image)

    # Draw first polygon
    points = []
    for i in xrange(0, len(dots1), 2):
        points.append((int(dots1[i]), int(dots1[i+1])))
    draw.polygon(points)

    # Clear points list, and draw second polygon
    del points[:]
    for i in xrange(0, len(dots2), 2):
        points.append((int(dots2[i]), int(dots2[i+1])))
    draw.polygon(points)

    del draw
    image.show()


def level_10():
    """
    Challenge 10: Look-and-say number sequence
    URL: http://www.pythonchallenge.com/pc/return/bull.html
    Seq: 1, 11, 21, 1211, 111221, 312211, ...
    """
    array = ['1']
    for i in xrange(0, 31):
        current = array[i][0]
        array.append("")
        count = 0
        for j in array[i]:
            if j == current:
                count += 1
            else:
                array[i+1] += str(count)+current
                count = 1
            current = j
        array[i+1] += str(count)+current
    print len(array[30])
