def mult_tuple(tuple1, tuple2):
    """
    Returns a tapel containing all
     pairs that can be created from
     the metaple organs passed as arguments.
    :param tuple1: some int tuple
    :type: tuple
    :param tuple2: some int tuple
    :type: tuple
    :return: Returns a tapel of all couple
    :rtype: tuple
    """
    new_tuple = ()
    for couple in tuple1:
        for n2 in tuple2:
            new_tuple += (couple, n2), (n2, couple)
    return new_tuple

def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))
if __name__ == '__main__':
    main()