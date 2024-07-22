# def dwa(num1, num2):
#     return num1 + num2
# res = dwa(2, 52)
# print(res)

def calculate(num1, num2):
    sum1 = str(num1 + num2)
    sum2 = str(num1 - num2)
    sum3 = str(num1 * num2)
    sum4 = str(num1 / num2)
    ans = [sum1, sum2, sum3, sum4]
    choice = int(input("Please enter which equation you want(0 - 3): "))
    if choice == 0:
        print(ans[0])
    elif choice == 1:
        print(ans[1])
    elif choice == 2:
        print(ans[2])
    elif choice == 3:
        print(ans[3])
    else:
        print("you didn't enter the correct number(0 - 3)")

calculate(2, 5)
