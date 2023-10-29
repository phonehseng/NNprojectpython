import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')


with open("input_file.txt") as f:
    for line in f:
        x = line.find("Phone")
        search1 = re.search(phoneNumRegex, line)
        if search1 is not None:
            print(search1.group())
        if x != -1:
            word = line[x : (x+5)]
            print(word)