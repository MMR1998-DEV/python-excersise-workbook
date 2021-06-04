# Please write a script that counts the number of .py files contained inside subdirs and all its sub-directories.

import glob

file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))