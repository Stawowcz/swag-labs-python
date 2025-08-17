# src/pages/base_page.py
import re
from typing import Optional
from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title: Locator = self.page.get_by_test_id("title")

    def goto(self, url: str = "/", wait_until: str = "load") -> None:
        self.page.goto(url, wait_until=wait_until)

    def safe_click(self, locator: Locator, state: str = "visible", timeout: Optional[int] = None) -> None:
        locator.wait_for(state=state, timeout=timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        locator.click()

    def safe_fill(self, locator: Locator, value: str, state: str = "visible", timeout: Optional[int] = None) -> None:
        locator.wait_for(state=state, timeout=timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        locator.fill(value)

    def safe_clear(self, locator: Locator, state: str = "visible", timeout: Optional[int] = None) -> None:
        locator.wait_for(state=state, timeout=timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        locator.clear()

    def go_back(self) -> None:
        self.page.go_back()

    def go_forward(self) -> None:
        self.page.go_forward()

    def reload_page(self) -> None:
        self.page.reload()

    def expect_url_contains(self, path: str) -> None:
        expect(self.page).to_have_url(re.compile(f".*{re.escape(path)}"))
