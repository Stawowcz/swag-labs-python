# src/tests/products/test_text_and_content.py
from __future__ import annotations

import pytest
from typing import List, TYPE_CHECKING
# from math import fabs
from playwright.sync_api import expect

import src.utils.env_utils as env
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
from src.types.common import CommonText
from src.types.common.common_enums import PRODUCT_NAMES

from src.utils.patterns import suspicious_patterns
from src.utils.patterns import forbidden_css_classes

if TYPE_CHECKING:
    from playwright.sync_api import Page


class TestProductsStandardUser:
    @pytest.fixture(autouse=True)
    def _login(self, page: "Page", login_page: LoginPage, products_page: ProductsPage) -> None:
        login_page.login(env.SAUCE_DEMO_STANDARD_USER, env.SAUCE_DEMO_PASSWORD)
        products_page.expect_url_contains("inventory")
        expect(products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_no_suspicious_patterns(self, products_page: ProductsPage) -> None:
        names = products_page.all_product_titles.all_text_contents()
        descriptions = products_page.all_product_descriptions.all_text_contents()
        errors: List[str] = []

        for name in names:
            for pattern in suspicious_patterns:
                if pattern.lower() in name.lower():
                    errors.append(f'Pattern "{pattern}" found in product name: {name}')

        for desc in descriptions:
            for pattern in suspicious_patterns:
                if pattern.lower() in desc.lower():
                    errors.append(f'Pattern "{pattern}" found in product description: {desc}')

        assert not errors, "Suspicious patterns detected:\n" + "\n".join(errors)

    def test_names_alignment(self, products_page: ProductsPage) -> None:
        elements = products_page.all_product_titles.all()
        misaligned: List[str] = []

        for idx, el in enumerate(elements):
            class_attr = el.get_attribute("class") or ""
            for forbidden in forbidden_css_classes:
                if forbidden in class_attr:
                    misaligned.append(f"Name {idx} contains forbidden class: {forbidden}")

        assert not misaligned, "Misaligned product names:\n" + "\n".join(misaligned)

    def test_add_to_cart_buttons_no_forbidden_classes(self, products_page: ProductsPage) -> None:
        buttons = products_page.add_to_cart_button_by_role.all()
        misaligned: List[str] = []

        for idx, btn in enumerate(buttons):
            class_attr = btn.get_attribute("class") or ""
            for forbidden in forbidden_css_classes:
                if forbidden in class_attr:
                    misaligned.append(
                        f"Add to cart button {idx} contains forbidden class: {forbidden}"
                    )

        assert not misaligned, "Forbidden classes on Add to Cart buttons:\n" + "\n".join(misaligned)


class TestProductsVisualUser:
    @pytest.fixture(autouse=True)
    def _login(self, page: "Page", login_page: LoginPage, products_page: ProductsPage) -> None:
        login_page.login(env.SAUCE_DEMO_VISUAL_USER, env.SAUCE_DEMO_PASSWORD)
        products_page.expect_url_contains("inventory")
        expect(products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_no_suspicious_patterns(self, products_page: ProductsPage) -> None:
        names = products_page.all_product_titles.all_text_contents()
        descriptions = products_page.all_product_descriptions.all_text_contents()
        errors: List[str] = []

        for name in names:
            for pattern in suspicious_patterns:
                if pattern.lower() in name.lower():
                    errors.append(f'Pattern "{pattern}" found in product name: {name}')

        for desc in descriptions:
            for pattern in suspicious_patterns:
                if pattern.lower() in desc.lower():
                    errors.append(f'Pattern "{pattern}" found in product description: {desc}')

        assert not errors, "Suspicious patterns detected (visual user):\n" + "\n".join(errors)

    def test_names_alignment(self, products_page: ProductsPage) -> None:
        elements = products_page.all_product_titles.all()
        misaligned: List[str] = []

        for idx, el in enumerate(elements):
            class_attr = el.get_attribute("class") or ""
            for forbidden in forbidden_css_classes:
                if forbidden in class_attr:
                    misaligned.append(f"Name {idx} contains forbidden class: {forbidden}")

        assert not misaligned, "Misaligned product names (visual user):\n" + "\n".join(misaligned)

    def test_add_to_cart_buttons_no_forbidden_classes(self, products_page: ProductsPage) -> None:
        buttons = products_page.add_to_cart_button_by_role.all()
        misaligned: List[str] = []

        for idx, btn in enumerate(buttons):
            class_attr = btn.get_attribute("class") or ""
            for forbidden in forbidden_css_classes:
                if forbidden in class_attr:
                    misaligned.append(
                        f"Add to cart button {idx} contains forbidden class: {forbidden}"
                    )

        assert not misaligned, (
            "Forbidden classes on Add to Cart buttons (visual user):\n" + "\n".join(misaligned)
        )


class TestPriceConsistencyBetweenUsers:
    def test_compare_prices_standard_problem_error(
        self,
        login_page: "LoginPage",
        products_page: "ProductsPage",
    ) -> None:
        # --- standard user ---
        login_page.login(env.SAUCE_DEMO_STANDARD_USER, env.SAUCE_DEMO_PASSWORD)
        products_page.expect_url_contains("inventory")
        standard_prices: list[float] = [
            products_page.get_product_price_by_name(product_name)
            for product_name in PRODUCT_NAMES
        ]

        products_page.open_menu()
        products_page.click_logout()

        login_page.login(env.SAUCE_DEMO_PROBLEM_USER, env.SAUCE_DEMO_PASSWORD)
        problem_user_prices: list[float] = [
            products_page.get_product_price_by_name(product_name)
            for product_name in PRODUCT_NAMES
        ]

        products_page.open_menu()
        products_page.click_logout()

        login_page.login(env.SAUCE_DEMO_ERROR_USER, env.SAUCE_DEMO_PASSWORD)
        error_user_prices: list[float] = [
            products_page.get_product_price_by_name(product_name)
            for product_name in PRODUCT_NAMES
        ]

        problem_user_price_mismatches: list[str] = []
        error_user_price_mismatches: list[str] = []

        for index, product_name in enumerate(PRODUCT_NAMES):
            if abs(problem_user_prices[index] - standard_prices[index]) > 0.01:
                problem_user_price_mismatches.append(
                    f"Price mismatch (problem vs standard) for '{product_name}': "
                    f"{problem_user_prices[index]} vs {standard_prices[index]}"
                )

        for index, product_name in enumerate(PRODUCT_NAMES):
            if abs(error_user_prices[index] - standard_prices[index]) > 0.01:
                error_user_price_mismatches.append(
                    f"Price mismatch (error vs standard) for '{product_name}': "
                    f"{error_user_prices[index]} vs {standard_prices[index]}"
                )

        assert not problem_user_price_mismatches, (
            "Price mismatches (problem vs standard):\n" + "\n".join(problem_user_price_mismatches)
        )
        assert not error_user_price_mismatches, (
            "Price mismatches (error vs standard):\n" + "\n".join(error_user_price_mismatches)
        )