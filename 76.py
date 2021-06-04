#print today's date

from datetime import datetime 
today = datetime.now()
print(today.strftime("Today is %A, %B %d, %Y"))