# create a program tthat ask the users to submit text repeatly

file = open("user_data_save_close.txt", "a+")

while True:
    line = input("Write a  value: ")
    if line == "SAVE":
        file.close()
        file.open("user_data_save_close.txt", "a+")
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")