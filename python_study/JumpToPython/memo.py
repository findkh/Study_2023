import sys

option = sys.argv[1]
memo = sys.argv[2:]

str = ''
for i in memo:
    str += i + ' '

# 입력 받은 값 프린트
# print(option)
# print(memo)

if option == '-a':
    f = open('memo.txt', 'a')
    f.write(str)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

