# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k),
# не превосходящие числа N.

number = input("enter the last power of 2: ")
try:
    testnumber = int(number)
    count = 1
    while 2 ** count <= testnumber:
        print(f"2 in degree {count} = {2 ** count}")
        count = count + 1
except ValueError:
    print("Not a number entered")