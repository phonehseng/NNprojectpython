with open("input_file.txt") as f:
    inputtext = f.read()
    print(inputtext)
    print(inputtext.upper())
    print(inputtext.lower())
    print(len(inputtext))
    for x in range(len(inputtext)):
        print(inputtext[x])