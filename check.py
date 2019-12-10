import time
from os import listdir
from os.path import isfile, join

def does_file_exist_in_dir(path):
    return any(isfile(join(path, i)) for i in listdir(path))

def list_files(listas):
    return listdir(listas)

def open_files(filas):
    with open_files('filas') as fp:
        line = fp.readline()
    return

#print(does_file_exist_in_dir("/home/tadela/PycharmProjects/The_best_project/directory"))


i =  does_file_exist_in_dir("/home/tadela/PycharmProjects/The_best_project/directory")

while i != None:
    if i == True:
        print("Failas rastas")
        #print(open_files(i))
        i = does_file_exist_in_dir("/home/tadela/PycharmProjects/The_best_project/directory")
        time.sleep(5)
    elif i == False:
        print('Failo vis dar nera')
        time.sleep(5)
        i =  does_file_exist_in_dir("/home/tadela/PycharmProjects/The_best_project/directory")
#time.sleep(5)



#print(list_files("/home/tadela/PycharmProjects/The_best_project/directory"))
#
#
# def read_file(file):


#print(does_file_exist_in_dir("C:/Users/tadrmk/PycharmProjects/The_best_project/directory/"))