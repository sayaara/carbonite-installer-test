# conftest.py
import pytest
from pywinauto import Application, timings
import logging
import os
import sys

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/test_log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


@pytest.fixture(scope="function")
def setup_installer():
    timings.Timings.window_find_timeout = 10
    # replace with actual path
    app = Application(backend="uia").start(r"C:\Users\aravi\Downloads\Carbonite-personal-client.exe")  
    dlg = app.window(title_re="Installing Carbonite")
    logging.info("Installer started.")
    yield app, dlg
    # teardown
    try:
        app.kill()
        logging.info("Closing the installer")
    except Exception as e:
        logging.warning(f"App might have already been closed during the test: {e}")

# Pytest hook to log test results
def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.passed:
            logging.info(f"TEST PASSED: {report.nodeid}")
        elif report.failed:
            logging.error(f"TEST FAILED: {report.nodeid}")
        elif report.skipped:
            logging.warning(f"TEST SKIPPED: {report.nodeid}")