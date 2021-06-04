"""
Question: Create an English to bangla translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. Also, return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary. Also, make the program non-case-sensitive, meaning that, for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "আবহাওয়া", earth = "দুনিয়া", rain = "ব্রিষ্টি") 

Expected output: 

Enter word: earfdgth
nothing found!
"""
d = dict(weather = "আবহাওয়া", earth = "দুনিয়া", rain = "ব্রিষ্টি") 
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't find that word!"

word = input("Enter word: ").lower()
print(vocabulary(word))