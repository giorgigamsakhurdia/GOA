fruits = ["banana", "apple", "melon"]
for i in fruits:
    if i == "apple":
        continue       
    elif i == "melon":
        break
    print(i)



cars = ["ferrari", "bugatti", "mustang"]
for i in cars:
    if i == "ferrari":
        break
    else:
        continue

print(i)



superhumans = ["batman", "spiderman", "flash"]
for i in superhumans:
    if i == "spiderman":
        print("goat")        
        continue
    else:
        print("mid")
        continue
    print(i)