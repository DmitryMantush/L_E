# Найти и исправить ошибку (см файл task3.py), оставив многопоточность.
from threading import Thread


def function(arg):
    a = 0
    for i in range(arg):
        a += 1
    print("----------------------", a)


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    # print("----------------------", a)  # a is a result of each thread


main()
