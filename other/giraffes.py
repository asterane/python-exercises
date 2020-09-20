class Things:
    pass

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
	    print('breathing')
    def move(self):
	    print('moving')
    def eat_food(self):
	    print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
	    print('feeding young')

class Giraffes(Mammals):
	def __init__(self, spots):
		self.giraffe_spots = spots
	def eat_leaves_from_trees(self):
		self.eat_food()
	def find_food(self):
		self.move()
		print("I've found food!")
		self.eat_food()
	def dance_a_jig(self):
		self.move()
		self.move()
		self.move()
		self.move()
	def leftfootforward(self):
		print('left foot forward')
	def leftfootback(self):
		print('left foot back')
	def rightfootforward(self):
		print('right foot forward')
	def rightfootback(self):
		print('right foot back')
	def dance(self):
                self.leftfootforward()
                self.leftfootback()
                self.rightfootforward()
                self.rightfootback()
                self.leftfootback()
                self.rightfootback()
                self.rightfootforward()
                self.leftfootforward()
