class Kettle:
	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)  # Kenwood
print(kenwood.price)  # 8.99

# update the price
kenwood.price = 12.75
print(kenwood.price)
