# 35. 파일 경로를 객체로 다루려면
# pathlib은 파일 시스템 경로를 문자열이 아닌 객체로 만들어 여러 가지 일을 할 수 있도록 하는 모듈이다.
import pathlib

# 현재 디렉터리의 모든 텍스트 파일을 archive라는 디렉터리로 이동하는 코드
for p in pathlib.Path.cwd().glob('*.txt'):
    new_p = p.parent.joinpath('archive', p.name)
    p.replace(new_p)

# 현재 디렉터리의 모든 파일을 조사하여 확장자별 개수 구하기
import collections

print(collections.Counter([p.suffix for p in pathlib.Path.cwd().iterdir()]))

# 36. 디렉터리의 구성을 알려면?
# os.path는 경로명과 파일명에 대한 유용한 함수를 제공하는 모듈이다.
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            search(filepath)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == '.py': 
                print(filepath)

search("C:/Users/findk/git/python_study") 

# 37. 여러 개의 파일을 한꺼번에 읽으려면?
# fileinput은 여러 개의 파일을 한꺼번에 처리할 때 사용하는 모듈이다.

import fileinput
import glob

with fileinput.input(glob.glob("*.text")) as f:
    for line in f:
        print(line)

# 38. 디렉터리와 파일을 비교하려면?
# filecmp는 파일 두 개 또는 디렉터리 두 곳을 비교할 때 사용하는 모듈이다.
import filecmp

fd = filecmp.dircmp('dir1', 'dir2')

for a in fd.left_only:
    print("dir1: %s" % a)

for b in fd.right_only:
    print("dir2: %s" % b)

for x in fd.diff_files:
    print("dir3: %s" % x)

# 39. 임시로 만든 파일을 이용하려면?
# tempfile은 임시 파일을 만들 떄 사용하는 모듈이다.
import random
import tempfile

def sumfile(f):
    result = 0
    for line in f.readlines():
        num = int(line)
        result += num
    return result


tf = tempfile.TemporaryFile(mode='w+')
for i in range(10):
    num = random.randint(1, 100)
    tf.write(str(num))
    tf.write("\n")

tf.seek(0)  # 파일 오프셋을 처음으로 이동
result = sumfile(tf)
tf.close()

print(result)

# 40. 파일을 찾으려면?
import glob

print('파일 찾기=============')
for filename in glob.glob("**/*.text", recursive=True):
    print(filename)

# 41. 특정 파일만 찾으려면?
# fnmatch는 파일 중에서 특정 패턴과 일치하는 파일을 찾을 때 사용하는 모듈이다.
import fnmatch

print('특정파일 찾기=============')
for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, 'a???[0-9].py'):
        print(filename)

# 42. 파일에서 무작위로 한 줄만 가져오기
# linecache는 파일에서 원하는 줄의 값을 읽을 때 사용하는 모듈이다.
import linecache

print('속담=====================')
no = random.randint(1, 100)
print(linecache.getline('saying.txt', no))