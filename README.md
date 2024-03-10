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

Here's an example to help you understand the script's output:

    ==================================================
    Drive V:
    Percentage Encrypted: 97.85%
    ================================================== 
    
    ================================================== 
    Drive F: 
    Encryption status for F: not available 
    ==================================================

In the above example, the script displays the encryption status for drive V, which is 97.85% encrypted. However, the encryption status for drive F is not available.

## Notes

-   This script uses the `manage-bde` command, which is a Windows-specific command-line tool for managing BitLocker. It not work on non-Windows systems.
    
-   Ensure that you run the script with administrator privileges to access the `manage-bde` command.
    
    

## License

This script is released under the MIT License.
