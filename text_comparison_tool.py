
# TODO: Add line numbers to original files
# TODO: Output differences in a new file 
# TODO: Indicate line number of each difference 


import difflib


def compare_text_files(file1_path, file2_path):
    with open(file=file1_path, mode='r', encoding="utf8") as file1, open(file=file2_path, mode='r', encoding="utf8") as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    differ = difflib.Differ()
    diff = differ.compare(file1_lines, file2_lines)
    print(diff)

    # Print difference(s) in file2 compared to file1   
    for line in diff:
        if line.startswith('- '):
            print(f'Line removed: {line[2:]}')
        elif line.startswith('+ '):
            print(f'Line added: {line[2:]}')


if __name__ == "__main__":
    # Input absolute/relative file paths  
    file1_path = r'file1_path'
    file2_path = r'file2_path'

    compare_text_files(file1_path, file2_path)

