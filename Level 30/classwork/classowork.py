def filter_odd(listofnums):
    ans = []
    for i in listofnums:
        if i % 2 == 0:
            ans.append(i)
    return ans
res = filter_odd([2, 6, 7, 3, 9])
print(res)

def introduce(name, age):
    return f"My name is {name} and i am {age} years old"


result = introduce("Luka",100)

print(result)



def even_sum(numbers_list):
    even = []
    ans = sum(even)
    for i in numbers_list:
        if i % 2 == 0:
            even.append(i)
    return ans

res = even_sum([5, 6, 1, 26, 7, 89])
print(res)


#MEORE

def odd_index_sum(numbers_lists):
    odd = []
    ans = sum(odd)
    for x in numbers_lists:
        if x % 2 == 0:
            odd.append(x)
    return ans

res = odd_index_sum([2, 6, 1, 26, 8, 2])
print(res)