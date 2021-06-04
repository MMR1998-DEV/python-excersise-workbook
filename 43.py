"""
Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.
"""
import string

with open("latters2.txt", "w") as file:
    for latter1, latter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(latter1 + latter2 + "\n")