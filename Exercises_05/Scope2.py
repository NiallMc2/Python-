def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        
    return False
            

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)
# 9 was not found because 9 was not in the number list, if you change to any number between 1-8 it will be found 
# else: return False changes none to False
 
