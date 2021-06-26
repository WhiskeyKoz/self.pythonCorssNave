pilandrom = (input("Enter a word: ").lower()).replace(" ", "")
if pilandrom[::-1] == pilandrom:
    print("OK")
else:
    print("NOT")

