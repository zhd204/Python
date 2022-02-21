def only_files(file_path):
    from os import listdir
    from os.path import isfile, join

    onlyFiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    return onlyFiles

import re

l = "$2,999+/mo"
s = l.split(" ")
print(s)
s[0].replace("-", "")
print(s[0])

special_characters = ["$", ",", "+", "/", "mo"]
for cha in special_characters:
    s[0] = s[0].replace(cha, "")
print(s[0])

from datetime import datetime
print(datetime.now().year)
