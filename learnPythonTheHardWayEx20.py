file_name_input = raw_input("Please enter file path: ")

file_name = open(file_name_input)

def print_all(file_name_in):
    print file_name_in.read()

def revind(file_name_in):
    file_name_in.seek(0)

def print_a_line(line_number,file_name_in):
    print line_number,file_name_in.readline()

print_all(file_name)

revind(file_name)

current_line = 1
print_a_line(current_line,file_name)

current_line += 1
print_a_line(current_line,file_name)

current_line += 1
print_a_line(current_line,file_name)

file_name.close()
