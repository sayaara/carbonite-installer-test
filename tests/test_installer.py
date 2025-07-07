import pytest
from pages.installer_page import InstallerPage

def test_checkbox_can_be_checked(setup_installer):
    app, dlg = setup_installer
    page = InstallerPage(dlg)

    page.check_terms_checkbox()

    assert page.is_checkbox_checked(), "Checkbox should be checked"
    assert page.is_continue_enabled(), "'Continue' should be enabled after checking the checkbox"

def test_cancel_setup_triggers_confirmation(setup_installer):
    app, dlg = setup_installer
    page = InstallerPage(dlg)

    page.click_no_thanks()
    # page.confirm_cancel(app)
    page.confirm_cancel(dlg)

    # verify that the installer window is closed
    assert not dlg.exists(timeout=5), "Installer dialog should be closed after confirming cancels"

# def test_setup_can_be_continued(setup_installer):
#     app, dlg = setup_installer
#     page = InstallerPage(dlg)
#     page.click_continue()