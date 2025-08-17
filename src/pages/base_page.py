from __future__ import annotations

import re
from typing import Optional, Literal
from playwright.sync_api import Page, Locator, expect

WaitUntil = Literal["commit", "domcontentloaded", "load", "networkidle"]
WaitState = Literal["attached", "detached", "hidden", "visible"]


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title: Locator = self.page.get_by_test_id("title")

    def goto(self, url: str = "/", wait_until: WaitUntil = "load") -> None:
        self.page.goto(url, wait_until=wait_until)

    def safe_click(
        self,
        locator: Locator,
        state: WaitState = "visible",
        timeout: Optional[float] = None,
    ) -> None:
        locator.wait_for(state=state, timeout=timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        locator.click(timeout=timeout)

    def safe_fill(
        self,
        locator: Locator,
        value: str,
        state: WaitState = "visible",
        timeout: Optional[float] = None,
    ) -> None:
        locator.wait_for(state=state, timeout=timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        locator.fill(value, timeout=timeout)

    def safe_clear(
        self,
        locator: Locator,
        state: WaitState = "visible",
        timeout: Optional[float] = None,
    ) -> None:
        locator.wait_for(state=state, timeout=timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        locator.fill("", timeout=timeout)

    def go_back(self) -> None:
        self.page.go_back()

    def go_forward(self) -> None:
        self.page.go_forward()

    def reload_page(self) -> None:
        self.page.reload()

    def expect_url_contains(self, path: str) -> None:
        expect(self.page).to_have_url(re.compile(f".*{re.escape(path)}"))
