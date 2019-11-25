import re

def main():
    """
    Challenge 03: Regex to find pattern, remember it says "exactly" 3
    http://www.pythonchallenge.com/pc/def/equality.html
    """
    data = open("data/level_03.txt").read()

    # Match regex pattern in data from pattern hint.
    bodyguard = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', data)
    print(''.join(bodyguard))

if __name__ == '__main__':
    main()
