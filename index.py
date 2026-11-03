import os


def up():
    prev = os.getcwd()
    os.chdir("..")
    if os.getcwd() == prev:
        return False
    else:
        return True


def find_all(file_name):
    found_path = []

    for path, subfolders, files in os.walk(os.getcwd()):
        if file_name in files:
            found_path.append(path)

    return found_path


def find_one(file_name):
    while True:
        for path, subfolders, files in os.walk(os.getcwd()):
            if file_name in files:
                return [path]

        if up() == False:
            return []


def print_res(paths: list):
    if len(paths) != 0:
        for path in paths:
            print(path)
    else:
        print("path was not found")


modes = {"a": find_all, "1": find_one}


file_name = input("file : ").strip()
file_path = input("path : ").strip()
while True:
    mode = input("Search all(a) or one(1) file?: ")
    if mode not in modes:
        print("unidentified mode")
    else:
        break


if file_path == "":
    os.chdir("/home/")
else:
    os.chdir(file_path)

search = modes[mode]
result = search(file_name)
print_res(result)


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
