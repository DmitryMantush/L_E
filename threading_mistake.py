# Найти и исправить ошибку (см файл task3.py), оставив многопоточность.
import concurrent.futures

a = 0


def function(arg: int):
    n = 0
    for i in range(arg):
        n += 1
    return n  # result of single thread incrementation


def main():
    with concurrent.futures.ThreadPoolExecutor() as tpe:
        results = [tpe.submit(function, 1000000) for _ in range(5)]
        for z in concurrent.futures.as_completed(results):
            global a
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
