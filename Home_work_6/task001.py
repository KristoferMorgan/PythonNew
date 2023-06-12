# Заполните строку элементами арифметической прогрессии.Ее первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-ого члена прогрессии:
# an = a1 + (n - 1) * d
# Каждое число вводиться с новой строки.


from CustomFuncs import enterStrForm 

a = int(input("Enten fist number in string: "))
n = int(input("Enter long string:  "))
d = int(input("Enter the number for the difference in the formula: "))
print(f"Outpu of your string: {enterStrForm(a,n,d)}")