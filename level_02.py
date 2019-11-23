def main():
    """
    Challenge 02: Find hidden message in source
    URL: http://www.pythonchallenge.com/pc/def/ocr.html
    """
    data = open("data/level_02.txt").read()

    # Construct hidden message by looking for alpha characters
    message = ""
    for letter in data:
        if letter.isalpha():
            message += letter
    print(message)

if __name__ == '__main__':
    main()
