def count_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines=file.readline()
        line_count=len(lines)
        word=sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        print(char_count)
        






file_path ='example.txt'
lines = count_txt_file(file_path)