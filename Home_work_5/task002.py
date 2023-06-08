# : Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать цикл

from CustonFuncs import recursionSum

numberA = int(input("enter one number: "))
numberB = int(input("enter two number: "))
print(f"Sum your number = {recursionSum(numberA,numberB)}")