family = ["aleqsandre", "luka", "elene amaglobeli"]
print(family[0])
print(family[1])
print(family[2])
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[0], num[9])
num1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num2 = []
for i in num1:
    if i % 2 == 0:
        num2.append(1)
    else:
        num2.append(i)
    
print(num2)

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
surname = input("Please enter your surname: ")
email = input("Please neter your email: ")
all = [name, age, surname, email]
print(all)

surname1 = "gamsakhurdia"
for i in surname1:
    print(i)
