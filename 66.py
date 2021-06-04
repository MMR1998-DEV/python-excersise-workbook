"""
Question: Create an English to bangla translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "আবহাওয়া", earth = "দুনিয়া", rain = "ব্রিষ্টি") 

Expected output: 

Enter word: earth
terra
"""

d = dict(weather = "আবহাওয়া", earth = "দুনিয়া", rain = "ব্রিষ্টি")  

def vocabulary(word):
    return d[word]

word = input("Enter word: ")
print(vocabulary(word))