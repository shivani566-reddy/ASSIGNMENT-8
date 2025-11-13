import unittest
from datetime import datetime
from typing import List, Tuple

# --- Implementation under test ---

class ShoppingCart:

    def __init__(self):
        self._items: List[Tuple[str, float]] = []

    def add_item(self, name: str, price: float) -> None:
        if not isinstance(name, str) or not name:
            raise TypeError("name must be a non-empty string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if price < 0:
            raise ValueError("price must be non-negative")
        self._items.append((name, float(price)))

    def remove_item(self, name: str) -> bool:
        """Remove the first occurrence of an item by name. Return True if removed, False if not found."""
        for i, (n, _) in enumerate(self._items):
            if n == name:
                del self._items[i]
                return True
        return False

    def total_cost(self) -> float:
        return sum(price for _, price in self._items)


def convert_date_format(date_str: str) -> str:

    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string")
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("empty date string")
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except Exception as e:
        raise ValueError(f"invalid date format or value: {date_str}") from e
    return dt.strftime("%d-%m-%Y")


# --- Tests ---

class TestShoppingCart(unittest.TestCase):
    def test_add_single_item_and_total(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.50)
        self.assertAlmostEqual(cart.total_cost(), 1.50)

    def test_add_multiple_items_and_total(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.50)
        cart.add_item("banana", 0.75)
        cart.add_item("milk", 2.00)
        self.assertAlmostEqual(cart.total_cost(), 4.25)

    def test_remove_item_reduces_total(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.50)
        cart.add_item("banana", 0.75)
        removed = cart.remove_item("banana")
        self.assertTrue(removed)
        self.assertAlmostEqual(cart.total_cost(), 1.50)

    def test_remove_nonexistent_item_returns_false(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.50)
        removed = cart.remove_item("orange")
        self.assertFalse(removed)
        self.assertAlmostEqual(cart.total_cost(), 1.50)

    def test_add_negative_price_raises(self):
        cart = ShoppingCart()
        with self.assertRaises(ValueError):
            cart.add_item("apple", -0.99)

    def test_add_invalid_name_or_price_type_raises(self):
        cart = ShoppingCart()
        with self.assertRaises(TypeError):
            cart.add_item("", 1.0)
        with self.assertRaises(TypeError):
            cart.add_item("apple", "one dollar")

    def test_duplicate_items_are_allowed_and_removed_one_by_one(self):
        cart = ShoppingCart()
        cart.add_item("cookie", 1.00)
        cart.add_item("cookie", 1.00)
        self.assertAlmostEqual(cart.total_cost(), 2.00)
        removed = cart.remove_item("cookie")
        self.assertTrue(removed)
        self.assertAlmostEqual(cart.total_cost(), 1.00)
        removed2 = cart.remove_item("cookie")
        self.assertTrue(removed2)
        self.assertAlmostEqual(cart.total_cost(), 0.00)
        # now no more cookies
        self.assertFalse(cart.remove_item("cookie"))


class TestConvertDateFormat(unittest.TestCase):
    def test_standard_conversion(self):
        self.assertEqual(convert_date_format("2025-12-31"), "31-12-2025")

    def test_leap_day_conversion(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")

    def test_invalid_format_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("31-12-2025")  # wrong input format

    def test_invalid_date_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2021-02-29")  # 2021 not a leap year

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_non_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            convert_date_format(20251231)

    def test_whitespace_around_input(self):
        self.assertEqual(convert_date_format(" 2023-01-05 "), "05-01-2023")

    def test_month_out_of_range_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01")

    def test_day_out_of_range_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-04-31")  # April has 30 days


if __name__ == "__main__":
    unittest.main(verbosity=2)