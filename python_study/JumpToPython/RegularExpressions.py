import re

data = """
park 800905-1049118
lee 800905-1049119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# 문자 클래스
# \d : 숫자와 매치, [0-9]와 동일
# \D : 숫자가 아닌 것과 매치, [^0-9]와 동일
# \s : whitespace 문자(space, tab)와 매치, [ \t\n\r\f\v]와 동일한 표현식
# \S : whitespace가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식
# \w : 문자+숫자와 매치, [a-zA-Z0-9]와 매치
# \W : 문자+숫자가 아닌 것과 매치, [^a-zA-Z0-9]와 매치


# Dot(.)
# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치된다.
# a.b : a와 b 사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치

# 반복(*)
# ca*t : 문자 바로 앞에 있는 a가 0번 이상 반복되는 매치 (0부터 무한대로 반복 가능)

# 반복(+)
# ca+t : + 문자 바로 앞에 있는 a가 1번 이상 반복되는 매치

# 반복
# {m}
# ca{2}t = "c + a(반드시 2번 반복) + t"
# {m,n}
# ca{2,5} = "c + a(2번~5번 반복) + t"
# ?
# ab?c : b가 0~1번 사용되면 매치

# re 모듈
# match() : 문자열의 처음부터 정규식과 매치되는 조사
# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
# finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
p = re.compile('[a-z]+')
m = p.match('python')
m2 = p.match('3python')
print(m) #<re.Match object; span=(0, 6), match='python'>
print(m2) #None

# search 
m3 = p.search('python') #<re.Match object; span=(0, 6), match='python'>
print(m3)
m4 = p.search('3python') #<re.Match object; span=(1, 7), match='python'>
print(m4)

#findall
result = p.findall("life is too short")
print(result) #['life', 'is', 'too', 'short']

# finditer
result = p.finditer("life is too short")
print(result) #<callable_iterator object at 0x000002104313B700>

for r in result : print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

# match 객체의 메서드
# group() : 매치된 문자열을 돌려준다.
# start() : 매치된 문자열의 시작 위치를 돌려준다.
# end() : 매치된 문자열의 끝 위치를 돌려준다.
# span() : 매치된 문자열의 해당하는 튜플을 돌려준다.
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# 모듈 단위 실행
m = re.match('[a-z]+', 'python').group()
print(m)

# 컴파일 옵션
# DOTALL : S : dot 문자가 줄바꿈 문자를 포마하여 모든 문자와 매치한다.
# IGNORECASE : I : 대소문자에 관계없이 매치한다.
# MULTILINE : M : 여러 줄과 매치한다.(^, $ 메타 문자의 사용과 관련 있는 옵션이다.)
# VERBOSE : X : verbose 모드를 사용한다(정규식을 보기 편하게 만들고 주석을 사용할 수 있다.)

# DATALL, S
p = re.compile('a.b')
m = p.match('a\nb')
print(m) # None

p2 = re.compile('a.b', re.DOTALL)
m2 = p2.match('a\nb')
print(m2) #<re.Match object; span=(0, 3), match='a\nb'>

# IGNORECASE, I
p3 = re.compile('[a-z]', re.I)
print(p3.match('python')) #<re.Match object; span=(0, 1), match='p'>
print(p3.match('PYTHON')) #<re.Match object; span=(0, 1), match='p'>

# MULTILINE, M
p4 = re.compile("^python\s\w+")
data = """python one
live is too short
python two
you need oython
python three"""
print(p4.findall(data)) # ^ 메타 문자 때문에 첫 번쨰 줄만 매치된다. ['python one']

p5 = re.compile("^python\s\w+", re.MULTILINE)
print(p5.findall(data)) # ['python one', 'python two', 'python three']

# VERBOSE, X
charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
  | [0-9]+          # Decimal form
  | x[0-9a-fA-F]+   # Hexadecimal form
)
                    # Trailing semicolon
""", re.VERBOSE)

# 메타 문자

# | : or과 동일한 의미로 사용된다.
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m) # <re.Match object; span=(0, 4), match='Crow'>

# ^ : 메타 문자는 문자열의 맨 처음과 일치함
print(re.search('^Life', 'Life is too short')) # <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life')) # None

# $ : ^ 메타 문자와 반대, 문자열
print(re.search('short$', 'Life is too short')) #<re.Match object; span=(12, 17), match='short'>

# A : 문자열의 처음과 매치된다. re.MULTILINE과 사용할 경우 줄과 상관 없이 전체 문자열의 처음하고 매치된다.

# Z : 문자열의 끝과 매치된다. re.MULTILINE 옵션 사용시 전체 문자열의 끝과 매치된다.

# /b : 단어 구분자다. 
# 보통의 단어는 whitespace에 의해 구분된다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all')) #e.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm')) #None -> class 문자열이 포함되어 있찌만 whitespace로 구분된 단어가 아니므로 매치되지 않는다.

# \B : /b와 반대로 whitespace로 구분된 단어가 아닌 경우에만 매치된다.
p = re.compile(r'\Bclass\B')
print(p.search('no class at all')) #None
print(p.search('the declassified algorithm')) #<re.Match object; span=(6, 11), match='class'>

# 그루핑
# 그룹을 만들어주는 메타 문자는 ()이다
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m) #<re.Match object; span=(0, 9), match='ABCABCABC'>

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-5678")
print(m) #<re.Match object; span=(0, 18), match='park 010-1234-5678'>

# () 사용하여 그룹으로 만들면 그루핑된 부분의 문자열만 뽑아 낼 수 있다.
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-5678")

print(m.group(0)) #park 010-1234-5678
print(m.group(1)) #park
print(m.group(2))


# 전방탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

# 긍정형 전방 탐색 : (?=...) : ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방 탐색 : (?!...) : ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group())