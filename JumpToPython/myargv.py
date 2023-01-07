import sys

numbers = sys.argv[1:]
result = 0
for num in numbers:
    result += int(num)
    #print(result)

print(result)