def my_mp3_playlist(file_path):
    """
    :param file_path: path to txt file
    :return:tuple of:
    index 0: that represents the longest song name in the file.
    index 1: sum of songs
    index 2: And a string representing the name of the performer that appears in the file
    The largest number of times assumed there was only one.
    :rtype: tuple
    """
    artis_list = []
    most_artist = ""
    count_artis = 0
    long_song = ""
    index_long_song = 0
    with open(file_path, 'r') as file:
        file_txt = file.readlines()
        for i in range(0, len(file_txt)):
            file_txt[i] = list(file_txt[i].split(";"))
            artis_list.append(file_txt[i][1])

        for x in range(len(file_txt)):
            file_txt[x][2] = (file_txt[x][2]).replace(":", "")
            if x == 0:
                long_song = file_txt[x][2]
                index_long_song = x
                count_artist = int(artis_list.count(file_txt[x][1]))
                most_artist = file_txt[x][1]

            if int(long_song) < int(file_txt[x][2]):
                long_song = file_txt[x][2]
                index_long_song = x
            # most_artist != file_txt[x][1] and
            if count_artis < artis_list.count(file_txt[x][1]):
                count_artist = artis_list.count(file_txt[x][1])
                most_artist = file_txt[x][1]
        tuple_func = (file_txt[index_long_song][0], len(file_txt), most_artist)
        return tuple_func


# C:\Users\Admin\Downloads\songs_long.txt
print(my_mp3_playlist(r"C:\Users\Admin\Downloads\songs_long.txt"))
def main():
    """
    main of all function

    :rtype: object
    """



if __name__ == '__main__':
    main()
