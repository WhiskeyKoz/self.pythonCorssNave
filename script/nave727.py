def arrow(my_char, max_length):
    """
    collected some cher and some number and the
    function make "arrow" built of my_char length built of max_length
    and return arrow
    :param my_char: cher arrow built
    :type my_char: str
    :param max_length:length arrow built
    :type max_length: int
    :return: the arrow
    :rtype: NoneType
    """
    str1 = ''
    fact = 1
    while fact <= max_length:
        for i in range(max_length):
            str1 += (i * my_char)

        str1 = str1 + "\n"
        fact += 1
    # for i in range(max_length):
    #     str1 += (i * my_char)
    #     str1 = str1 + "\n"
    # for x in range(max_length):
    #     str1 += my_char * (max_length - x) + '\n'
    return str1
def main():
    print(arrow('*', 4))
if __name__ == '__main__':
    main()