
Number_list = [1,3,8,9,13,21,31]

even = filter(lambda x: x % 2 == 0, numbers)
odd = filter(lambda x: x % 2 == 1, numbers)

print(list(even)) 
print(list(odd)) 
