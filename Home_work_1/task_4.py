# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).

length = input("Enter the length of the chocolate bar: ")
width = input("Enter the width of the chocolate bar: ")
number = input("enter the number of chocolate slices you want to break off: ")
try:
    testLength = int(length)
    testWidth = int(width)
    testNumber = int(number)
    if testLength * testWidth > testNumber:
        if testNumber % testLength == 0 or testNumber % testWidth == 0:
            print("You will succeed)))!!!")
        else:
            print("It is impossible to do this")
    else:
        print("You can't break off more of what is there")
except ValueError:
     print("Not a number entered")