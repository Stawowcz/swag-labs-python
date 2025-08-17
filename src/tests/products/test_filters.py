# src/tests/products/test_filters.py
from time import perf_counter
import pytest
from playwright.sync_api import expect
from typing import TYPE_CHECKING
from src.types.common import CommonText

from src.pages.products_page import ProductsPage

# typy tylko dla podpowiedzi (nie ładowane w runtime)
if TYPE_CHECKING:
    from src.tests.conftest import LoginAs, UserCredentials

TIME_LIMIT_MS = 1500


class TestFiltersStandardUser:
    @pytest.fixture(autouse=True)
    def _login_before_each(
        self, login_as: "LoginAs", standard_user: "UserCredentials"
    ) -> None:
        self.products_page: "ProductsPage" = login_as(standard_user)
        self.products_page.expect_url_contains("inventory")
        expect(self.products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_sort_az(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("az")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names)

    def test_sort_za(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("za")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names, reverse=True)

    def test_price_low_high(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("lohi")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices)

    def test_price_high_low(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("hilo")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices, reverse=True)


class TestFiltersProblemUser:
    @pytest.fixture(autouse=True)
    def _login_before_each(
        self, login_as: "LoginAs", problem_user: "UserCredentials"
    ) -> None:
        self.products_page: "ProductsPage" = login_as(problem_user)
        self.products_page.expect_url_contains("inventory")
        expect(self.products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_sort_az(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("az")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names)

    def test_sort_za(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("za")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names, reverse=True)

    def test_price_low_high(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("lohi")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices)

    def test_price_high_low(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("hilo")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices, reverse=True)


class TestFiltersErrorUser:
    @pytest.fixture(autouse=True)
    def _login_before_each(
        self, login_as: "LoginAs", error_user: "UserCredentials"
    ) -> None:
        self.products_page: "ProductsPage" = login_as(error_user)
        self.products_page.expect_url_contains("inventory")
        expect(self.products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_sort_az(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("az")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names)

    def test_sort_za(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("za")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names, reverse=True)

    def test_price_low_high(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("lohi")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices)

    def test_price_high_low(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("hilo")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices, reverse=True)


class TestFiltersVisualUser:
    @pytest.fixture(autouse=True)
    def _login_before_each(
        self, login_as: "LoginAs", visual_user: "UserCredentials"
    ) -> None:
        self.products_page: "ProductsPage" = login_as(visual_user)
        self.products_page.expect_url_contains("inventory")
        expect(self.products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_sort_az(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("az")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names)

    def test_sort_za(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("za")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names, reverse=True)

    def test_price_low_high(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("lohi")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices)

    def test_price_high_low(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("hilo")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices, reverse=True)


class TestFiltersPerfGlitchUser:
    @pytest.fixture(autouse=True)
    def _login_before_each(
        self, login_as: "LoginAs", performance_glitch_user: "UserCredentials"
    ) -> None:
        self.products_page: "ProductsPage" = login_as(performance_glitch_user)
        self.products_page.expect_url_contains("inventory")
        expect(self.products_page.title).to_have_text(CommonText.PRODUCTS_PAGE_TITLE)

    def test_sort_az(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("az")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names)

    def test_sort_za(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("za")
        names = [
            n.strip() for n in self.products_page.all_product_titles.all_text_contents()
        ]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert names == sorted(names, reverse=True)

    def test_price_low_high(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("lohi")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices)

    def test_price_high_low(self) -> None:
        start = perf_counter()
        self.products_page.sort_dropdown.select_option("hilo")
        raw = self.products_page.all_product_prices.all_text_contents()
        prices = [float(x.replace("$", "").strip()) for x in raw]
        assert (perf_counter() - start) * 1000 <= TIME_LIMIT_MS
        assert prices == sorted(prices, reverse=True)
