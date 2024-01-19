import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from databaseUrl import url

cred = credentials.Certificate("credentials.json")

firebase_admin.initialize_app(cred, url)

Username = db.reference('/UserName').get()
Password = db.reference('/Password').get()

# print(Username, Password)
