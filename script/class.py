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
    password = 'adf'
    password.startswith('abc')
    str1 = ''
    avrege = x // 3
    for i in range(max_length):
        str1 += i * my_char
        str1 += '\n'
    if == 'abc' or password == 'password' or password == 'qwerty' or password == 'love':
        for x in range(max_length):
            str1 += my_char * (max_length - x)
            str1 += '\n'
    return str1
def main():
    print(arrow('*', 1))
if __name__ == '__main__':
    main()