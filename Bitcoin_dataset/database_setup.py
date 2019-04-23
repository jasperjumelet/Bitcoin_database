import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	""" create a database connection to a SQLite database """
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		conn.close()

	return None

def databasesetup(connection):
	"""Create the tables"""
	connection.execute("""CREATE TABLE Bitcoindatabase(
		Datetimer Timestamp,
		Price FLOAT(20)
		);""")

def main():
	try:
		conn = sqlite3.connect("pythonsqlite.db")
	except Error as e:
		print(e)
	connection = conn.cursor()
	with conn:
		databasesetup(connection)

if __name__ == "__main__":
	main()
