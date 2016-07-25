from database import *
users = DataBase("users", "first", "last")
users.add_entry("Connor", "Dewar")
print(users.query("select * where first is Connor"))
users.add_entry("Yolo", "Dewar")
print(users.query("select * where last is Dewar"))
