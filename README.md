![Screenshot (396)](https://github.com/user-attachments/assets/c5da3434-b021-4767-b470-6f3bf48fbb8a)
# Lostxlso: Multi-Vulnerability Scanner

**Lostxlso** is a powerful and versatile multi-vulnerability scanner designed to detect various web application vulnerabilities, including Local File Inclusion (LFI), Open Redirects (OR), SQL Injection (SQLi), and Cross-Site Scripting (XSS). This tool was created by **AnonKryptiQuz**, **Coffinxp**, **Hexsh1dow**, and **Naho**.

## Features

- **LFI Scanner**: Detect Local File Inclusion vulnerabilities.
- **OR Scanner**: Identify Open Redirect vulnerabilities.
- **SQL Scanner**: Detect SQL Injection vulnerabilities.
- **XSS Scanner**: Identify Cross-Site Scripting vulnerabilities.
- **Multi-threaded scanning**: Improved performance through multi-threading.
- **Customizable payloads**: Adjust payloads to suit specific targets.
- **Success criteria**: Modify success detection criteria for specific use cases.
- **User-friendly command-line interface**: Simple and intuitive.
- **Save vulnerable URLs**: Option to save the results of vulnerable URLs to a file.

## Requirements

- **Python 3.x**
- `webdriver_manager`
- `selenium`
- `aiohttp`
- `beautifulsoup4`
- `colorama`
- `rich`
- `requests`
- `gitpython`
- `prompt_toolkit`

## Installation

### Clone the repository

```bash
git clone https://github.com/coffinsp/lostools
cd lostools
```
## Running the Script

To run the script, use the following command:

```bash
python lostsec.py
```
to update the tool to the latest version
```bash
just edit the config.yml file with your tool directory
after pressing 5 and exiting from the tool run the tool again it will run with an updated version
```
## Input Information:

- **Input URL/File**: You can provide a single URL or an input file containing a list of URLs to scan.
- **Payload File**: Select or provide a custom payload file for the type of vulnerability you want to scan for.
- **Success Criteria:**:  Define the patterns or strings that indicate a successful exploitation attempt.
- **Concurrent Threads:**: Set the number of threads for multi-threaded scanning.
- **View and Save Results:**: Results will be displayed in real-time as the scan progresses.
After the scan completes, you will have the option to save the URLs found to be vulnerable to a file for future reference.

## Customization

Lostxlso allows for various levels of customization to fit your specific testing needs:
- **Custom Payloads:**: Create or modify payload files to suit specific vulnerability types or applications. Payloads should be tailored to the vulnerability being tested.
- **Success Criteria:**: Adjust the success criteria patterns in the tool to identify successful exploitation attempts more accurately. For example, you can modify the tool to check for specific error messages or unique responses.
- **Concurrent Threads:**:  Control the number of concurrent threads used during the scan to optimize performance based on system resources.

## Chrome Installation Instructions

1. Launch Terminal.

2. Download the Google Chrome .deb file:

   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

3. Install the downloaded Google Chrome .deb file:

sudo dpkg -i google-chrome-stable_current_amd64.deb

4. Enter your Ubuntu/kali user password.

5.If you come across some errors during the install, use the following command and flag:

sudo apt -f install

after this again enter this sudo dpkg -i google-chrome-stable_current_amd64.de

Done

## Disclaimer

Lostxlso is intended for educational and ethical hacking purposes only. It should only be used to test systems you own or have explicit permission to test. Unauthorized use of third-party websites or systems without consent is illegal and unethical.
