"""
Please download the json file in the attachment and use Python to add a new employee to the file's content
"""
import json

with open("56.json", "+r") as file:
    d = json.loads(file.read())
    d['owners'].append(dict(firstName = 'Albert', lastName = 'Bert'))
    file.seek(0)
    json.dump(d, file, indent=7, sort_keys=True)
    file.truncate()