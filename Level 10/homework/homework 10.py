#homework numero 1

for i in range(21):
    print(i)
#homework numero 2

for i in range(1 , 11):
    print(i)
#homework numero 3

for i in range(0 , 101, 2):
    print(i)
#homework numero 4
num = int(input("Please enter your number: "))

if num > 0:
    print("it's a positive number")

if num < 0:
    print("it's a negative number")

if num == 0:
    print("it's equal to zero")

#homework numero 5

age = int(input("Please enter your age: "))
if age > 18:
    print("you are an adult")
else:
    print("you are a virgin")
#homework numero 6(final)

num1 = int(input("Please select number from 1 to 7: "))
if num1 == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("I told you to select number from 1 to 7.... should have listened")