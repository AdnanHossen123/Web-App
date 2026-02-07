import os, sys, time, random, threading

os.system("clear")

GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"

logo = [
    "                ██▒   █▓ ██▓ ██▀███   █    ██   ██████",
    "               ▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒",
    "                ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄",
    "                 ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒",
    "                  ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒",
    "                  ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░",
    "                  ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░",
    "                    ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░",
    "                     ░   ░     ░        ░           ░",
]

for line in logo:
    print(GREEN + line + RESET)

print("\n")

def glitch():
    while True:
        line_index = random.randint(0, len(logo)-1)
        color = random.choice([GREEN, RED])
        # move cursor up to line_index from bottom
        sys.stdout.write(f"\033[{len(logo)+2-line_index}A\r")
        sys.stdout.write(color + logo[line_index] + RESET)
        # move cursor back down to input line
        sys.stdout.write(f"\033[{len(logo)+1-line_index}B\r")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05,0.15))

threading.Thread(target=glitch, daemon=True).start()

user = input(f"{RED}[?] Enter your codename: {RESET}")
print(f"{GREEN}[✓] Welcome, {RED}{user}{RESET}")