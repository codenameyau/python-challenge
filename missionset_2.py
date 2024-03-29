"""
Python Challenge Levels 6-10
Pylint Score: 9.77
Username: huge
Password: file
"""
from PIL import Image, ImageDraw
import zipfile, re, requests


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
