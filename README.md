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
   
2. If you clone this repository before then run this on the project's root directory
    ```
    git pull
    ```
3. Copy/Cut files folder from project's root directory & paste it in C drive root directory.
    ```
    C:\files
    ```
   Make sure you have driver & Excel file in that path.
4. Go to the project's root directory and install requirements(Recommended create virtual env first).
    ```
    pip install -r requirements.txt
    ```

5. Run this script for Chrome.
    ```
    py.test --browser_name chrome -v -s

    ```
   This will open a browser in the current window.
6. . Run this script for Firefox.
    ```
    py.test --browser_name firefox -v -s

    ```
   This will open a browser in the current window.

7. This will default cmd. Open with Chrome.
    ```
    py.test 

    ```
   
8. Generate HTML reports with run script include log.
    ```
    pytest --html=report.html --capture=tee-sys 

    ```
   This will create an HTML report. You can find report in project's root directory

### Usage

You can use the whatsapp instance to perform any simple action.

```
// Open WhatsApp, go to three dot option, click linked devices. 
   Then click Link a device

```

While the above code is a script, it provides 2 min to scan QR code for login into Whatsapp WEB.