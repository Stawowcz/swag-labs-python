# src/tests/auth/test_positive.py
from __future__ import annotations
from time import perf_counter
from playwright.sync_api import expect
import src.utils.env_utils as env
from src.types.common import CommonText
from src.types.auth import LoginPageErrorMessages

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from playwright.sync_api import Page
    from src.pages.login_page import LoginPage
    from src.pages.products_page import ProductsPage


def test_should_log_in_standard_user(
    page: "Page",
    login_page: "LoginPage",
    products_page: "ProductsPage",
) -> None:
    login_page.goto(env.SAUCE_DEMO_BASEURL)
    login_page.fill_user_name_field(env.SAUCE_DEMO_STANDARD_USER)
    login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)
    login_page.click_on_login_button()

    products_page.expect_url_contains("inventory")
    expect(products_page.primary_header).to_contain_text(CommonText.PRIMARY_HEADER_TEXT)
    expect(products_page.hamburger_menu).to_be_visible()
    expect(products_page.shopping_cart_link).to_be_visible()


def test_should_log_in_locked_out_user_bug(
    page: "Page",
    login_page: "LoginPage",
    products_page: "ProductsPage",
) -> None:
    login_page.goto(env.SAUCE_DEMO_BASEURL)
    login_page.fill_user_name_field(env.SAUCE_DEMO_LOCKED_OUT_USER)
    login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)
    login_page.click_on_login_button()
    expect(login_page.error_message).to_contain_text(LoginPageErrorMessages.LOCKED_OUT)


def test_should_log_in_glitch_user_bug_slow(
    page: "Page",
    login_page: "LoginPage",
    products_page: "ProductsPage",
) -> None:
    login_page.goto(env.SAUCE_DEMO_BASEURL)
    login_page.fill_user_name_field(env.SAUCE_DEMO_PERFORMACE_GLITCH_USER)
    login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)

    start = perf_counter()
    login_page.click_on_login_button()

    expect(products_page.primary_header).to_contain_text(CommonText.PRIMARY_HEADER_TEXT)
    expect(products_page.hamburger_menu).to_be_visible()
    expect(products_page.shopping_cart_link).to_be_visible()

    duration_ms = (perf_counter() - start) * 1000
    assert duration_ms <= 1500, f"Login took too long: {duration_ms:.0f} ms"
