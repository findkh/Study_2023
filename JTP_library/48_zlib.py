# 48. 데이터 크기를 줄여 전송하려면? 
# zlib은 데이터를 압축하거나 해제할 때 사용하는 모듈이다.

data = "Life is too short, You need python." * 10000
print(len(data))

import zlib

data = "Life is too short, You need python." * 10000
compress_data = zlib.compress(data.encode(encoding='utf-8'))
print(len(compress_data)) 

org_data = zlib.decompress(compress_data).decode('utf-8')
print(len(org_data))

# 49. 데이터를 압축하여 파일로 저장하려면?
# gzip은 파일을 압축하거나 해제할 때 사용하는 모듈이다.
import gzip

data = "Life is too short, you need python." * 10000

with gzip.open('data.txt.gz', 'wb') as f:
    f.write(data.encode('utf-8'))  # 저장한 파일의 크기는 1097바이트

with gzip.open('data.txt.gz', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data

# 50. bzip2 알고리즘으로 압축
import bz2

data = "Life is too short, You need python." * 10000
compress_data = bz2.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 163 출력

org_data = bz2.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

assert data == org_data

# 압축 해제
with bz2.open('data.txt.bz2', 'wb') as f:
    f.write(data.encode('utf-8'))

with bz2.open('data.txt.bz2', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data

# 51. LZMA 알고리즘으로 압축
import lzma

compress_data = lzma.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 220 출력

org_data = lzma.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

assert data == org_data

# 압축 해제
with lzma.open('data.txt.xz', 'wb') as f:
    f.write(data.encode('utf-8'))

with lzma.open('data.txt.xz', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data

# 52. 여러 파일을 zip으로
import zipfile

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()

# 53. 여러 파일을 tar로 합치려면?
# tarfile은 여러 개의 파일을 tar 형식으로 합치거나 이를 해제할 때 사용하는 모듈
import tarfile

# 여러파일 합치기
with tarfile.open('mytext.tar', 'w') as mytar:
    mytar.add('a.txt')
    mytar.add('b.txt')
    mytar.add('c.txt')

# # 여러파일 해제하기
with tarfile.open('mytext.tar') as mytar:
    mytar.extractall()

with tarfile.open('mytext.tar') as mytar:
    mytar.extract('a.txt')

# 파일 압추갛여 묶기
# 여러파일 합치기
with tarfile.open('mytext2.tar.gz', 'w:gz') as mytar:
    mytar.add('a.txt')
    mytar.add('b.txt')
    mytar.add('c.txt')

# 여러파일 해제하기
with tarfile.open('mytext2.tar.gz') as mytar:
    mytar.extractall()