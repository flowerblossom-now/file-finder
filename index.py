import os
from pathlib import Path

file_name = input("file : ").strip()
file_path = input("path : ").strip()
os.chdir(file_path)

found = False

while True:
    for path, subfolders, files in os.walk(os.getcwd()):
        if file_name in files:
            print(f"file {file_name} was found in {path}")
            found = True
            break

    if found == True:
        break

    prev = os.getcwd()
    os.chdir("..")
    if os.getcwd() == prev:
        print("file was not found")
        break


# while os.path.isfile(file_name) == False:
#    prev = os.getcwd()
#    os.chdir("..")
#    if os.getcwd() == prev:
#        print("file not found")
#        break

# if os.path.isfile(file_name) == True:
#    print(f"File {file_name} is in {os.getcwd()}")
# else:
#    print("file not found")
