


import os
import time
import random
import threading
import sys

# Clear screen
def clear_screen():
    os.system("clear || cls")

# Colors
GREEN = "\033[1;32m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
DIM = "\033[2m"
BLINK = "\033[5m"
RESET = "\033[0m"

# Logo lines
logo_lines = [
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

def glitch_line(line, intensity=0.7):
    """Print glitchy line"""
    chars = list(line)
    glitch_chars = ['█','▓','▒','░','▐','▀','▄','▌','▐','▔','▁','▂','▃','▅']
    
    for i, char in enumerate(chars):
        if random.random() < intensity and char.isspace() == False:
            chars[i] = random.choice(glitch_chars)
        
        color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, CYAN])
        sys.stdout.write(color + chars[i] + RESET)
        sys.stdout.flush()
        time.sleep(0.002)
    print()

def continuous_glitch_background():
    """Background glitch effect"""
    while glitch_running:
        clear_screen()
        for line in logo_lines:
            glitch_line(line, random.uniform(0.5, 0.8))
        print(f"\n{RED}GLITCH INIT... {random.randint(404, 1337)} ERRORS DETECTED")
        time.sleep(0.12)

# Global glitch control
glitch_running = True

# Initial heavy glitch show
clear_screen()
print(f"\n{BLINK}{RED}⚡  GLITCH MODE: PERMANENT ⚡{RESET}\n")
time.sleep(0.5)

# Start background glitch
glitch_thread = threading.Thread(target=continuous_glitch_background, daemon=True)
glitch_thread.start()

# Wait then overlay clean elements
time.sleep(2)

# Stop glitch for main input phase
glitch_running = False
clear_screen()

# Perfect logo reveal
for line in logo_lines:
    print(f"{GREEN}{line}{RESET}")
print(f"\n{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")

# Glitch typing function
def glitch_print(text, glitch_chance=0.12, speed=0.035):
    for char in text:
        if random.random() < glitch_chance and char.isalnum():
            glitch_char = random.choice('█▓▒░▐▀▄█▓▒░')
            print(glitch_char, end='', flush=True)
            sys.stdout.flush()
            time.sleep(speed * 1.5)
            print('\b' + char, end='', flush=True)
        print(char, end='', flush=True)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Startup sequence
print()
glitch_print(f"{PURPLE}[+] Initializing Secure Terminal...", 0.15)
time.sleep(0.7)
glitch_print(f"{GREEN}[+] Quantum Link Established...", 0.12)
time.sleep(0.7)
glitch_print(f"{RED}[!] GLITCH PROTOCOL: ACTIVE FOREVER", 0.18)

print(f"\n{RED}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{RESET}")
print(f"{CYAN}    [SECURE INPUT TERMINAL ACTIVE]{RESET}")
print(f"{RED}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▬▬▬▬▬▬▬▬▬▬{RESET}")

# **CLEAN USER INPUT - Kono restriction nai**
print()
user_codename = input(f"{WHITE}{CYAN}[{GREEN}GLITCH-SEC{RESET}]{WHITE} Enter your codename: {RESET}").strip()

# Perfect validation and display (kono restriction nai)
if user_codename:
    clear_screen()
    
    # Final perfect logo
    for line in logo_lines:
        print(f"{GREEN}{line}{RESET}")
    
    print(f"\n{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
    
    glitch_print(f"{GREEN}[✓] ACCESS GRANTED: {RED}{user_codename.upper()}{GREEN}", 0.08)
    time.sleep(0.4)
    glitch_print(f"{GREEN}[✓] BIOMETRIC VERIFICATION: PASSED", 0.06)
    time.sleep(0.3)
    glitch_print(f"{RED}[⚡] PERMANENT GLITCH MODE: ENGAGED", 0.1)
    
    print(f"\n{GREEN}Welcome, {RED}{user_codename}{GREEN}. System ready.\n{RESET}")
    print(f"{DIM}{RED}█ ▓ ▒ GLITCH TERMINAL v∞.0 ░ ▒ ▓ █{RESET}")
    
else:
    print(f"\n{RED}[ERROR] Codename required!")
    time.sleep(2)

print(f"\n{RED}Press Enter to continue...")
input()