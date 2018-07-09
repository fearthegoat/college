import csv
from guestbook.models import College 
#import os
#path =  "C:\\...." # Set path of new directory here
#os.chdir(path) # changes the directory

# imports Colleges




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

# Imports Players and High School
import glob
import csv
from guestbook.models import Player, HighSchool

bio_files = glob.glob('myproject/static/scraper/bio*')
for bio in bio_files:
	with open(bio , 'r', encoding='ascii', errors='ignore') as csvfile:
		players = csv.DictReader(csvfile)
		for player in players:
			new_player = Player(
				recruit_year=player['Year'], 
				name=player['Name'], 		
				position=player['Pos'],
				city=player['City'],
				state=player['State'],
				prospect_id=player['ProspectID'],
				scraped=True				
				)
			new_player.rivals_rating=player['RR'] if player['RR'] != '' else 1.0
			new_player.height=player['HT'] if player['HT'] != '' else 1.0
			new_player.weight=player['WT'] if player['WT'] != '' else 1.0
			new_player.committed=True if player['School'] != '' else False
			high_school = HighSchool.objects.filter(NCES_ID=player['NCES_ID'])[0] if HighSchool.objects.filter(NCES_ID=player['NCES_ID']).exists() else False
			if high_school:
				new_player.high_school=high_school
			else:
				high_school = HighSchool.objects.filter(name=player['high_school'], city=player['City'], state=player['State'])[0] if HighSchool.objects.filter(name=player['high_school'], city=player['City'], state=player['State']).exists() else False
				if high_school:
					new_player.high_school=high_school
				else:
					high_school = HighSchool(name=player['high_school'], city=player['City'], state=player['State'], NCES_ID=player['NCES_ID'])
					high_school.save()
					new_player.high_school=high_school
			new_player.save()

import glob
import csv
from guestbook.models import Player, HighSchool

offer_files = glob.glob('myproject/static/scraper/player*')


