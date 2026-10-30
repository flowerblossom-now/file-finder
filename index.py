import os

file_name = input("file : ").strip()
file_path = input("path : ").strip()
os.chdir(file_path)

found_path = []

while True:
    for path, subfolders, files in os.walk(os.getcwd()):
        if file_name in files:
            found_path.append(path)

    if len(found_path) > 0:
        break

    prev = os.getcwd()
    os.chdir("..")
    if os.getcwd() == prev:
        break

if len(found_path) != 0:
    for path in found_path:
        print(path)
else:
    print("path was not found")


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
