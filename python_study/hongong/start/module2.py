# 외부 모듈
# cmd창에서 pip install 모듈 이름 설치
# beautiful soup : 웹 페이지 분석 모듈
# 태그를 여러 개 선택할 때는 select()함수, 하나를 선택할 때는 select_one()함수를 사용
# Beautiful Soup 모듈로 날씨 가져오기
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()


# Flask 모듈
from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터
def hello():
    return "<h1>Hello World</h1>"

# cmd 창에서 현재 파일이 있는 경로로 이동
# set FLASK_APP=module2.py 
# flask run
# 실행하면 아이피 주소가 뜸
