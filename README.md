# Whatsapp-Web-UI-Automation

# Introduction

This is a selenium based framework that interacts with Whatsapp Web interface and can be used to automate given below
1. Search number in search-box, number picked from Excel file.
2. Pick searched number and send text message.
3. Check sent successful status and send this data into Excel.
4. Check seen/non seen status and send this data into Excel.
5. Automatic logout and return to log in screen.

# Setup

1. Clone this repository
    ```
    git clone https://github.com/RFNshare/Whatsapp-Web-UI-Automation.git
    ```

2. Go to the project's root directory and install requirements.
    ```
    pip3 freeze > requirements.txt
    ```

3. Run this script for Chrome.
    ```
    py.test --browser_name chrome -v -s

    ```
   This will open a browser in the current window.
4. 
5. . Run this script for Firefox.
    ```
    py.test --browser_name firefox -v -s

    ```
   This will open a browser in the current window.

6. Now you can scan your whatsapp QR code in from phone.
    ```
    py.test 

    ```
   This will default cmd. Open with Chrome.

### Usage

You can use the whatsapp instance to perform any simple action.

```
// Open WhatsApp, go to three dot option, click linked devices. 
   Then click Link a device

```

While the above code is very script, it provides 2 min to scan QR code.