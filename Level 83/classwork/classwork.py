def Math_equal(number, number1, math_thing):
    if math_thing == "+":
        print(number + number1)
    elif math_thing == "-":
        print(number - number1)
    elif math_thing == "*":
        print(number * number1)
    elif math_thing == "/":
        yes =  number / number1
        if int(yes) != yes:
            print("error")
        else:
            print(int(yes))

Math_equal(10, 5, "/")
