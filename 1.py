#-*- coding:utf-8 -*-
__author__ = 'tony'

from threading import Thread
import time

# def my_counter():
#     i = 0
#     for _ in range(100000000):
#         i = i + 1
#     return True
#
# def main():
#     thread_array = {}
#     start_time = time.time()
#     for tid in range(2):
#         t = Thread(target=my_counter)
#         t.start()
#         thread_array[tid] = t
#
#     for i in range(2):
#         thread_array[i].join()
#     end_time = time.time()
#     print("Total time:{}".format(end_time - start_time))
#
# if __name__ == "__main__":
#     main()

import time
from threading import Thread
from multiprocessing import Process
from timeit import Timer

def countdown(n):
    while n > 0:
        n-=1

def t1():
    COUNT = 100000000
    thread1 = Thread(target=countdown,args=(COUNT,))
    thread1.start()
    thread1.join()

def t2():
    COUNT = 100000000
    thread1 = Process(target=countdown,args=(COUNT//2,))
    thread2 = Process(target=countdown,args=(COUNT//2,))
    thread1.start();thread2.start()
    thread1.join();thread2.join()

def t3():
    COUNT = 100000000
    p1 = Process(target=countdown, args=(COUNT // 2,))
    p2 = Process(target=countdown, args=(COUNT // 2,))
    p1.start();p2.start()
    p1.join();p2.join()

if __name__ == "__main__":
    t = Timer(t1)
    print('countdown in one thread:',t.timeit(1))

    t = Timer(t2)
    print('countdown in two thread:',t.timeit(1))

    t = Timer(t3)
    print('countdown user two process',t.timeit(1))





