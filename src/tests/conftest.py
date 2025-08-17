import pytest

@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright):
    """
    Ustawia atrybut identyfikujący testowe selektory na 'data-test',
    odpowiednik: use: { testIdAttribute: "data-test" }.
    """
    playwright.selectors.set_test_id_attribute("data-test")
