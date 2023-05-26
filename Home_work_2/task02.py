#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

product = input("enter the product of the numbers: ")
try:
    testProduct = int(product)
    if  0 < testProduct < 1001:
        sum = input("enter the sum of the numbers: ")
        try:
            testSum = int(sum)
            if 0 < testSum < 1001:
                 for x in range(testProduct):
                     for y in range(testSum):
                         if testSum == x + y and testProduct == x * y:
                             print(f"the values of x and y = {x} and {y} ")
            else:
                print("enter number < 1001") 
        except ValueError:
            print("Not a number entered")
    else:
        print("enter number < 1000")
except ValueError:
        print("Not a number entered")
