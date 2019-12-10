import os

path = '/home/tadela/PycharmProjects/The_best_project/directory/testas.txt'

def read_file(nuoroda):
    with open(nuoroda, 'r') as fp:
        line = fp.readline()
    return line

print(read_file(path))
