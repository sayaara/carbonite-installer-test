# Carbonite Installer Automation Assignment

This project demonstrates a sample Pytest-based automation framework using **Pywinauto** to automate user interaction with the **Carbonite Windows installer**.

It also includes:
- A standalone Python file format_date.py with a custom method format_date()
- An Excel spreadsheet (Test_Cases_Trial_Sign-Up _and_Installation_for_Carbonite Safe) containing manually created test cases

---

## Project Structure

```
carbonite_installer_automation/
├── conftest.py                # Pytest fixture for app setup/teardown
├── requirements.txt           # Required Python packages
├── README.md                  # Project instructions
├── format_date.py             # Custom method implementation
├── Test_Cases_Trial_Sign-Up _and_Installation_for_Carbonite Safe.xlsx   # Manual test cases spreadsheet
├── pages/
│   └── installer_page.py      # Page Object for installer UI
├── tests/
│   └── test_installer.py      # Test cases for checkbox and cancellation flow
└── logs/
    └── test_log.log           # Log file generated during test execution
```

---

## Requirements

- Windows OS (required for `pywinauto`)
- Python 3.8 or later
- Local copy of the **Carbonite Installer executable**

> Important: Update the path to the Carbonite installer in `conftest.py` before running the tests:

```python
app = Application(backend="uia").start(r"C:\Path\To\Your\Installer.exe")
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sayaara/carbonite-installer-test.git
cd carbonite-installer-test
```

### 2. (Optional) Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Tests

To execute the test suite, run the following command:

Tests require administrator privileges

1. Open Command Prompt as Administrator.
2. Navigate to the project folder.
3. Run the following command

```bash
pytest -v
```

> This will launch the Carbonite installer, check the agreement checkbox, and cancel the setup with confirmation.

> Test logs will be saved to `logs/test_log.log`.

---

## Logging

A basic logging setup is included. Logs will be saved to:
```
logs/test_log.log
```

---

## Contact
aravindhanv@gmail.com
Please let me know if you face any issues running the project.  
Thank you for your time and consideration!