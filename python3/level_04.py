import re
import requests

def main():
    """
    Challenge 04: Use requests to fetch next link
    http://www.pythonchallenge.com/pc/def/linkedlist.php
    """
    # Specify starting url link, pattern match, and current link number
    link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    pattern = re.compile(r'\d+')

    # use 12345 to start from beginning
    current = '77864'

    # Get page text and find next link with regex
    while pattern.match(current):
        nextlink = link + current
        data = requests.get(nextlink).text
        print(data)

        matches = re.findall(pattern, data)

        if matches:
            try:
                current = matches[-1]
            except IndexError:
                current = str(int(current)/2)
        else:
            break

if __name__ == '__main__':
    main()
