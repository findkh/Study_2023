# 77. json 데이터를 다루려면?

import json

# 딕셔너리로 변환
with open('myinfo.json', encoding="utf-8") as f:
    data = json.load(f)
    print(data)

print(type(data))

data2 = {'name': '유관순', "birth":"0328", "age":18}
json_data = json.dumps(data2, ensure_ascii=False)
print(json_data)

# 78. 바이너리 데이터를 문자열로 바꾸려면?
import base64

def img_to_string(filename):
    ''' 파일명(filename)을 입력으로 받아 base64로 인코딩한 문자열을 리턴한다 '''
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read())

def string_to_img(s, filename):
    ''' base64로 인코딩된 문자열(s)과 파일명(filename)을 입력으로 받아 문자열을 파일로 저장한다. '''
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(s))

img_string = img_to_string('test.jpg')  # test.jpg 파일을 base64 문자열로 반환
string_to_img(img_string, 'result.jpg')  # base64 문자열을 result.jpg 파일로 저장

# 79. 문자열을 16진수로 변환
import binascii
print(binascii.unhexlify(b'507974686f6e204c696272617279'))

# 80. 아스키 외의 문자만 인코딩하려면
import quopri
print(quopri.decodestring('Python Library =EA=B3=B5=EB=B6=80').decode('utf-8'))

test = quopri.encodestring('Python Library 공부하는 수달'.encode('utf-8'))
print(test)

# 81. 바이너리 파일을 텍스트 파일로 바꾸려면?
import uu

# 이미지를 텍스트로 변환
uu.encode('test.jpg', 'result.txt')

# 텍스트를 다시 이미지로 변환
uu.decode('result.txt', 'test1.jpg')