def range_sum(numbers, start, end):
    return sum(x for x in numbers if start <= x <= end)


input_numbers = map(int, input().split())
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))
