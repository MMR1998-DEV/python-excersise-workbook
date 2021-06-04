# program for taking data from user and store it in txt file

file =  open("user_data.txt", "a+")

while True:
    line = input("Write a Value: ")
    if (line == "CLOSE") or (line == "Close") or (line == "close"):
        file.close()
        break
    else:
        file.write(line + "\n")