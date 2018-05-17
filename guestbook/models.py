from django.db import models

from django.utils import timezone

class Comment(models.Model):
	name = models.CharField(max_length=20)
	comment = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)

class HighSchool(models.Model):
	name = models.CharField(max_length=40)
	address = models.CharField(max_length=40)
	zip_code = models.IntegerField()
	state = models.CharField(max_length=2)
	total_students = models.IntegerField()
	white_students = models.IntegerField()
	black_students = models.IntegerField()
	hispanic_students = models.IntegerField()
	asian_students = models.IntegerField()
	american_indian_students = models.IntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()

class College(models.Model):
	name = models.CharField(max_length=40)	
	conference = models.CharField(max_length=20)
	city = models.CharField(max_length=40)
#	zip_code = models.IntegerField(max_length=9)
	state = models.CharField(max_length=2)
	latitude = models.FloatField()
	longitude = models.FloatField()
	stadium_year_construction = models.IntegerField()
	stadium_capacity = models.IntegerField()
#	fbs = models.BooleanField() 

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)	

class Player(models.Model):
	fname = models.CharField(max_length=40)
	lname = models.CharField(max_length=40)
	prefix = models.CharField(max_length=5)
	suffix = models.CharField(max_length=5)
	position = models.CharField(max_length=10)
	secondary_position = models.CharField(max_length=10)
	forty_dash = models.FloatField()
	height = models.FloatField()
	weight = models.FloatField()
	twitter_handle = models.CharField(max_length=40)
	recruit_year = models.IntegerField()
	committed = models.BooleanField()
	high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE)

class Offer(models.Model):
	offer_date = models.DateField()
	scholarship_offer = models.BooleanField()
	active =  models.BooleanField()
	college_offering = models.ForeignKey(College, on_delete=models.CASCADE)