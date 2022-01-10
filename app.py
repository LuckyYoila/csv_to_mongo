import csv
from pymongo import MongoClient

# connect to the database
db = MongoClient("localhost", 27017)
cluster = db["csv_to_mongo"]
dataCollection = cluster["data"]

i = 0

# open file in read mode
with open("test.csv", "r") as file:

	document = csv.DictReader(file)

	for row in document:

		# add a custom id to each data to insert
		person = {
			"_id" : i+1,
			"name": row['Name'],
			"surname": row['Surname'],
			"age": row['Age']
		}

		dataCollection.insert_one(person)
		i = i+1