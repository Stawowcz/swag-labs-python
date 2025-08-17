# src/pages/products_page.py
import re
from playwright.sync_api import Page, Locator
from .base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # top / header
        self.primary_header: Locator = self.page.get_by_test_id("primary-header")
        self.hamburger_menu: Locator = self.page.get_by_test_id("open-menu")
        self.hamburger_menu_button: Locator = self.page.locator(
            "#react-burger-menu-btn"
        )

        # cart / shop controls
        self.shopping_cart_link: Locator = self.page.get_by_test_id(
            "shopping-cart-link"
        )
        self.add_to_cart_button: Locator = self.page.get_by_test_id("add-to-cart")
        self.remove_from_cart_button: Locator = self.page.get_by_test_id("remove")
        self.shopping_cart_container: Locator = self.page.locator(
            "#shopping_cart_container"
        )

        # side menu / actions
        self.reset_app_button: Locator = self.page.get_by_test_id("reset-sidebar-link")
        self.menu_logout_link: Locator = self.page.get_by_test_id("logout-sidebar-link")
        self.menu_about_link: Locator = self.page.get_by_test_id("about-sidebar-link")

        # misc UI
        self.cart_badge: Locator = self.page.get_by_test_id("shopping-cart-badge")
        self.sort_dropdown: Locator = self.page.get_by_test_id("product-sort-container")
        self.back_to_products_button: Locator = self.page.get_by_test_id(
            "back-to-products"
        )

        # lists
        self.all_product_descriptions: Locator = self.page.get_by_test_id(
            "inventory-item-desc"
        )
        self.all_product_titles: Locator = self.page.get_by_test_id(
            "inventory-item-name"
        )
        self.all_product_prices: Locator = self.page.get_by_test_id(
            "inventory-item-price"
        )

        # generic "Add to cart" by role (regex)
        self.add_to_cart_button_by_role: Locator = self.page.get_by_role(
            "button", name=re.compile(r"add to cart", re.I)
        )

        # burger menu overlay
        self.burger_menu_close_button: Locator = self.page.locator(
            "#react-burger-cross-btn"
        )
        self.burger_menu: Locator = self.page.locator(".bm-menu-wrap")

    # ----- helpers / getters -----
    def get_product_image_by_alt_text(self, alt_text: str) -> Locator:
        return self.page.locator(f'img[alt="{alt_text}"]')

    def get_add_to_cart_button(self, product_id: str) -> Locator:
        return self.page.get_by_test_id(f"add-to-cart-{product_id}")

    def get_remove_from_cart_button(self, product_id: str) -> Locator:
        return self.page.get_by_test_id(f"remove-{product_id}")

    # ----- actions -----
    def click_on_cart_basket(self) -> None:
        self.safe_click(self.shopping_cart_link)

    def wait_for_cart_badge(self) -> Locator:
        self.cart_badge.wait_for(state="visible")
        self.cart_badge.scroll_into_view_if_needed()
        return self.cart_badge

    def add_product_to_cart(self, product_id: str) -> None:
        self.safe_click(self.get_add_to_cart_button(product_id))

    def add_to_cart_from_product_details(self) -> None:
        self.safe_click(self.add_to_cart_button)

    def remove_from_product_details(self) -> None:
        self.safe_click(self.remove_from_cart_button)

    def remove_product_from_cart(self, product_id: str) -> None:
        self.safe_click(self.get_remove_from_cart_button(product_id))

    def open_menu(self) -> None:
        self.safe_click(self.hamburger_menu_button)

    def click_about(self) -> None:
        self.safe_click(self.menu_about_link)

    def click_logout(self) -> None:
        self.safe_click(self.menu_logout_link)

    def click_reset_app(self) -> None:
        self.safe_click(self.reset_app_button)

    def click_back_to_products(self) -> None:
        self.safe_click(self.back_to_products_button)

    def click_burger_menu_close_button(self) -> None:
        self.safe_click(self.burger_menu_close_button)
