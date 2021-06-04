"""
Question: Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.
"""
import time
i = 0
while 1<2:
    i = i+1
    print(i)
    print("hello")
    time.sleep(i)
    if(i >= 3):
        print("end of the loop!")
        break