import os
import time
import random
import threading
import sys

# Clear screen
os.system("clear || cls")

# Colors
GREEN = "\033[1;32m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
DIM = "\033[2m"
BLINK = "\033[5m"
RESET = "\033[0m"

# Enhanced glitchy logo with multiple layers
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

def glitch_line(line, glitch_intensity=0.8):
    """Print a single line with heavy glitch effect"""
    chars = list(line)
    glitch_chars = ['█','▓','▒','░','▐','▀','▄','▌','▐','▔','▁']
    
    for i, char in enumerate(chars):
        if random.random() < glitch_intensity:
            # Heavy glitch - replace with random block chars
            chars[i] = random.choice(glitch_chars)
        
        # Random color shifts
        color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, BLINK+RED])
        sys.stdout.write(color + chars[i] + RESET)
        sys.stdout.flush()
        time.sleep(random.uniform(0.001, 0.01))
    
    print()
    return ''.join(chars)

def heavy_glitch_effect():
    """Continuous background glitch effect"""
    while glitch_active:
        os.system("clear || cls")
        for line in logo_lines:
            glitch_line(line, random.uniform(0.6, 0.9))
        time.sleep(0.1)

# Start continuous glitch background
glitch_active = True
glitch_thread = threading.Thread(target=heavy_glitch_effect, daemon=True)
glitch_thread.start()

# Wait for dramatic effect
time.sleep(1.5)

# Main logo display with insane glitch
print(f"\n{BLINK}{RED}⚡ GLITCH MODE ENGAGED ⚡{RESET}\n")
time.sleep(0.3)

for _ in range(15):  # Heavy glitch loop
    os.system("clear || cls")
    for line in logo_lines:
        glitch_line(line, 0.85)
    print(f"\n{RED}█▓▒░ GLITCHING... {random.randint(1000,9999)} ERRORS ░▒▓█{RESET}")
    time.sleep(0.08)

# Stop glitch for clean reveal
glitch_active = False
time.sleep(0.3)
os.system("clear || cls")

# Clean animated logo reveal
colors = [GREEN, CYAN, BLUE, YELLOW]
for frame in range(3):
    os.system("clear || cls")
    color = colors[frame % len(colors)]
    for i, line in enumerate(logo_lines):
        glitch_factor = 0.3 - (frame * 0.1)
        glitch_line(line, max(0, glitch_factor))
    print(f"\n{GREEN}SYSTEM BOOT {frame+1}/3...{RESET}")
    time.sleep(0.4)

os.system("clear || cls")

# Final perfect logo
for line in logo_lines:
    print(f"{GREEN}{line}{RESET}")
print(f"\n{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")

# Enhanced typing effect with glitch
def glitch_type(text, glitch_chance=0.15, delay=0.04):
    for i, char in enumerate(text):
        if random.random() < glitch_chance and char not in ' \n':
            glitch_char = random.choice('█▓▒░▐▀▄▌▐▔▁▓▒░')
            print(glitch_char, end='', flush=True)
            time.sleep(delay * 2)
            print('\b' + char, end='', flush=True)
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Startup sequence with glitch
print()
glitch_type(f"{PURPLE}⚡{RESET} {GREEN}[+] Neural Interface Booting...{RESET}", 0.2)
time.sleep(0.8)
glitch_type(f"{PURPLE}⚡{RESET} {GREEN}[+] Quantum Encryption Active...{RESET}", 0.18)
time.sleep(0.8)
glitch_type(f"{PURPLE}⚡{RESET} {RED}[!] GLITCH PROTOCOL: PERMANENT{RESET}", 0.15)
time.sleep(1.0)

# Fancy input with glitch border
print(f"\n{RED}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{RESET}")
user_input = input(f"{CYAN}[{RED}GLITCH-SEC{RESET}]{CYAN} Enter Secure Codename: {RESET}").strip()

# Glitch the input display
print()
glitch_type(f"{GREEN}[✓] BIOMETRIC SCAN: {RED}{user_input.upper()}{GREEN} - VERIFIED{RESET}", 0.1)
time.sleep(0.5)

glitch_type(f"{GREEN}[✓] QUANTUM LINK: {RED}SECURED{RESET}", 0.08)
time.sleep(0.4)

glitch_type(f"{GREEN}[!] PERMANENT GLITCH MODE: {RED}ACTIVE{RESET}", 0.12)
print(f"\n{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
glitch_type(f"{GREEN}Welcome back, {RED}{user_input}{GREEN}. Interface ready.{RESET}\n", 0.06)

# Final glitch signature
print(f"{DIM}{RED}█ ▓ ▒ ░ GLITCH PROTOCOL v∞.0 ░ ▒ ▓ █{RESET}")