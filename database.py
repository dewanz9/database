"""
The database class file
"""
import os

class DataBase(object):
	"""The database class for creating an empty database"""
	def __init__(self, name, *columns):
		"""The initializer for creating a new database"""
		self.columns = list(columns)
		self.rows = []
		self.name = name
	
	def add_entry(self, *fields):
		"""adds a new to entry to self.rows"""
		#check to see if the right amount of args was passed in
		fields = list(fields)
		if len(fields) < len(self.columns):
			print("too few arguments passed in")
			return -1
		elif len(fields) > len(self.columns):
			print("too many arguments passed in")
		else:
			#right amount of arguments passed in. add them
			self.rows.append(fields)
		print(self.rows)

	def save(self):
		"""saves the database to name.txt under standard format"""
		lines_to_write = []
		#create the column line in lines_to_write
		temp_str = ""
		for column in self.columns:
			temp_str += column + ','
		temp_str = temp_str[:-1]
		lines_to_write.append(temp_str)

		#add the rows to the lines_to_write array
		for row in self.rows:
			temp_str = ''
			for entry in row:
				temp_str += entry + ','
			temp_str = temp_str[:-1]
			lines_to_write.append(temp_str)
		print(lines_to_write)	

