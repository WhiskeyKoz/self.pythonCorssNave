num = int(input("Enter three digits (each digit for one pig): "))
sum_of_piges = int((num % 100) % 10) + int((num % 100) // 10) + int(num // 100)
avrege_piges = sum_of_piges // 3
check_clising = (sum_of_piges % 3) == 0
print(sum_of_piges)
print(sum_of_piges // 3)
print(sum_of_piges % 3)
print(check_clising)
