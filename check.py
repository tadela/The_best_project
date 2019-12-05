from os import listdir
from os.path import isfile, join

def does_file_exist_in_dir(path):
    return any(isfile(join(path, i)) for i in listdir(path))

def list_files(listas):
    return listdir(listas)

def open_files(filas):
    return

print(list_files("C:/Users/tadrmk/PycharmProjects/The_best_project/directory/"))
#
#
# def read_file(file):


#print(does_file_exist_in_dir("C:/Users/tadrmk/PycharmProjects/The_best_project/directory/"))