"""
Question: Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:

abc
def
ghi

and so on.
"""
import string

with open("latters3.txt", "w") as file:
    for latter1, latter2, latter3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
        file.write(latter1 + latter2 +latter3 + "\n")