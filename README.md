[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- PROJECT LOGO -->

<br />
<p align="center">
  <a href="https://github.com/rfnshare/StraightIntLtd">
    <img src="logo.png" alt="Logo">
  </a>

  <h3 align="center">Whatsapp Web UI Automation</h3>

  <p align="center">
    ...
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/RFNshare/Whatsapp-Web-UI-Automation/issues">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
Introduction

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
For more examples,  please refer to the [Documentation](https://example.com)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/rfnshare/StraightIntLtd/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Your Name - [@rfnshare](https://twitter.com/rfnshare) - aalfaroque@gmail.com

Project Link: [WhatsApp WebUI Automation](https://github.com/RFNshare/Whatsapp-Web-UI-Automation.git)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-0-yellow?style=for-the-badge
[contributors-url]: https://github.com/rfnshare/Whatsapp-Web-UI-Automation/graphs/contributors
[forks-shield]: https://img.shields.io/badge/froks-0-blue?style=for-the-badge
[forks-url]: https://github.com/rfnshare/StraightIntLtd/network/members
[stars-shield]: https://img.shields.io/badge/stars-0-red?style=for-the-badge
[stars-url]: https://github.com/rfnshare/Whatsapp-Web-UI-Automation/stargazers
[issues-shield]: https://img.shields.io/badge/issues-0-success?style=for-the-badge
[issues-url]: https://github.com/rfnshare/Whatsapp-Web-UI-Automation/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rfnshare