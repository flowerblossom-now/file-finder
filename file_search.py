import os


def asking(modes):
    while True:
        mode = input("Search all(a) or one(1) file?: ")
        if mode in modes:
            return mode
        print("option no found")


def choose_file(paths, file_name):
    if len(paths) == 0:
        return

    number = int(input("file number: "))
    folder = paths[number - 1]
    full_path = os.path.join(folder, file_name)
    show_file(full_path)


def show_file(path):
    with open(path, "r") as f:
        context = f.read()
        print(context)


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
        for number, path in enumerate(paths, 1):
            print(f"{number}. {path}")
    else:
        print("file not found")


modes = {"a": find_all, "1": find_one}


def search_files():
    while True:
        file_name = input("file : ").strip()
        file_path = input("path : ").strip()
        mode = asking(modes)
        if file_path == "":
            os.chdir("/home/")
        else:
            os.chdir(file_path)

        search = modes[mode]
        result = search(file_name)
        print_res(result)
        choose_file(result, file_name)
        ans = input("live the workplase?(y/n): ").lower().strip()
        if ans == "y":
            break
