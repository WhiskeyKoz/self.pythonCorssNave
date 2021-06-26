def count_chars(my_str):
    """
    collected a string and returns a dictionary so that each member of it is a pair consisting
    of a character key from the string passed to The Exclusion
    :param my_str: string
    ::type my_str: str
    :return: returns a dictionary so that each member of it is a pair consisting
    of a character key from the string passed to The Exclusion
    :rtype: dict
    """
    dict_count = {}
    my_str = my_str.replace(" ", "")
    for x in my_str:
         dict_count[str(x)] = my_str.count(x)
    return dict_count
def main():
    magic_str = "abra cadabra"
    print(count_chars('Abra Cabrera'))
if __name__ == '__main__':
    main()