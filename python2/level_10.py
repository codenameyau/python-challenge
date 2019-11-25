def main():
    """
    Challenge 10: Look-and-say number sequence
    http://www.pythonchallenge.com/pc/return/bull.html
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
    print(len(array[30]))


if __name__ == '__main__':
    main()
