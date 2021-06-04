"""
question:  create a Python function that takes a text file as input and returns the number of words contained in the text file.
"""
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print(count_words("word_file1.txt"))