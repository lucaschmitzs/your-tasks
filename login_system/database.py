# Connection with the database.
# For this WebApp/API we choose MongoDB

import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.your_tasks
