import pytest
from unittest.mock import patch, Mock
from cart import Cart, MAX_QUANTITY_PER_PRODUCT


def test_add_product_to_cart(capsys):
	cart = Cart()
	product = "apple"
	cart.add_to_cart(product)
	captured = capsys.readouterr()
	assert f"{product} successfully added to cart. Quantity now: 1" in captured.out

def test_exceed_max_quantity_per_product():
	cart = Cart()
	product = "apple"
	for _ in range(MAX_QUANTITY_PER_PRODUCT):
		cart.add_to_cart(product)
	with pytest.raises(Exception) as exc: 
		cart.add_to_cart(product)
	assert str(exc.value) == f"You can't add more than {MAX_QUANTITY_PER_PRODUCT} items per product" 

def test_total_price_empty_cart():
	cart = Cart()
	assert cart.total_price() == 0.0

@patch("cart.ProductDatabase")
def test_total_price_with_items(product_db):
	cart = Cart()
	instance = product_db.return_value
	cart.carts = {"apple": 1, "banana": 1, "orange": 3}
	def item_price(item):
		return {"apple": 10.0, "banana": 5.0, "orange": 1.0}[item]
	instance.get_price.side_effect = item_price
	assert cart.total_price() == 18.0
	
		
	
	
