# src/pages/login_page.py
from playwright.sync_api import Page, Locator
from .base_page import BasePage
from src.utils import env_utils as env


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_name_field: Locator = self.page.get_by_test_id("username")
        self.password_field: Locator = self.page.get_by_test_id("password")
        self.login_button: Locator = self.page.get_by_test_id("login-button")
        self.error_button: Locator = self.page.get_by_test_id("error-button")
        self.error_message: Locator = self.page.get_by_test_id("error")

    def click_on_login_button(self) -> None:
        self.safe_click(self.login_button)

    def fill_user_name_field(self, user_name: str) -> None:
        self.safe_fill(self.user_name_field, user_name)

    def fill_password_field(self, password: str) -> None:
        self.safe_fill(self.password_field, password)

    def login(self, user_name: str, password: str) -> None:
        self.goto(env.SAUCE_DEMO_BASEURL)
        self.fill_user_name_field(user_name)
        self.fill_password_field(password)
        self.click_on_login_button()
