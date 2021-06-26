def are_files_equal(file1, file2):
    """
    check if the value of files was same and return true or false(in matching)
    :param file1: Path to file one
    :type: str
    :param file2: Path to file tow
    :type: str
    :return: if the value of file was same return true
    :rtype: bool
    """
    path_file1 = open(file1, "r")
    path_file2 = open(file2, "r")
    txt_file1 = path_file1.read()
    txt_file2 = path_file2.read()
    path_file1.close(), path_file2.close()
    return txt_file1 == txt_file2

def main():
    """
    main of all function

    :rtype: object
    """

    #r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt", r"C:\Users\Admin\OneDrive\שולחן העבודה\file2.txt"


    #C:\Windows\System32\file1
    #C:\Windows\System32\file2
if __name__ == '__main__':
    main()
