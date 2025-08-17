# src/tests/auth/test_negative.py
from __future__ import annotations

import pytest
from typing import TYPE_CHECKING
from playwright.sync_api import expect

from src.pages.login_page import LoginPage
from src.types.auth.login_enums import LoginPageErrorMessages as Err

if TYPE_CHECKING:
    from src.tests.conftest import UserCredentials  # tylko do typów

class TestNegativeAuth:
    @pytest.fixture(autouse=True)
    def _setup(self, login_page: LoginPage) -> None:
        self.login_page = login_page

    def test_should_show_error_for_incorrect_username(
        self, incorrect_user: "UserCredentials"
    ) -> None:
        self.login_page.login(incorrect_user["username"], incorrect_user["password"])
        expect(self.login_page.error_button).to_be_visible()
        expect(self.login_page.error_message).to_have_text(Err.INVALID_CREDS.value)

    def test_should_show_error_for_incorrect_password(
        self, incorrect_password: "UserCredentials"
    ) -> None:
        self.login_page.login(incorrect_password["username"], incorrect_password["password"])
        expect(self.login_page.error_button).to_be_visible()
        expect(self.login_page.error_message).to_have_text(Err.INVALID_CREDS.value)
