def change(x):
    """
    uxiliary function for us to track the second index
    :param x:the the tuple of list
    :type: tuple
    :return: index [1] of tuple
    :rtype str

    """

    return x[1]

def sort_prices(list_of_tuples):
    """
    sort the price frome all tuple frome the big to the small
    :param list_of_tuples: list of tuple was have each item and each price
    :type: tuple
    :return: list of tuple frome the big to the small
    :rtype list

    """

    return sorted(list_of_tuples, key=change, reverse=True)
products = ([('milk', '5.5'), ('bread', '5.51'), ('candy', '2.50'), ('bread', '9.0')])
print(sort_prices(products))