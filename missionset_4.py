"""
Python Challenge Levels 16-20
Pylint Score:
Username: butter
Password: fly
"""
from PIL import Image
import re, requests, bz2
import urllib, xmlrpclib, difflib
import email, wave, array
import auth, data


def level_16():
    """
    Challenge 16: Align pixels to single column
    URL: http://www.pythonchallenge.com/pc/return/mozart.html
    Data: http://www.pythonchallenge.com/pc/return/mozart.gif
    """
    # Open image and get dimensions
    image_file = "images/lv16-mozart.gif"
    image_url = "http://www.pythonchallenge.com/pc/return/mozart.gif"
    image = data.open_image(image_file, image_url, auth.AUTH_01)
    width, height = image.size[0], image.size[1]

    # Create new image, load pixels
    new_img = Image.new('RGB', (width, height))
    pix_1 = image.load()
    pix_2 = new_img.load()
    shifting = False
    pxs_seen = []
    new_w = 0

    # Scan through image looking for pattern (195)
    for img_h in xrange(0, height):
        for img_w in xrange(0, width):
            pix = pix_1[img_w, img_h]

            # Start writing pxs to new image
            if shifting:
                pix_2[new_w, img_h] = pix
                new_w += 1
            elif pix == 195:
                shifting = True
            else:
                pxs_seen.append(pix)

        # Finish up shifting pixels from before
        for i in pxs_seen:
            pix_2[new_w, img_h] = i
            new_w += 1

        # Reset variables
        shifting = False
        del pxs_seen[:]
        new_w = 0

    new_img.show()


def level_17():
    """
    Challenge 17: Cookie information using requests
    URL: http://www.pythonchallenge.com/pc/return/romance.html
    This challenge backtracks to level 4 as hinted by the image
    """
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    phone = "http://www.pythonchallenge.com/pc/phonebook.php"
    current = "12345"
    current_url = url+current
    cookie_info = []

    # Find next link and gather cookie info
    try:
        while True:
            req = requests.get(current_url, auth=auth.AUTH_01)
            current_url = url+str(re.findall(r'\d{3,7}', req.text)[-1])
            print "\n%s\n%s" % (current_url, req.text)
            cookie_info.append(req.cookies['info'])
    except IndexError:
        cookie_info.append(req.cookies['info'])
    finally:
        # Decipher message from cookie info
        msg = "".join(cookie_info)
        print bz2.decompress(urllib.unquote_plus(msg))
        server = xmlrpclib.ServerProxy(phone)
        print server.phone("Leopold")

        #Send message to Leopold
        url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
        cookie = dict(info="the flowers are on their way")
        req = requests.get(url, cookies=cookie)
        print req.text


def level_18():
    """
    Challenge 18: Telling the difference with deltas
    URL: http://www.pythonchallenge.com/pc/return/balloons.html
    Split lines from [0:53] and [56:109]
    """
    deltas = open('text/lv18-delta.txt', 'r').read()
    lines  = deltas.splitlines()
    left, right, png = [], [], ['', '', '']

    # Separate the values by columns 53 and 56
    for i in lines:
        left.append(i[0:53])
        right.append(i[56:109])

    # Compare the difference between left and right
    diff = list(difflib.ndiff(left, right))
    for row in diff:
        symbol = row[0]
        # Convert each number into ascii data
        for vals in row[2:].split():
            byte = chr(int(vals, 16))
            if symbol == '-':
                png[0] += ''.join(byte)
            elif symbol == '+':
                png[1] += ''.join(byte)
            elif symbol == ' ':
                png[2] += ''.join(byte)

    # Save into image png
    for i in range(3):
        with open('images/lv18-pic%d.png' % i, 'wb') as img:
            img.write(png[i])
    print "Finished writing binary to PNG in images."


def level_19():
    """
    Challenge 19: Writing to audio wav file
    URL: http://www.pythonchallenge.com/pc/hex/bin.html
    Colors on map are inverted, so wav should be inverted
    """
    # From mail content, create wav file
    mail = email.message_from_file(open('text/lv19-email.txt'))
    for chunk in mail.walk():
        if chunk.get_content_maintype() == "audio":
            audio = chunk.get_payload(decode=1)
            with open('data/lv19-audio.wav', 'wb') as sound:
                sound.write(audio)

    # Open wav file and create new wav with same parameters
    wav_old = wave.open('data/lv19-audio.wav', 'rb')
    wav_inv = wave.open('data/lv19-invert.wav', 'wb')
    wav_inv.setparams(wav_old.getparams())
    frames = wav_old.getnframes()

    # Byte swap contents of wav file
    data = array.array('i')
    data.fromstring(wav_old.readframes(frames))
    data.byteswap()

    # Write data to inverted file and close
    wav_inv.writeframes(data.tostring())
    wav_old.close()
    wav_inv.close()