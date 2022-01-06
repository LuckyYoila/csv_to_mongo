import csv

with open("test.csv", "r") as file:

	# to read file as a dictionary
	doc = csv.DictReader(file)

	for row in doc:
		print(f"{row['Surname']}, {row['Name'], }")
