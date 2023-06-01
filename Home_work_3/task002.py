# Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#    1 2 3 4 5
#    6
#    -> 5

length = int(input("Введите количество элементов массива: "))
print("Введите массив целых чисел")
arr = list()
for i in range(length):
    number = int(input(f"Введите {i + 1} элемент массива: "))
    arr.append(number)

numberX = int(input("введите число для сравнения:"))
numberСomparison = arr[0]
for i in range(1,length):
    if abs(numberX - arr[i]) < (numberX - numberСomparison):
        numberСomparison = arr[i]
        if i == length - 1:
            print(f"ближайшее число к {numberX} в массиве {numberСomparison} ")
    elif abs(numberX - arr[i]) == numberX - numberСomparison:
        print(f"ближайшие числа к {numberX} в массиве {arr[i]} и {numberСomparison}")
        break


