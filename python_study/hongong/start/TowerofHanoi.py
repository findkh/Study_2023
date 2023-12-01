# # 3개의 기둥과 크기가 다른 원판이 원뿔 형태로 존재한다.
# # 규칙
# # - 한 번에 한 개의 원판만 옮길 수 있다.
# # - 큰 원판이 작은 원판 위에 있어서는 안된다.

count = 0

def hanoi(disc, start, main, sub):
    global count
    if disc == 1:
        count += 1
        # print("sub기둥에서 main기둥으로 이동, count : {}".format(count))
        # print(start, "->", main, "count=", count)
    else :
        hanoi(disc -1, start, sub, main)
        count += 1
        hanoi(disc -1, sub, main, start)
        # print(start, "->", main, "count=", count)
        # print("start기둥에서 sub기둥으로 이동, count : {}".format(count))

disc = int(input("원판의 개수를 입력하세요: >"))
hanoi(disc, "A", "B", "C")
print("2 ** disc - 1 = ", 2**disc -1)
print(count)