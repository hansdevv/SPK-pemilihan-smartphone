import streamlit as st
from pymongo import MongoClient

class Smartphone:
	def __init__(self, uri, username, password):
			self.uri = uri
			self.username = username
			self.password = password
	def show(self):
		url = f"mongodb+srv://{self.username}:{self.password}@spk.rltinf1.mongodb.net/?retryWrites=true&w=majority"
		client = MongoClient(url)
		db = client['spkPemilihanSmartphone']
		collection = db['smartphone']
		data = collection.find()
		return data