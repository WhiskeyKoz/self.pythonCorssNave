num1 = int(input("Please type a number between 1 - 7: "))
birth_date = "27.03.1970"
last_name = "Carey"
first_name = "Mariah"
hobbies = ["Sing", "Compose", "Act"]
identity_card = {1: first_name, 2: last_name, 3: birth_date, 4: hobbies}
if num1 == 1:
    print(identity_card[2])
elif num1 == 2:
    print(identity_card[3])
elif num1 == 3:
    print(len(identity_card[4]))
elif num1 == 4:
    print(identity_card[4][-1])
elif num1 == 5:
    identity_card[4].append("Cooking")
    print(identity_card[4])
elif num1 == 6:
    birth_date = ("27.03.1970",)
    print(identity_card[3])
elif num1 == 7:
    identity_card['age'] = 50
    print(identity_card["age"])
