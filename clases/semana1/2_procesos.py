'''
Tema 2
Created on 24 jul. 2023

@author: eliumontoya
'''
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    print('hello', name)
    info('function f')
    i = 0
#    while True:
    while i<1000:
        i = i+1


if __name__ == '__main__':
    info('main line')#52494
    p = Process(target=f, args=('bob',))
    p.start() #52496
    ##p.join()#52494
    p2 = Process(target=f, args=('juan',))
    p2.start()
    #p2.join()#52494
    