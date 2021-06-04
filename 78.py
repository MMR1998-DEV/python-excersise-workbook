# Create a program that generates a password of 6 random alphanumeric characters.

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 8)
password = "".join(chosen)
print(password)