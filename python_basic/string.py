my_str = """
수달
엔터
하파
엔터
꼬꼬
"""

print(my_str)

# Formatting
my_str = 'my name is %s' % '하파'
print(my_str)
print('%d %d' % (3, 4))
print('%d %f' % (3, 3.14))

# '{}'.format()
myName = 'My name is %s' % 'Hafa'
print(myName)

myName2 = 'My name is {}'.format('Hafa')
print(myName2)

print('{} * {} = {}'.format(2,3,6))

print('{2} {1} {0}'.format(2,3,6)) #인덱스값 넣을 수 있음

# Indexing
str = 'PYTHON'
