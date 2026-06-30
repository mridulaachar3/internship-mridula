# test_cart.py

import unittest
from unittest.mock import patch, MagicMock
from cart import Cart


class TestCart(unittest.TestCase):

    # setUp runs before every test - so each test gets a fresh cart
    # this is a fixture
    def setUp(self):
        self.cart = Cart()
        self.cart.add_item("Laptop", 55000, 1)
        self.cart.add_item("Phone", 20000, 2)

    # tearDown runs after every test
    def tearDown(self):
        self.cart.clear()


    # add item tests

    def test_add_new_item(self):
        self.cart.add_item("Headphones", 3000, 1)
        self.assertIn("Headphones", self.cart.items)

    def test_add_same_item_twice(self):
        # adding laptop again should increase qty, not add duplicate
        self.cart.add_item("Laptop", 55000, 1)
        self.assertEqual(self.cart.items["Laptop"]["qty"], 2)

    def test_add_item_zero_qty(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Mouse", 500, 0)

    def test_add_item_negative_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Keyboard", -100, 1)


    # remove item tests

    def test_remove_item(self):
        self.cart.remove_item("Phone")
        self.assertNotIn("Phone", self.cart.items)

    def test_remove_item_not_in_cart(self):
        with self.assertRaises(KeyError):
            self.cart.remove_item("Tablet")


    # total tests

    def test_get_total(self):
        # laptop 55000x1 + phone 20000x2 = 95000
        self.assertEqual(self.cart.get_total(), 95000)

    def test_total_empty_cart(self):
        self.cart.clear()
        self.assertEqual(self.cart.get_total(), 0)


    # discount tests

    def test_apply_discount(self):
        # 10% off 95000 should be 85500
        self.assertEqual(self.cart.apply_discount(10), 85500.0)

    def test_zero_discount(self):
        self.assertEqual(self.cart.apply_discount(0), 95000)

    def test_full_discount(self):
        self.assertEqual(self.cart.apply_discount(100), 0.0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.cart.apply_discount(110)


    # misc tests

    def test_item_count(self):
        # laptop qty 1 + phone qty 2 = 3 total
        self.assertEqual(self.cart.item_count(), 3)

    def test_cart_is_not_empty(self):
        self.assertFalse(self.cart.is_empty())

    def test_cart_empty_after_clear(self):
        self.cart.clear()
        self.assertTrue(self.cart.is_empty())

    def test_update_qty(self):
        self.cart.update_qty("Laptop", 5)
        self.assertEqual(self.cart.items["Laptop"]["qty"], 5)

    def test_update_qty_invalid(self):
        with self.assertRaises(ValueError):
            self.cart.update_qty("Laptop", -1)


    # mocking tests
    # mock = replacing a real function with a fake one for testing
    # useful when you dont want to call actual APIs or services

    @patch("cart.Cart.apply_discount")
    def test_mock_discount(self, mock_discount):
        mock_discount.return_value = 500.0
        result = self.cart.apply_discount(10)
        mock_discount.assert_called_once_with(10)
        self.assertEqual(result, 500.0)

    def test_mock_payment_gateway(self):
        # pretending there's a payment API without actually calling it
        payment = MagicMock()
        payment.process.return_value = {"status": "success", "txn_id": "TXN123"}

        response = payment.process(self.cart.get_total())

        self.assertEqual(response["status"], "success")
        self.assertIn("txn_id", response)
        payment.process.assert_called_once_with(95000)


if __name__ == "__main__":
    unittest.main(verbosity=2)