"""
Question: Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

https:/www.google.com
https:/www.yahoo.com
https:/www.stackoverflow.com
https:/www.pythonhow.com
Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

Expected output: 

http://www.google.com
http://www.yahoo.com
http://www.stackoverflow.com
http://www.pythonhow.com
"""

from os import waitpid


with open("urls.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("url_corrected.txt", "w") as file:
    for line in lines:
        line_remove_s = line.replace("s", "", 1)
        print(line_remove_s)
        line_remove_s_add_slash = line_remove_s[:5] + "/" + line_remove_s[5:]
        print(line_remove_s_add_slash)
        add_slash_at_end = line_remove_s_add_slash[:-1] + "/" + "\n"
        print(add_slash_at_end)
        file.write(add_slash_at_end)