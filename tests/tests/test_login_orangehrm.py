import re
from playwright.sync_api import Page
from pages.orangehrm_login_page import LoginPage

def test_org_login(page: Page):
    Login_page = LoginPage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(1000)  # Wait for 3 seconds to ensure the page is fully loaded
      
    Login_page.enter_username("Admin")
    Login_page.enter_password("admin123")
    Login_page.click_login()
    
    
    