# BitLocker Encryption Status Checker

This script allows you to monitor the encryption status of BitLocker-protected drives in real-time. It displays the percentage of encryption progress for each specified drive and clears the output after two iterations.

## Prerequisites

-   Python 3.x (Tested on Python 3.7 and above)
-   `colorama` library (Install using `pip install colorama`)
-   Administrator access to run the `manage-bde` command

## Use Case

Imagine you have a collection of BitLocker-encrypted hard drives containing important data. You want to transfer the data to a larger storage device, but first, you need to decrypt the drives. Decrypting the drives can be a time-consuming process, and it's important to keep track of the progress to ensure a smooth data transfer. This tool allows you to connect the encrypted drives to your system and monitor the decryption progress in real time. By running the script and specifying the drive letters to monitor, you can easily see the encryption percentage for each drive. This information helps you estimate the time required for decryption and plan the data transfer accordingly.

## Usage

1.  Clone the repository or download the `bitlocker_encryption_status.py` file.
    
2.  Open the `bitlocker_encryption_status.py` file in a text editor.
    
3.  Modify the following variables according to your requirements:
    
    -   `DRIVES_TO_MONITOR`: Specify the drive letters you want to monitor. Add or remove drive letters as needed.
4.  Save the changes in the file.
    
5.  Open a terminal or command prompt.
    
6.  Navigate to the directory where the `bitlocker_encryption_status.py` file is located.
    
7.  Run the script using the following command:
    `python bitlocker_encryption_status.py` 
    
8.  The script will start monitoring the specified drives and display the encryption status every 5 seconds.
    
9.  After two iterations (displaying the status for both drives twice), the output will be cleared, and the process will repeat.
    

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

-   This script uses the `manage-bde` command, which is a Windows-specific command-line tool for managing BitLocker. It may not work on non-Windows systems.
    
-   Ensure that you run the script with administrator privileges to access the `manage-bde` command.
    
-   The output is stylized using ANSI escape sequences, and it works best with terminals that support ANSI colors. If you experience any issues with the output's appearance, make sure your terminal supports ANSI escape sequences.
    
-   The script clears the output after two iterations to keep the display clean and concise. If you want to change the number of iterations before clearing the output, modify the `iteration` variable in the code.

## Acknowledgements
This scrpt was made possible with the assistance of [ChatGPT](https://openai.com/product/chatgpt), a language model developed by [OpenAI](https://openai.com/). ChatGPT provided guidance and assistance in developing the code logic and addressing specific requirements.
    

## License

This script is released under the [MIT License](https://chat.openai.com/c/LICENSE).
