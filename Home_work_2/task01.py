# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, 
# которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

count = input("enter the number of coins: ")
try:
    testCount = int(count)
    i = 0
    numbers = 0
    eagle = 0
    tails = 0
    while i < testCount: 
        number = input(f"If the {i+1} number is an eagle up,enter 0.If it is tails up, enter 1: ")
        try:
            testNumber = int(number)
            if testNumber == 0: 
                eagle = eagle + 1
                i = i + 1
            elif testNumber == 1:
                tails = tails + 1
                i = i + 1
            else:
                print("the entered data is incorrect")
        except ValueError:
            print("Not a number entered") 
    if eagle <= tails:
        print(f"you need to flip {eagle} coin")
    else:
        print(f"you need to flip {tails} coin")
except ValueError :
      print("Not a number entered") 