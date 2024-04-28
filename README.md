# Micropython Web Server

---

### Description: 
  This project is a simple web login system developed using HTML and Python. It allows users to log in through a web interface, sets the datetime with local time, and creates a configuration file (`config.txt`) to save strings.

### File structure:
  - html:
      - login.html: HTML file for the login page.
      - web.html: HTML file for the main web page.
  - python:
      - boot.py: Python script for bootstrapping the system.
      - main.py: Main Python script containing the backend logic.

### Features:
  - Login System:
      description: Users can log in through the provided web interface (`login.html`).
  - Local Datetime:
      description: The system sets the datetime with local time, enhancing user experience.
  - Configuration File:
      description: A configuration file named `config.txt` is created to save important strings.

### Setup:
  1. Clone the Repository:
     command: git clone https://github.com/strcxs/micropython-web.git
  2. Navigate to Project Directory:
     command: cd web-login-system
  3. Run the System:
     description: 
       - Open `login.html` in a web browser to access the login page.
       - Execute `main.py` to start the backend functionality.

### Usage:
  1. Login:
     description: 
       - Open `login.html` in a web browser.
       - Enter valid credentials to log in.
  2. Datetime Settings:
     description: Datetime is automatically set with local time upon system startup.
  3. Configuration File:
     description: The `config.txt` file stores important strings used within the system.

contributing: Contributions are welcome! Feel free to submit pull requests.
