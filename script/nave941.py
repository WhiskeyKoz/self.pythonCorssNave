from collections import Counter
def choose_word(file_path, index):
    """
    the function return tuple of The number of different words in the file
    that is, does not include repetitive words and word in index was the function was collected
    :param file_path: path to txt file
    :type: str
    :param index: index in a word in txt file
    :type: int
    :return:tuple of The number of different words in the file
    that is, does not include repetitive words and word in index was the function was collected
    :rtype: int and str
    """
    with open(file_path, "r") as x:
        redeing = x.read()
        redeing = redeing.split(" ")
        for i in range(0, len(redeing)):
            redeing[i] = "".join(redeing[i])
        x = Counter(redeing)
        none_duplicates_list = " ".join(x.keys())
        len_list = none_duplicates_list.split(" ")
        len_redeing = len(redeing)
        while index > len_redeing:
            index -= len_redeing
        end_tuple = (len(len_list), redeing[index-1])
        return end_tuple

def maim():

    print(choose_word(r"C:\Users\Admin\OneDrive\שולחן העבודה\file1.txt", 3))
if __name__ == '__main__':
    maim()