# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов,чем Петя и Сережа вместе?


sum = input("enter the number of cranes made by children: ")
try:
    testNumber = int(sum)
    if testNumber % 2 == 0:
         katia = int(sum) // 2
    else:
        katia = int(sum) // 2 + 1
    Petia = int(sum) // 2 // 2
    Seryuzha = Petia
    print(f"Seryozha made {Seryuzha} cranes, Katya {katia}, Petya {Petia}")
except ValueError:
    print("Not a number entered")
