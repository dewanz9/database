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

	def save(self, path):
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
		

		if path[-1] != "/":
			path += "/"
		path += self.name + ".csv"
		#delete the old database file and write the new one to the same path
		if os.path.exists(path):
			os.remove(path)
		file_to_write = open(path, "w")
		for line in lines_to_write:
			file_to_write.write(line+"\n")
		file_to_write.close()

	def query(self, query_string):
		"""runs a query on the database and returns a list of rows"""
		commands = query_string.split(" ")
		if commands[0] == "select":
			#allgood
			commands.pop(0) #select
			commands.pop(0) #*
			commands.pop(0) #where
			#find the column index
			target_index = -1
			for _ in range(len(self.columns)):
				if self.columns[_] == commands[0]:
					target_index = _
					break
			if target_index == -1:
				print("Column '{}' not found".format(commands[0]))
			commands.pop(0)
			commands.pop(0)#is
			#find the rows
			return_rows = []
			for row in self.rows:
				if row[target_index] == commands[0]:
					return_rows.append(row)
				else:
					print(commands[0])
					print("failed:", end='')
					print(row[target_index])
			return return_rows
		else:
			#not allgood
			print("Command '{}' not recognized".format(commands[0]))




class DataBaseFromFile(DataBase):
	"""loads a db from a file"""
	def __init__(self, name):
		"""the init functin for databse from file"""
		#the input name should hold the path to db file
		if not os.path.exists(name):
			print("file does not exist")
		else:
			#path exists, so load and enter the database
			parts = name.split("/")
			self.name = parts[-1][:-4]
			database_file = open(name, "r")
			lines = database_file.readlines()
			database_file.close()
			processed_lines = []
			for entry in lines:
				processed_lines.append(entry.strip().split(","))
			self.columns = processed_lines[0]
			processed_lines.pop(0)
			self.rows = []
			for line in processed_lines:
				self.rows.append(line)

if __name__ == '__main__':
	print("Python database library")
