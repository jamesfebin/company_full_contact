import csv
import requests
import json

#Please add your FULL CONTACT API KEY below
api_key = '15edc76d93d8d49e'
url='https://api.fullcontact.com/v2/company/lookup.json'

def append_to_file(filename,row):
    try:
        with open(filename, 'ab') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            writer.writerows(row)
    except Exception as e:
        print "Unable to write to file. Please check permissions"

def init_file_found():
    try:
        with open("found.csv", 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            writer.writerows([['Domain','Records']])
    except Exception as e:
        print "Unable to write to file. Please check permissions"

def init_file_not_found():
    try:
        with open("not_found.csv", 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            writer.writerows([['Domain']])
    except Exception as e:
        print "Unable to write to file. Please check permissions"

def fetch_from_full_contact(domain):
	try:
		kwargs = {}
		kwargs['apiKey'] = api_key
		kwargs['domain'] = domain
		r = requests.get(url, params=kwargs)
		r= json.loads(r.text)
		return r
	except Exception as e:
		print e



# Read the input file
def read_csv_input(): 
	try:
		filename = raw_input("Please enter input file name ")
		init_file_found()
		init_file_not_found()
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
			   domain = row['Domain']
			   if domain != '':
			   		r = fetch_from_full_contact(domain)
			   		if r and r['status'] == 200:
			   			append_to_file("found.csv",[[domain,str(r)]])
			   		else:
			   			append_to_file("not_found.csv",[[domain]])
		print ' Task Completed'
		print ' Your results are stored in found.csv and not_found.csv'
	except Exception as e:
		print e
		print "File not found. Please check if file exists"


#This is where it begins 
read_csv_input()
