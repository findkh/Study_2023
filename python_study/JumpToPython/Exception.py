# IndexError가 발생할 때 오류 메시지를 출력하는 소스 작성
a = [1,2]
try:
    print(a[2])
except IndexError as e:
    print(e)

# 에외 만들기
class MyError(Exception):
    #pass
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick('천사')
say_nick('바보')

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")