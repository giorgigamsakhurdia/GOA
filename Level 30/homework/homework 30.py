def odd_index_sum(numbers):
    return sum(numbers[i] for i in range(len(numbers)) if i % 2 != 0)

res = odd_index_sum([2, 6, 7, 2, 6])
print(res)  