"""
The database class file
"""

class DataBase(object):
	"""The database class for creating an empty database"""
	def __init__(self, name, *columns):
		self.columns = list(columns)
		self.rows = []
		self.name = name
	def save(self):
		"""saves the database to name.txt under standard format"""
		pass

