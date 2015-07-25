import csv
import requests
import json


#Example Parsing JSON BACK

def read_csv_input(): 
	try:
		filename = raw_input("Please enter input file name you want parse json records ")
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
			   record = row['Records']
			   company = json.loads(record)
			   print company
	except Exception as e:
		print e
		print "File not found. Please check if file exists"

read_csv_input()