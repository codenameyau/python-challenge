import re
from PIL import Image, ImageDraw

def main():
    """
    Challenge 09: Using ImageDraw to draw polygon from points
    http://www.pythonchallenge.com/pc/return/good.html
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

if __name__ == '__main__':
    main()
