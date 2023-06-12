# Определите  индексы элементов списка,
# значения которых принадлежат заданному диапазону(
# т.е. не меньше заданного минимума и не больше заданного максимума)


from CustomFuncs import indexRange

myList = (10,22,41,234,3,34,3,2,5,1,56,23,22,44,1002,234,99)
rangeMin = int(input("Enter min number for the range: "))
rangeMax = int(input("Enter max number for the range: "))
print(f"Indexes your range:{indexRange(myList,rangeMin,rangeMax)}")