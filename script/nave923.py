def who_is_missing(file_name):
    """
    find the number wes disappear and update the file with the right number order
    :param file_name: path of file txt
    :type: str
    :return: the number was disappear
    :rtype: int

    """
    x = 0
    with open(file_name, 'r') as file:
        file_txt = file.readlines()
        check_disappear = 0
        for char_in_txt in file_txt:
            while x != len(char_in_txt):
                x += 1
                check_disappear += 1
                if not (str(check_disappear) in char_in_txt):
                    new_file = open(r"C:\Users\Admin\OneDrive\שולחן העבודה\file2.txt", "w")
                    new_file.write(str(check_disappear))
                    new_file.close()
                    return int(check_disappear)


def main():
    """
    main of all function

    :rtype: object
    """
    # r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txְt", r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt"
    print(who_is_missing(r"C:\Users\Admin\Downloads\findMe2.txt"))


if __name__ == '__main__':
    main()
