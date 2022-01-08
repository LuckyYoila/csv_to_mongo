import csv
from pymongo import MongoClient

# connect to the database
db = MongoClient("localhost", 27017)
cluster = db["csv_to_mongo"]
dataCollection = cluster["data"]


# set counter
i = 0
with open("test.csv", "r") as file:

	# to read csv file as a dictionary
	doc = csv.DictReader(file)

	for row in doc:
		print(f"{row['Surname']}, {row['Name'], }")

		# add a custom id to each data to insert
		person = {
			"_id" : i+1,
			"name": row['Name'],
			"surname": row['Surname'],
			"age": row['Age']
		}
		
		i = i+1
		dataCollection.insert_one(person)
