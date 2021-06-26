def inverse_dict(my_dict):
    """
    collected some dictionary and return a new dictionary of this dictionary the key in the last dictionary is the value
    and the value in the last dictionary is the key
    :param my_dict: some dictionary
    :type my_dict: dict
    :return: new dictionary of this dictionary the key in the last dictionary is the value
    and the value in the last dictionary is the key
    :rtype: dict
    """
    keys_dict = []
    values_dict = []
    for key, value in my_dict.items():
        keys_dict.append(key)
        values_dict.append(value)
    new_dict = {}
    x = 0
    place = 1

    while x < len(values_dict):
        new_dict[values_dict[x]] = [keys_dict[x]]
        for i in values_dict[place:]:
            if values_dict[x] == i:
                new_dict[values_dict[x]] = [keys_dict[x], keys_dict[place]]
                x += 1
                place += 1
        x += 1
        place += 1
    print(new_dict)

def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    inverse_dict(course_dict)
if __name__ == '__main__':
    main()