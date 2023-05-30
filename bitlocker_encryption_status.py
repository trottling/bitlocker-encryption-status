import subprocess
import time

from colorama import init, Fore, Style
import re
import os

# Enable ANSI support in Cmder
os.environ['ANSICON'] = '1'

# Initialize colorama
init(convert=True)

# Interval between each status check (in seconds)
CHECK_INTERVAL = 5

# Drives to monitor
DRIVES_TO_MONITOR = ['V:', 'F:']

def get_encryption_status(drive):
    try:
        # Execute the manage-bde command to get the encryption status for the specified drive
        output = subprocess.check_output(['manage-bde', '-status', drive]).decode('utf-8')

        # Find the line containing the Percentage Encrypted status
        for line in output.splitlines():
            if 'Percentage Encrypted' in line:
                return line.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return f'Encryption status for {drive} not available'

def format_percentage(percentage):
    match = re.search(r'\d+\.?\d*', percentage)
    if match:
        value = float(match.group())
        if value == 0:
            return f'\033[38;2;164;90;162m{percentage}\033[0m'  # #A45A2 (purple color)
        else:
            return f'\033[38;2;164;90;162m{percentage}\033[0m'  # #A45A2 (purple color)

    return percentage

def main():
    iteration = 0
    while True:
        for drive in DRIVES_TO_MONITOR:
            # Get the encryption status for each drive
            status = get_encryption_status(drive)

            # Display the status in large text
            print('\n' + '=' * 50)
            print(f'Drive {drive}:')
            print(format_percentage(status))
            print('=' * 50)

        iteration += 1

        # Clear the output after two iterations
        if iteration >= 1:
            time.sleep(CHECK_INTERVAL)  # Wait for a short duration to allow user to read the output
            subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
            iteration = 0
        else:
            # Wait for the next check interval
            time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
