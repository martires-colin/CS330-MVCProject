from pymongo import MongoClient

# Connect to local MongoDB database
db_client = MongoClient('localhost', 27017)
db = db_client.boredapp
completed_activities = db.completed_activities