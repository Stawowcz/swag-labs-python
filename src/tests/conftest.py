# src/fixtures/conftest.py
from __future__ import annotations

import pytest
from playwright.sync_api import Page, Playwright
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage

# Włącza plugin Playwrighta → udostępnia page, browser, context
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
