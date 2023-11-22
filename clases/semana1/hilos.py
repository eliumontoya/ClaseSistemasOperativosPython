'''
Created on 24 jul. 2023

@author: eliumontoya
'''
import threading
import os


#FUNCIÓN A EJECUTAR
def cuenta(n, name):
    count=n
    print(name ," Parent: ", os.getppid(), ". ID:",os.getpid())

    while count<10:
        #print(count)
        #count+=1
        pass

#CREAMOS PROCESOS A EJECUTAR EN PARALELO.        
t = threading.Thread(target = cuenta, args =(1, 'thread1') )
t2 = threading.Thread(target = cuenta, args =(2, 'thread2') )
t3 = threading.Thread(target = cuenta, args =(3, 'thread3') )

#INICIAMOS PROCESOS.
t.start() 
#t.join()
t2.start()
#t2.join()
t3.start()
t3.join()