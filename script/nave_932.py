def my_mp4_playlist(file_path, new_song):
    """
    The function writes to the file the string that represents the name of a new song
    :param file_path: path to txt file
    :type: str
    :param new_song: name of a new song to write.
    :type: str
    :return: print the value txt of the file
    :rtype: no type becauose  print
    """
    file = open(file_path, 'r')
    list_txt_file = file.read().split("\n")
    file.close()
    #print(list_txt_file)
    if len(list_txt_file) >= 2:
        list_txt_file[2] = list_txt_file[2].split(";")
        list_txt_file[2][0] = new_song
        list_txt_file[2] = ";".join(list_txt_file[2])
    else:
        for num in range(len(list_txt_file), 2):
            list_txt_file += [" "]
        list_txt_file += [new_song + ";"]
    print("\n".join(list_txt_file))
    file = open(file_path, 'w')
    for song in list_txt_file:
        file.write(song + '\n')

my_mp4_playlist(r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt", "hello")
