def squared_numbers(start, stop):
    """
       collected tow number and return list of consist all square
       number between start between stop
       :param start:
       :type start:int
       :param stop:
       :type stop:int
       :return:
       :rtype: list
       """
    list_squar_number = []
    while start <= stop:
        x = start ** 2

        list_squar_number.append(x)
        start += 1
    return list_squar_number


def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))


if __name__ == '__main__':
    main()