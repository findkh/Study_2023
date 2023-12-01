# 59. 문자열을 파일처럼 다루려면?

import csv
import io

def execute(f):
    result = []
    reader = csv.reader(f)
    for line in reader:
        one = int(line[0])
        two = int(line[1])
        three = one+two
        line.append(three)
        result.append(line)
    return result

src = '''\
20,40
50,90
77,22
'''

with io.StringIO(src) as f:  # 문자열을 파일객체럼 만든다.
    result = execute(f)
    print(result)

# 60. 명령행 옵션을 지정하여 실행하려면?
# argparse : 파이썬 스크립트의 명령행 옵션을 파싱할 때 사용하는 모듈이다.
import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("합은 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("곱은 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))

# 61. 디버기용 로그를 남기려면?
from logging.config import dictConfig
import logging

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})

def myfunc():
    logging.debug("함수가 시작되었습니다.")

myfunc()

# 62. 입력한 비밀번호를 감추려면?
import getpass
passwd = getpass.getpass("Password: ")

# 64. 시스템 정보를 알아보려면?
import platform
info = platform.uname()
print(info)