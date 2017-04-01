class Cards:
	"""Makes 1 card at a time, we probably have to use a loop to make them all, or just use the deck"""
	def __init__(self,Display_in,PointValue_in,Suit_in):
		self.DisplayName = Display_in 
		self.PointValue = PointValue_in 
		self.Suit = Suit_in 
		

	def __str__(self):
		return self.DisplayName
