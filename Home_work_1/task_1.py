# Найдите сумму трехзначного числа

number = input('enter a three-digit number: ')
sum = 0
try:
    testNumber = int(number)
    if 99 < testNumber < 999:
        for i in number:
            sum = int(sum) + int(i)
        print(f"The sum of the digita in your number is {sum}")
    else:
        print("A non-three-digit number has been entered")
except ValueError:
    print("Not a number entered")