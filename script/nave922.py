def copy_file_content(source, destination):
    """
    copy the txt in source file to destination txt file
    doing action on the txt file in matching to varible: action
    :param source: Path to txt file for copy
    :type: str
    :param destination: Path to txt file for past from the copy from source
    :type: str
    :return: noting
    :rtype:not type
    """
    path_source = open(source, "r")
    path_destination = open(destination, "w")
    txt_source = path_source.read()
    path_destination.write(txt_source)
    path_source.close()
    path_destination.close()


def main():
    """
    main of all function

    :rtype: object
    """
    # r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt", r"C:\Users\Admin\OneDrive\שולחן העבודה\file2.txt"
    copy_file_content(r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt",
                      r"C:\Users\Admin\OneDrive\שולחן העבודה\file2.txt")


if __name__ == '__main__':
    main()
