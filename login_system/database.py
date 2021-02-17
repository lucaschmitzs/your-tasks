# Connection with the database.
# For this WebApp/API we choose MongoDB

import pymongo

client = pymongo.MongoClient('mongodb://mongodb:27017/')
db = client.login_system
