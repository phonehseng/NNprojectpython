# with open('data_file.txt', 'w') as file:
#     for x in range(10):
#         file.write(f'{x+1}. Some text to write to text file\n')


with open('data_file.txt') as file:
    x = 0
    for line in file:
        position = line.find("1")
        print(position)



        # x += 1
        # print(f"line {x} is {line} ")

    # content = file.read()
    # print(content)

