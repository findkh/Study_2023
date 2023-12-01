# 86. 웹 브라우저를 실행하려면? ― webbrowser
import webbrowser

webbrowser.open_new('http://python.org')

# 90. 웹 페이지를 저장하려면? ― urllib
import urllib.request

def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as s:
        print(s)
        with open('wikidocs_%s.html' % page, 'wb') as f:
            print(f)
            f.write(s.read())

get_wikidocs("7")

# 91. 웹 페이지를 저장하는 다른 방법
import http.client

def get_wikidocs(page):
    conn = http.client.HTTPSConnection("wikidocs.net")
    conn.request("GET", "/12")
    r = conn.getresponse()
    with open('wikidocs_%s.html' % page, 'wb') as f:
        f.write(r.read())
    conn.close()


if __name__ == "__main__":
    get_wikidocs(1)