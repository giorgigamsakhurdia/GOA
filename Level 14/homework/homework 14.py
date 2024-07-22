#IF 



a = 298321
b = 3
if b > a:
    print("b is greater then a")
elif a > b:
    print("a is greater then b")
else:
    print("they are equal")



a = int(input("Please enter your desire number: "))
b = int(input("Please enter your desire number: "))
if b > a:
    print("b is greater then a")
elif a > b:
    print("a is greater then b")
else:
    print("they are equal")


for i in range(5):
    print(i)
    if i == 3:
        break



password = "giorgi"
your_password = input("Please enter your password: ")
if your_password == password:
    print("you are authorized")
else:
    print("it's not your password,try again!")



num = int(input("Please enter your number form 1-10: "))
correct = 6
if num == 6:
    print("You Won!!!")
else:
    print("You Lost!!!")


x = 5
b = 6
if b > x or x == b:
    print("b is greater")


a = 76
t = 76

if a == t and t == a:
    print("it's equal")