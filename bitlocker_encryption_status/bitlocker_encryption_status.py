import ctypes
import subprocess

import re


class EncStatus:
    """
    This library allows you to get the encryption status of BitLocker-protected drives. It Float value of encryption progress or Bool value of drive encryption.
    WARNING: Admin privileges required
    """

    def __init__(self):
        pass

    def check_admin(self):
        # Check for admin privileges
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

    def get_encryption_status(self, drive: str) -> bool:
        """
        :keyword drive - Disk name, like "C:"

        :return Bool value of disk encryption, return False if disk doesn't have encryption or can't check drive or func run without admin privileges
        """

        if not self.check_admin():
            return False

        try:
            # Execute the manage-bde command to get the encryption status for the specified drive
            output = subprocess.check_output(['manage-bde', '-status', drive]).decode('utf-8')

            # Check the line containing the AES or XEX encryption type
            # https://learn.microsoft.com/en-us/mem/configmgr/protect/tech-ref/bitlocker/settings
            # https://en.wikipedia.org/wiki/BitLocker
            for line in output.splitlines():
                if 'AES' or 'XEX' in line:
                    return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

        return False

    def get_encryption_status_percentage(self, drive: str) -> float:
        """
        :keyword drive - Disk name, like "C:"
        recommended run get_encryption_status_percentage() first
        :return Float value of disk encryption, return 0.0 if can't check drive or func run without admin privileges
        """

        if not self.check_admin():
            return 0.0

        try:
            # Execute the manage-bde command to get the encryption status for the specified drive
            output = subprocess.check_output(['manage-bde', '-status', drive]).decode('utf-8')

            perc_pattern = re.compile(r"(\d+,\d)%")

            # Match the line percentage pattern
            for line in output.splitlines():
                if perc_pattern.match(line):
                    return float(perc_pattern.findall(line)[1])
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

            return 0.0
