from file_search import search_files
from net_tools import net_menu

tools = {"1": search_files, "2": net_menu}


def main():
    while True:
        choice = input("1 - search, 2 - ip tools, q - quit: ").strip().lower()
        if choice == "q":
            break
        if choice not in tools:
            print("tool not found")
            continue
        tool = tools[choice]

        tool()


if __name__ == "__main__":
    main()
