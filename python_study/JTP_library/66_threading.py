# 66. 스레드를 이용하여 병렬로 처리하려면?
# threading은 스레드를 이용하여 한 프로세스에서 2가지 이상의 일을 동시에 실행할 수 있게 하는 모듈이다.

import urllib.request

def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'

import time

start = time.time()
pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]

for page in pages:
    get_wikidocs(page)

end = time.time()
print("수행시간: %f 초" % (end - start))

# 스레드 사용

def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'

import threading

start = time.time()
pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
threads = []
for page in pages:
    t = threading.Thread(target=get_wikidocs, args=(page, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()  # 스레드가 종료될 때까지 대기

end = time.time()

print("수행시간: %f 초" % (end - start))

# 67. 멀티 프로세스를 이용하여 병렬로 처리
# multiprocessing은 멀티 프로세스를 활용하여 2가지 또는 그 이상의 일을 동시에 실행할 수 있게 하는 모듈이다.

def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)

start = time.time()

for i in range(4):
    heavy_work(i)

end = time.time()

print("수행시간: %f 초" % (end - start))

def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import threading

    start = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=heavy_work, args=(i, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print("수행시간: %f 초" % (end - start))

def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import multiprocessing

    start = time.time()
    procs = []
    for i in range(4):
        p = multiprocessing.Process(target=heavy_work, args=(i, ))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 대기

    end = time.time()

    print("수행시간: %f 초" % (end - start))

# 68. 병렬로 작업을 처리하려면
# 스레드를 구현하려면 threading 모듈을 사용하고 멀티 프로세스 프로그램을 구현하려면 multiprocessing 모듈을 사용해야 한다. 
# 하지만 일반적으로 concurrent.futures 모듈을 사용하면 같은 규칙으로 스레드와 멀티 프로세스 코드를 더 쉽게 작성할 수 있다.

def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)
    return result  # 결과를 반환하도록 변경

if __name__ == '__main__':
    import concurrent.futures

    start = time.time()

    total_result = 0
    pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)

    procs = []
    for i in range(4):
        procs.append(pool.submit(heavy_work, i))

    for p in concurrent.futures.as_completed(procs):
        total_result += p.result()

    end = time.time()

    print("수행시간: %f 초" % (end - start))
    print("총결괏값: %s" % total_result)

def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'


if __name__ == '__main__':
    import time
    import concurrent.futures

    start = time.time()

    pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    threads = []
    for page in pages:
        threads.append(pool.submit(get_wikidocs, page))

    concurrent.futures.wait(threads)  # 스레드가 모두 종료될 때까지 대기

    end = time.time()

    print("수행시간: %f 초" % (end - start))

# 70 원하는 작업을 원하는 시간에 실행하려면?
import sched

start = time.time()

def print_a(a):
    print(time.time() - start)
    print(a)

def print_b(b):
    print(time.time() - start)
    print(b)

def print_c(c):
    print(time.time() - start)
    print(c)

s = sched.scheduler()
s.enter(5, 1, print_a, ('A',))  # 5초 후에 실행
s.enter(3, 1, print_b, ('B',))  # 3초 후에 실행
s.enter(7, 1, print_c, ('C',))  # 7초 후에 실행
s.run()