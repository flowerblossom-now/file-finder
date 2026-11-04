import platform
import subprocess


def ask_addr():
    while True:
        address = input("write down your ip or adress: ").strip()
        if address != "":
            return address
        print("address is invalid")


linux_opt = {
    "i": ("show_ip", ["ip", "-4", "-br", "a"], False),
    "d": ("dns", ["nslookup"], True),
    "t": ("trace_ip", ["tracepath", "-m", "12"], True),
    "p": ("ping_ip", ["ping", "-c", "10"], True),
    "r": ("route", ["ip", "route"], False),
    "m": ("mac_addr", ["ip", "-br", "link"], False),
    "n": ("net_neighbor", ["ip", "neigh"], False),
    "s": ("show_ports", ["ss", "-tuln"], False),
    "g": ("global_ip", ["curl", "ipinfo.io"], False),
}

windows_opt = {
    "i": ("show_ip", ["ipconfig"], False),
    "d": ("dns", ["nslookup"], True),
    "t": ("trace_ip", ["tracert", "-h", "12"], True),
    "p": ("ping_ip", ["ping", "-n", "10"], True),
    "r": ("route", ["route", "print"], False),
    "m": ("mac_addr", ["getmac"], False),
    "n": ("net_neighbor", ["arp", "-a"], False),
    "s": ("show_ports", ["netstat", "-an"], False),
    "g": ("global_ip", ["curl", "ipinfo.io"], False),
}

macos_opt = {
    "i": ("show_ip", ["ifconfig"], False),
    "d": ("dns", ["nslookup"], True),
    "t": ("trace_ip", ["traceroute", "-m", "12"], True),
    "p": ("ping_ip", ["ping", "-c", "10"], True),
    "r": ("route", ["netstat", "-rn"], False),
    "n": ("net_neighbor", ["arp", "-a"], False),
    "s": ("show_ports", ["netstat", "-an"], False),
    "g": ("global_ip", ["curl", "ipinfo.io"], False),
}

all_opts = {
    "Linux": linux_opt,
    "Windows": windows_opt,
    "Darwin": macos_opt,
}

net_opt = all_opts.get(platform.system(), linux_opt)


def run_command(command, needs_addr):
    if needs_addr:
        command = command + [ask_addr()]
    subprocess.run(command, check=False)
    input("\n\nenter to menu")


def net_menu():
    while True:
        for key, (name, _, _) in net_opt.items():
            print(key + " - " + name)
        print("q - quit")
        choice = input("choose an option: ").strip().lower()
        if choice == "q":
            break
        if choice not in net_opt:
            print("undentified")
            continue

        name, command, needs_addr = net_opt[choice]
        run_command(command, needs_addr)
