import csv
from guestbook.models import College 
#import os
#path =  "C:\\...." # Set path of new directory here
#os.chdir(path) # changes the directory
with open('guestbook/static/guestbook/college_seed.csv') as csvfile:
	colleges = csv.DictReader(csvfile)
	for college in colleges:
		p = College(
			name=college['name'], 
			conference=college['conference'],
			stadium_capacity=college['stadium_capacity'],
			latitude=college['latitude'],
			longitude=college['longitude'],
			city=college['city'],
			state=college['state'],
			stadium_year_construction=college['stadium_construction']
			)
		p.save()