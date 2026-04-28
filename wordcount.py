import sys
from basics import read_file

filename = sys.argv[1]
text_list = read_file(filename).split()
count = len(text_list)
print(f"File: {filename}\nWord count: {count}")