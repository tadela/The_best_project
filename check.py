import time
import os
#import RPi.GPIO as GPIO
from os import listdir
from os.path import isfile, join

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(22,12, GPIO.OUT, initial=GPIO.LOW)

def does_file_exist_in_dir(path):
    return any(isfile(join(path, i)) for i in listdir(path))

def list_file(listas):
    for r in os.walk(path):
        print(r[2])
    return

def read_file(nuoroda):
    with open(nuoroda, 'r') as fp:
        line = fp.readline()
    return line

path = '/home/tadela/PycharmProjects/The_best_project/directory'
i =  does_file_exist_in_dir(path)



while i != None:
    if i == True:
        print("Failas rastas")
#        z = list_file(i)
        print(i)
#        print(read_file(path + i))
        i = does_file_exist_in_dir(path)
        time.sleep(5)
    elif i == False:
        print('Failo vis dar nera')
        time.sleep(5)
        i =  does_file_exist_in_dir(path)
