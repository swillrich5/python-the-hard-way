from sys import argv

script, input_file = argv

current_file = open(input_file)

current_line = 1
for line in current_file:
    stripped_line = line.strip()
    print(str(current_line) + ":", stripped_line)
    current_line += 1