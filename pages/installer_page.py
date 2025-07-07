# pages/installer_page.py
import time

class InstallerPage:
    def __init__(self, dlg):
        self.dlg = dlg

    def check_terms_checkbox(self):
        checkbox = self.dlg.child_window(
            title="I agree to Carbonite's Terms of Service and acknowledge Carbonite's Privacy Policy",
            control_type="CheckBox",
            auto_id="crbSetupCheckbox"
        )
        checkbox.toggle()
        time.sleep(1)

    def is_checkbox_checked(self):
        checkbox = self.dlg.child_window(
            title="I agree to Carbonite's Terms of Service and acknowledge Carbonite's Privacy Policy",
            control_type="CheckBox"
        )
        return checkbox.get_toggle_state() == 1

    def is_continue_enabled(self):
        continue_btn = self.dlg.child_window(
            title="Continue",
            control_type="Hyperlink",
            auto_id="crbSetupButton1"
        )
        return continue_btn.is_enabled() and continue_btn.rectangle().width() > 0

    def click_no_thanks(self):
        no_thanks = self.dlg.child_window(
            title="No thanks",
            control_type="Hyperlink",
            auto_id="crbSetupButton2"
        )
        no_thanks.click_input()

    def confirm_cancel(self, app):
        confirm_dlg = app.child_window(title_re="Carbonite Setup")
        confirm_btn = confirm_dlg.child_window(title_re="Yes", control_type="Button")
        confirm_btn.click_input()

    def click_continue(self):
        continue_btn = self.dlg.child_window(
            title="Continue",
            control_type="Hyperlink",
            auto_id="crbSetupButton1"
        )
        continue_btn.click_input()