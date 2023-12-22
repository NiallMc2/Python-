def even_number(number_test):
    for iterate_number in number_test:
        if iterate_number % 2 ==0:
            return True
    return False

# list of numbers to go through
numbers = [1,2,3,4,5,6,7,8,9,10]
result = even_number(numbers)
print(result)
