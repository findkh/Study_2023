import textwrap
import re

# textwrap.shorten() : 문자열을 원하는 길이에 맞게 줄여 표시
a = textwrap.shorten('Life is too short, you need python', width=15)
print(a)

b = textwrap.shorten('수달은 쉬고 싶어요.... ㅋㅋㅋㅋ', width=15)
print(b)

c = textwrap.shorten('언능 공부하고 쉬어야겠다......', width=15)

# textwrap.wrap() : 긴 문자열을 원하는 길이로 줄바꿈할 때 사용
long_text = 'Developer Sudal is studying again today.' * 10
# result = textwrap.wrap(long_text, width=70)
# print('\n'.join(result))

result = textwrap.fill(long_text, width=70)
print(result)

data = """
홍길동의 주민등록번호는 790123-4567890
그리고 고길동의 주민등록번호는 709876-5432109
그렇다면 누가 형님일까요?
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub('\g<1>-*******', data))