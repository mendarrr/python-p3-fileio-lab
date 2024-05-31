# write mode
def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode ='w') as write_file:
        write_file.write(file_content)
    pass

# append mode
def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode = 'a') as append_file:
        append_file.write(append_content)
    pass

# read mode
def read_file(file_name):
    with open(f"{file_name}.txt", mode = 'r') as read_file:
        return read_file.read()
    pass
