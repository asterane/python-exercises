print("Welcome to Projectile Motion v1.0, written in Python.")

class Projectile(object):
	def __init__(self, name, mass, position):
		self.name = name
		self.mass = mass

class Launcher(object):
	def __init__(self, height, angle):
		self.height = height
		self.angle = angle

class Environment(object):
	def __init__(self, size, lheight):
		self.size = size
		self.lheight = lheight

	def rendergrid(self):
		global x
		global y
		global grid
		global temp
		y = int(self.size.pop())
		x = int(self.size.pop())
		grid = []
		temp = []
		for i in range(1, x):
			temp.append(i * 10)
			for j in range(1, y):
				grid.append(temp)
				del temp[:]
				print("X")
                s = temp
		print(grid)

b = Environment([5, 5], 3)
b.rendergrid()


