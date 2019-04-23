import sqlite3
from sqlite3 import Error
from urllib.request import urlopen
import datetime
import json
import time
import sys

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

def databaseupdater(timer, connection):
	quit = False
	while quit == False:

		time.sleep(timer)

		with urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as response:
			source = response.read()			
		data = json.loads(source)

		insert_data = (str(datetime.datetime.now()), str(data['bpi']['EUR']['rate'])) 
			
		insert = """INSERT INTO Bitcoindatabase(Datetimer,Price) 
					VALUES (?,?) """

		connection.execute(insert, insert_data)

	return connection.lastrowid


def main():
	
	try:
		conn = sqlite3.connect("pythonsqlite.db")

	except Error as e:
		print(e)
	
	connection = conn.cursor()
	with conn:

		try:
			if sys.argv[1] == "d".lower():
				databaseupdater(86400, connection)
			elif sys.argv[1] == "h".lower():
				databaseupdater(3600, connection)
			elif sys.argv[1] == "m".lower():
				databaseupdater(60, connection)
			elif sys.argv[1] == str(range(0,99999)):	
				databaseupdater(int(sys.argv[1]), connection)

		except:
			print("""An error occurred at stdin.
		 		Please enter an argument as standard input to make sure you apply a refresh rate of data coming in.
		 		===================================================================================================
		 		If you want a refresh rate of one day fill in D as stdin.

		 		If you want a refresh rate of one hour fill in H as stdin.

				If you want a refresh rate of one minute fill in M as stdin,
		 		Or you could just use an integer to specify the amount of seconds you want it to be refreshed.""")

if __name__ == "__main__":
	main()
	


