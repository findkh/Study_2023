# 56. 비밀번호를 암호화하여 저장하려면?
# hashlib은 MD5, SHA256 등의 알고리즘으로 문자열을 해싱할 때 사용하는 모듈이다.

import hashlib
import os

def check_passwd():
    if os.path.exists('passwd.txt'):
        before_passwd = input('기존 비밀번호를 입력하세요:')
        m = hashlib.sha256()
        m.update(before_passwd.encode('utf-8'))
        with open('passwd.txt', 'r') as f:
            return m.hexdigest() == f.read()
    else:
        return True


if check_passwd():
    passwd = input('새로운 비밀번호를 입력하세요:')
    with open('passwd.txt', 'w') as f:
        m = hashlib.sha256()
        m.update(passwd.encode('utf-8'))
        f.write(m.hexdigest())
else:
    print("비밀번호가 일치하지 않습니다.")

# 57. 메시지 변조를 확인하려면?
# hmac는 비밀키와 해싱 기술을 사용하여 송수신자 간 메시지 변조를 확인할 수 있도록 하는 모듈이다.
import hmac
import hashlib

# 보냄
SECRET_KEY = 'PYTHON'

important_message = '이것은 누구나 볼 수 있는 원본 파일의 내용이다.'

with open('message.txt', 'w') as f:
    f.write(important_message)

with open('message_digest.txt', 'w') as f:
    m = hmac.new(SECRET_KEY.encode('utf-8'), important_message.encode('utf-8'),
                 hashlib.sha256)
    f.write(m.hexdigest())

# 확인
SECRET_KEY = 'PYTHON'

with open('message_digest.txt') as f:
    message_digest = f.read()

with open('message.txt') as f:
    message = f.read()
    m = hmac.new(SECRET_KEY.encode('utf-8'), message.encode('utf-8'),
                 hashlib.sha256)

    if m.hexdigest() == message_digest:
        print("메시지가 변조되지 않았습니다. 안전합니다.")

# 58. 안전한 난수를 생성하려면?
# secrets는 비밀 관리에 필요한 안전한 난수를 생성하고자 할 떄 사용하는 모듈이다.
import secrets
key = secrets.token_hex(16)
print(key)

key = secrets.token_hex(8)
print(key)