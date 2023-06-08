# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
from CustonFuncs import powerOfNumber


NumberA = int(input("enter number A: "))
NumberB = int(input("enter number B: "))
print(f"the power of the number A = {powerOfNumber(NumberA,NumberB)}")