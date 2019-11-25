import bz2

def main():
    """
    Challenge 08: Using bz2 to decompress data
    http://www.pythonchallenge.com/pc/def/integrity.html
    """
    user = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
    pswd = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
    print(bz2.decompress(user))
    print(bz2.decompress(pswd))

if __name__ == '__main__':
    main()
