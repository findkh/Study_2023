# 54. csv 파일을 읽고 쓰려면?

import csv

result = []
with open('score.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for line in reader:
        average = sum(map(int, line[1].split(','))) / 2
        line.append(average)
        result.append(line)

with open('score_result.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerows(result)

# 55. 설정 파일에서 정보를 읽으려면?
# ini 파일은 프로그램 정보를 저장하는 텍스트 문서로 섹션과 그 섹션에 해당하는 키 = 값으로 구성된다.
#configparser는 이러한 형식의 ini 파일을 처리할 떄 사용하는 모듈이다.
import configparser

config = configparser.ConfigParser()
config.read('ftp.ini')
ftp2_port = config['FTP2']['PORT']

print(ftp2_port)