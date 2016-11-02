'''
author : Kennedy kolute
class  : Andela bootcamp 11
'''
import requests
import json

def search(query):
    # the url below will get info from hipolabs api 
    url = 'http://universities.hipolabs.com/search?country='
	# transform string to url string
    country = query.replace(' ', '%20')
    final_url = url + country
    json_obj = requests.get(final_url)
    data = json_obj.json()
   # loop through items in data to print out the result
    for item in data:
        for uni in item:
        	print (uni , " : ", item[uni],)

search("kenya")
