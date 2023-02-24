import os
from deta import Deta 
from dotenv import load_dotenv
load_dotenv(".env")
DETA_KEY = "d0uykfhmbwh_bA8MJRAaQNc94fALykvCe7Mqm57ZTHD2" 
deta = Deta(DETA_KEY)
db = deta.Base("users_db")
def insert_user(username, name, password):
	return db.put({"key": username, "name":name, "password": password})

insert_user("Rishwin", "rishwin r kanth", "rishwin123")

def fetch_all_users():
	res = db.fetch()
	return res.items

print(fetch_all_users())


