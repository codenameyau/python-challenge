import zipfile
import re

def main():
    """
    Challenge 06: zipfile, traverse plain text files
    http://www.pythonchallenge.com/pc/def/channel.html
    """
    zipfiles = zipfile.ZipFile('data/level_06.zip', 'r')
    pattern  = re.compile(r'\d{2,8}')
    current  = "readme"
    message  = ""

    # Traverse text files in zipfiles
    while True:
        try:
            # Read each text file and print contents
            file_data = zipfiles.open(current + '.txt').read()
            print(file_data)

            # Find file number and add to collection
            current = re.findall(pattern, file_data)[-1]
            message += zipfiles.getinfo(current+'.txt').comment

        except IndexError:
            break
    print(message)
    zipfiles.close()


if __name__ == '__main__':
    main()
