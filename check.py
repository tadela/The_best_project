import os
from pathlib import Path

my_file = Path("C:/Users/tadrmk/PycharmProjects/The_best_project/directory/")
if my_file.is_file():
    print('failas yra')
else:
    print('failo nera')
    # file exists

# def read_file():
#     with open('directory\*, 'r') as R:
#         R.read()


