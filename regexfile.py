import re

# phoneNumRegex = re.compile(r'^(1\s?)?(\d{3}|\(\d{3}\))[\s\-]?\d{3}[\s\-]?\d{4}$')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

with open("input_file.txt") as reader, open("new_input_file.txt", "w") as writer:
    for line in reader:
        x = line.find("Phone Hseng")
        if x != -1:
            writer.write(line)
        y = line.find("Aunty Chan Chan")
        if y != -1:
            writer.write(line)
        search1 = re.search(phoneNumRegex, line)
        if search1 is not None:
            writer.write(line)

    # for line in f:
    #     x = line.find("Phone Hseng")
    #     search1 = re.search(phoneNumRegex, line)
    #     if search1 is not None:
    #   w     print("im heree")
    #         with open('new_input file.txt', 'a') as g:
    #             g.write(search1.group())
    #             print("im in search1")

