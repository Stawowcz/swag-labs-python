# src/tests/auth/test_positive.py
from time import perf_counter
from playwright.sync_api import expect
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
import src.utils.env_utils as env

PRIMARY_HEADER_TEXT = "Swag Labs"


def test_should_log_in_standard_user(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.goto(env.SAUCE_DEMO_BASEURL)
    login_page.fill_user_name_field(env.SAUCE_DEMO_STANDARD_USER)
    login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)
    login_page.click_on_login_button()

    products_page.expect_url_contains("inventory")
    expect(products_page.primary_header).to_contain_text(PRIMARY_HEADER_TEXT)
    expect(products_page.hamburger_menu).to_be_visible()
    expect(products_page.shopping_cart_link).to_be_visible()


def test_should_log_in_locked_out_user_bug(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.goto(env.SAUCE_DEMO_BASEURL)
    login_page.fill_user_name_field(env.SAUCE_DEMO_LOCKED_OUT_USER)
    login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)
    login_page.click_on_login_button()

    # BUG: user is locked – odwzorowujemy asercje z TS
    products_page.expect_url_contains("inventory")
    expect(products_page.primary_header).to_contain_text(PRIMARY_HEADER_TEXT)
    expect(products_page.hamburger_menu).to_be_visible()
    expect(products_page.shopping_cart_link).to_be_visible()


def test_should_log_in_glitch_user_bug_slow(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.goto(env.SAUCE_DEMO_BASEURL)
    login_page.fill_user_name_field(env.SAUCE_DEMO_PERFORMACE_GLITCH_USER)
    login_page.fill_password_field(env.SAUCE_DEMO_PASSWORD)

    start = perf_counter()
    login_page.click_on_login_button()

    expect(products_page.primary_header).to_contain_text(PRIMARY_HEADER_TEXT)
    expect(products_page.hamburger_menu).to_be_visible()
    expect(products_page.shopping_cart_link).to_be_visible()

    duration_ms = (perf_counter() - start) * 1000
    assert duration_ms <= 1500, f"Login took too long: {duration_ms:.0f} ms"
