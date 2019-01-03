cantP = int(input("We offer you several products, there's A, B, C and D \nHow many products do you wanna select: "))
A = (750 * 75)/100
B = (1500 * 25)/100
C = 500
D = 250
ContA = 0
ContB = 0
ContC = 0
ContD = 0
i = 0

while i < cantP:
    P = input("Add one of the products you wanna buy.\nWe have in stock: A, B, C, D\nType the letter here: ")
    if P == 'A':
        print('You have selected product A')
        ContA = ContA + 1
    elif P == 'B':
        print('You have selected product B')
        ContB = ContB + 1
    elif P == 'C':
        print('You have selected product C')
        ContC = ContC + 1
    elif P == 'D':
        print('You have selected product D')
        ContD = ContD + 1
    i = i + 1

totalA = ContA * A
totalB = ContB * B
totalC = ContC * C
totalD = ContD * D
totalN = totalA + totalB + totalC + totalD

print("The quantity of A products selected and the total amount of it is: ", ContA, ', and ', totalA)
print("The quantity of B products selected and the total amount of it is: ", ContB, ', and ', totalB)
print("The quantity of C products selected and the total amount of it is: ", ContC, ', and ', totalC)
print("The quantity of D products selected and the total amount of it is: ", ContD, ', and ', totalD)
print("The total amount of the purchase is: ", totalN)