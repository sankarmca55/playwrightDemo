from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        
    #Username input method
    def enter_username(self, username: str):
        self.username_input.click()
        self.username_input.fill(username)
        self.page.wait_for_timeout(1000)  # Wait for 1 second
    
    #Password input method
    def enter_password(self, password: str):
        self.password_input.click()
        self.password_input.fill(password)
        self.page.wait_for_timeout(1000)  # Wait for 1 second
    
    #Login button click method
    def click_login(self):
        self.login_button.click()
        self.page.wait_for_timeout(1000)  # Wait for 3 seconds to ensure the dashboard is loaded