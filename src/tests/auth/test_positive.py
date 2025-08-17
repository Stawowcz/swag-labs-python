# src/tests/auth/test_positive.py
from __future__ import annotations

import pytest
from time import perf_counter
from typing import TYPE_CHECKING
from playwright.sync_api import expect

import src.utils.env_utils as env
from src.types.common import CommonText
from src.types.auth.login_enums import LoginPageErrorMessages as Err

if TYPE_CHECKING:
    from src.pages.login_page import LoginPage
    from src.pages.products_page import ProductsPage


class TestPositiveAuth:
    @pytest.fixture(autouse=True)
    def _setup(self, login_page: "LoginPage", products_page: "ProductsPage") -> None:
        self.login_page = login_page
        self.products_page = products_page

    def test_should_log_in_standard_user(self) -> None:
        self.login_page.login(env.SAUCE_DEMO_STANDARD_USER, env.SAUCE_DEMO_PASSWORD)
        self.products_page.expect_url_contains("inventory")
        expect(self.products_page.primary_header).to_contain_text(
            CommonText.PRIMARY_HEADER_TEXT.value
        )
        expect(self.products_page.hamburger_menu).to_be_visible()
        expect(self.products_page.shopping_cart_link).to_be_visible()

    def test_should_log_in_locked_out_user_bug(self) -> None:
        self.login_page.login(env.SAUCE_DEMO_LOCKED_OUT_USER, env.SAUCE_DEMO_PASSWORD)
        expect(self.login_page.error_message).to_contain_text(Err.LOCKED_OUT.value)

    def test_should_log_in_glitch_user_bug_slow(self) -> None:
        self.login_page.goto(env.SAUCE_DEMO_BASEURL)
        self.login_page.fill_user_name_field(env.SAUCE_DEMO_PERFORMACE_GLITCH_USER)
        self.login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)

        start = perf_counter()
        self.login_page.click_on_login_button()

        expect(self.products_page.primary_header).to_contain_text(
            CommonText.PRIMARY_HEADER_TEXT.value
        )
        expect(self.products_page.hamburger_menu).to_be_visible()
        expect(self.products_page.shopping_cart_link).to_be_visible()

        duration_ms = (perf_counter() - start) * 1000
        assert duration_ms <= 1500, f"Login took too long: {duration_ms:.0f} ms"
