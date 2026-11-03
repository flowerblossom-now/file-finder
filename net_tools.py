import subprocess


def show_ip():
    ip_run = subprocess.run(["ip", "-4", "-br", "a"])
    return ip_run


def ns_look_up():
    adr = input("Paste the site: ")
    look_dns = subprocess.run(["nslookup", adr])
    return look_dns


def net_menu():
    while True:
        res = input("choose an option: ip(i),dns(d),quit(q): ")
        if res == "i":
            show_ip()
        elif res == "d":
            ns_look_up()
        elif res == "q":
            break
        else:
            print("undientified")
