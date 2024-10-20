# BitLocker Encryption Status Checker

This library allows you to get the encryption status of BitLocker-protected drives. It Float value of encryption progress or Bool value of drive encryption.


## Prerequisites

-   Python 3.x
-   Windows 7, 8, 8.1, 10 or 11
-   Administrator access to run the `manage-bde` command


## Python requirements

- This library used pure Python packages and doesn't need to any external libraries - ctypes, subprocess and re


## Usage

- Install package via pip:
   `pip install bitlocker_encryption_status`


## Example

`

from bitlocker_encryption_status.bitlocker_encryption_status import EncStatus

# Create an instance of the EncStatus class
enc_status = EncStatus()

# Disc encryption status
print(enc_status.get_encryption_status(drive= "C:"))

# Disc encryption status in percentage
print(enc_status.get_encryption_status_percentage(drive= "C:"))



`

In the above example, the script displays the encryption status for drive V, which is 97.85% encrypted. However, the encryption status for drive F is not available.

## Notes

-   This script uses the `manage-bde` command, which is a Windows-specific command-line tool for managing BitLocker. It not work on non-Windows systems.
    
-   Ensure that you run the library funcs with administrator privileges to access the `manage-bde` command.
    
    

## License

This script is released under the MIT License.
