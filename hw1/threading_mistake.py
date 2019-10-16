# Найти и исправить ошибку (см файл task3.py), оставив многопоточность.
import concurrent.futures


def function(arg: int):
    n = 0
    for i in range(arg):
        n += 1
    return n  # result of single thread incrementation


def main():
    a = 0
    with concurrent.futures.ThreadPoolExecutor() as tpe:
        results = [tpe.submit(function, 1000000) for _ in range(5)]
        for z in concurrent.futures.as_completed(results):
            a += z.result()
    # threads = []
    # for _ in range(5):
    #     thread = Thread(target=function, args=(1000000,))
    #     thread.start()
    #     threads.append(thread)
    #
    # [t.join() for t in threads]
    print("----------------------", a)  # a is sum result of all the threads


main()
