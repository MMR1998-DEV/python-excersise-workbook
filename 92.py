"""
Question: write a script that counts and prints out the number of .py files in files folder.

Expected output: 2
"""

import glob

file_list=glob.glob1("files","*.py")
print(len(file_list))
