def main():
    """
    Challenge 01: Translate message
    URL: http://www.pythonchallenge.com/pc/def/map.html
    """
    # Copy purple message from page.
    message = open("data/level_01.txt").read()

    # Create translation table and translate text.
    map_before = "abcdefghijklmnopqrstuvwxyz"
    map_after  = "cdefghijklmnopqrstuvwxyzab"
    transtable = str.maketrans(map_before, map_after)
    print(message.translate(transtable))

    # Apply translate on URL "map"
    print(f"\nNext Mission URL: {'map'.translate(transtable)}")

if __name__ == '__main__':
    main()
