my_float = 3.5
print(my_float)
print(type(my_float))

str = '수달'
print(str)
print(type(str))

bool = True
print(bool)
print(type(bool))

# List
my_list = [1,2,3]
print(my_list)
print(type(my_list))

my_list2 = ['sudal', 'hafa', 'haha']
print(my_list2)
print(type(my_list2))

my_list2.append('ㅋㅋ')
print(my_list2)

# Tuple : 값 못바꿈
my_tuple = ('하하', 'ㅠㅠ', '어어어')
#my_tuple[0] = '이응이응' #'tuple' object does not support item assignment
print(my_tuple)

# dictionary : 키 값 쌍
my_dict = {'hafa': '여', 'sudal': '여'}
print(my_dict['hafa'])

# 형변환
my_str = 'sudal'
print(list(my_str))
print(type(list(my_str)))