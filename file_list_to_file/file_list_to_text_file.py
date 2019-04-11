#Script to get file list with extention and contains string to text file.

import os

root = 'C:\Windows\Fonts'
file_output = open("file_list.txt", "w+")
extension = '.TTF'
contains_string = 'A' #string contains in file name

file_list = list()

for path, subdirs, files in os.walk(root):
    for name in files:
        if os.path.join(path, name).endswith(extension) == True:
            if contains_string in os.path.join(path, name):
				#file name with directory
                #file_list.append(os.path.join(path, name))
                #print(os.path.join(path, name))
				#file name with directory
                #only file name
                file_list.append(os.path.join(name[:-len(extension)])) 
                print(os.path.join(name[:-len(extension)]))
				#only file name
i=0
while i < len(file_list):
    file_output.write(file_list[i] + '\n')
    i+=1
file_output.close()
