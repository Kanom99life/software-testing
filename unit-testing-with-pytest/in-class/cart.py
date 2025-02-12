from product_db import ProductDatabase

MAX_QUANTITY_PER_PRODUCT = 5

class Cart:

	def __init__(self): 
		self.carts = {} # type: dict[str, int]

	def add_to_cart(self, product: str):
		if product not in self.carts:
			self.carts[product] = 0
		if self.carts[product] < MAX_QUANTITY_PER_PRODUCT:
			self.carts[product] += 1
			print(f"{product} successfully added to cart. Quantity now: {self.carts[product]}")
		else:
			raise Exception(f"You can't add more than {MAX_QUANTITY_PER_PRODUCT} items per product")

	def total_price(self):
		if len(self.carts) == 0:
			return 0.0
		total_price = 0
		product_db = ProductDatabase()

		for product, quantity in self.carts.items():
			total_price += product_db.get_price(product) * quantity
		return total_price