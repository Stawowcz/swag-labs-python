# src/types/common/common_enums.py
from enum import Enum, IntEnum

class CommonText(str, Enum):
    PRIMARY_HEADER_TEXT = "Swag Labs"
    PRODUCTS_PAGE_TITLE = "Products"

class ProductNames(str, Enum):
    BACKPACK = "Sauce Labs Backpack"
    BIKE_LIGHT = "Sauce Labs Bike Light"
    BOLT_TSHIRT = "Sauce Labs Bolt T-Shirt"
    FLEECE_JACKET = "Sauce Labs Fleece Jacket"
    ONESIE = "Sauce Labs Onesie"
    RED_TSHIRT = "Test.allTheThings() T-Shirt (Red)"

class CommonValues(IntEnum):
    TIME_LIMIT_MS = 1500

# krotka stringów – Pylance będzie znał typ
PRODUCT_NAMES: tuple[str, ...] = tuple(p.value for p in ProductNames)
