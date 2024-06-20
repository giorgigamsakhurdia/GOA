numbers = []

start = int(input("Please enter start number: "))
end = int(input("Please enter end number"))

for i in range(start , end):
    numbers.append(i)

print(max(numbers))
print(min(numbers))
print(sum(numbers))