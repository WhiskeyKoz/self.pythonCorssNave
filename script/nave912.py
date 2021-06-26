def are_files_equal(file, action):
    """
    doing action on the txt file in matching to varible: action
    :param file: Path to txt file
    :type: str
    :param action: name of the acticn was the user want to do
    :type: str
    :return: in matching to the method_name
    :rtype:not type beacuos printed
    """

    if action == "sort":
        new_list = []
        with open(file, 'r') as file:
            for line in file:
                for word in line.split():
                    if not (word in new_list):
                        new_list.append(word)
        print(sorted(new_list))
        # txt_file = path_file.read()
        # # for x in range(len(txt_file)):
        # #     if txt_file[x] == "\n":
        # #         txt_file[x] = txt_file[x].replace("\n", "")
        # txt_file = txt_file.replace('\n', ' ')
        # print(list(dict.fromkeys(sorted(txt_file.split(" ")))))
    elif action == "rev":
        path_file = open(file, "r")
        rev_txt = path_file.readlines()
        for line in rev_txt:
            print(line[::-1])
        path_file.close()
    elif action == "last":
        with open(file, 'r') as file:
            txt_last = file.readlines()
            number = int(input("Enter a number: "))
            for line in range(number, len(txt_last)):
                print(txt_last[line])


def main():
    """
    main of all function

    :rtype: object
    """
    path_file = input("Enter a file path: ")
    method = input("Enter a task: ")

    #r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt", r"C:\Users\Admin\OneDrive\שולחן העבודה\sampleFile.txt"
    are_files_equal(path_file, method)
if __name__ == '__main__':
    main()
