"""
Question: Create an English to bangla translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary.

d = dict(weather = "আবহাওয়া", earth = "দুনিয়া", rain = "ব্রিষ্টি") 

Expected output: 

Enter word: earfdgth
nothing found!
"""

d = dict(weather = "আবহাওয়া", earth = "দুনিয়া", rain = "ব্রিষ্টি")  

def vocabulary(word):
    try:
        return d[word]
    except:
        print("nothing found!")


word = input("Enter word: ")
print(vocabulary(word))