def shop(shoping_list):
    """
    collected shoping list and doing a acticen of a menu
    #1 Print the product list
    #2 Print the number of products
    #3 Print the answer to the test "Is the product on the list"
     the user will be prompted to press a product name
    #4 Print the answer to the test "How many times does a particular
     product appear" The user will be prompted to press a product name
    #5 Deleting a product from the User will be prompted to press a product
     name Only one product will be deleted
    #6 Add a product to the list The user will be prompted to enter a product name
    #7 Printing all products that are not valid A product is invalid if it
     is less than 3 years long or has characters other than letters
    #8 Remove all duplicates in the list
    #9 exit
    :param shoping_list:list of shoping prudact
    :type: str
    :return: What action will the user choose

    """

    newlist = []

    chose = 0
    legalList = ''
    shoping_list = list(shoping_list.split(","))

    while chose != 9:
        chose = int(input("Enter a number: "))
        if chose == 1:
            print(shoping_list)
        elif chose == 2:
            print("the item's you have is: ", len(shoping_list))
        elif chose == 3:
            item = input("check if this item in the order: ")
            if item in shoping_list:
                print("True")
            else:
                print("False")
        elif chose == 4:
            many = input("check who many times this item in the order: ")
            print(shoping_list.count(many))
        elif chose == 5:
            which = input("which item you want to delete: ")
            shoping_list.remove(which)
        elif chose == 6:
            add = input("which item you want to add: ")
            shoping_list.append(add)
        elif chose == 7:
            for char in shoping_list:
                if len(char) < 3 or char.isalpha() == False:
                    legalList = (legalList + char)
                    print(legalList)
        elif chose == 8:
            for char in shoping_list:
                if char not in newlist:
                    newlist.append(char)
            shoping_list = newlist


def main():
    theShopingList = input("please enter the shoping list: ")# apple,banana,coconut
    shop(theShopingList)
if __name__ == '__main__':
    main()