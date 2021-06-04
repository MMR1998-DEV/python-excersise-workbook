with open("countries-raw.txt", "r") as file:
    content = file.readlines()
print(content)


content = [i.strip("\n") for i in content if "\n" in i]
print(content)

content = [i for i in content if i !=""]

content = [i for i in content if i != "top of Page"]
print(content)

content = [i for i in content if len(i) != 1]
print(content)

with open("countries_clean.txt", "w") as file:
    for i in content:
        file.write(i+"\n")