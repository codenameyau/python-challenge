import pickle

def main():
    """
    Challenge 04: Use requests to fetch next link
    http://www.pythonchallenge.com/pc/def/peak.html
    """
    # Open pickle file and load pickle data
    with open('data/level_05.p', 'rb') as file:
        loaded_data = pickle.load(file, encoding='latin1')

    # Read data and write each line in message
    message = ""
    for line in loaded_data:
        for chars in line:
            message += chars[0] * chars[1]
        message += "\n"

    print(message)


if __name__ == '__main__':
    main()
