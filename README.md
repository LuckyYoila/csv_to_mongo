# csv_to_mongo
Programatically push CSV data to MongoDB


## Install pymongo
    - install the pymongo module using **pip install pymongo**.

## Connect to the database
    - Create a database and a collection on MongoDB locally through **MongoDB Compass** or online through **MongoDB Atlas**.
    - Import MongoClient and connect to MongoDB using localhost port (local), or connection link (Atlas).
    - Connect to the database cluster and connection respectively.

## Read csv
    - Import csv module
    - Open the csv file in read mode and pass the file to the csv module.

## Coup de grace
    - Finally, loop through the rows of the file and insert the data to the database.