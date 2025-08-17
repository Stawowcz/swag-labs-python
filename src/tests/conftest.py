# src/fixtures/conftest.py
from __future__ import annotations

from typing import TypedDict, Protocol
import pytest
from playwright.sync_api import Page, Playwright

from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
import src.utils.env_utils as env

pytest_plugins = ("pytest_playwright",)


@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright) -> None:
    """
    Ustawia atrybut identyfikujący testowe selektory na 'data-test',
    odpowiednik: use: { testIdAttribute: "data-test" }.
    """
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    return ProductsPage(page)


class UserCredentials(TypedDict):
    username: str
    password: str


class LoginAs(Protocol):
    def __call__(self, user: UserCredentials) -> ProductsPage: ...


@pytest.fixture
def login_as(page: Page) -> LoginAs:
    """
    Fabryka logowania: zaloguj jako dowolny użytkownik i zwróć ProductsPage.
    Użycie w teście:
        p = login_as(standard_user)
    """

    def _login_as(user: UserCredentials) -> ProductsPage:
        lp = LoginPage(page)
        pp = ProductsPage(page)
        lp.goto(env.SAUCE_DEMO_BASEURL)
        lp.fill_user_name_field(user["username"])
        lp.fill_password_field(user["password"])
        lp.click_on_login_button()
        return pp

    return _login_as


@pytest.fixture
def standard_user() -> UserCredentials:
    return {
        "username": env.SAUCE_DEMO_STANDARD_USER,
        "password": env.SAUCE_DEMO_PASSWORD,
    }


@pytest.fixture
def locked_user() -> UserCredentials:
    return {
        "username": env.SAUCE_DEMO_LOCKED_OUT_USER,
        "password": env.SAUCE_DEMO_PASSWORD,
    }


@pytest.fixture
def incorrect_user() -> UserCredentials:
    return {
        "username": env.SAUCE_DEMO_INCORRECT_USER,
        "password": env.SAUCE_DEMO_PASSWORD,
    }


@pytest.fixture
def incorrect_password() -> UserCredentials:
    return {
        "username": env.SAUCE_DEMO_STANDARD_USER,
        "password": env.SAUCE_DEMO_INCORRECT_PASSWORD,
    }


@pytest.fixture
def problem_user() -> UserCredentials:
    return {
        "username": env.SAUCE_DEMO_PROBLEM_USER,
        "password": env.SAUCE_DEMO_PASSWORD,
    }


@pytest.fixture
def performance_glitch_user() -> UserCredentials:
    return {
        "username": env.SAUCE_DEMO_PERFORMACE_GLITCH_USER,
        "password": env.SAUCE_DEMO_PASSWORD,
    }


@pytest.fixture
def error_user() -> UserCredentials:
    return {"username": env.SAUCE_DEMO_ERROR_USER, "password": env.SAUCE_DEMO_PASSWORD}


@pytest.fixture
def visual_user() -> UserCredentials:
    return {"username": env.SAUCE_DEMO_VISUAL_USER, "password": env.SAUCE_DEMO_PASSWORD}
