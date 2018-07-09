from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Comment(models.Model):
	name = models.CharField(max_length=20)
	comment = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)

class HighSchool(models.Model):
	name = models.CharField(max_length=40)
	NCES_ID = models.CharField(max_length=20)
	state = models.CharField(max_length=2)
	city = models.CharField(max_length=40)
	# address = models.CharField(max_length=40)
	# zip_code = models.IntegerField()
	# total_students = models.IntegerField()
	# white_students = models.IntegerField()
	# black_students = models.IntegerField()
	# hispanic_students = models.IntegerField()
	# asian_students = models.IntegerField()
	# american_indian_students = models.IntegerField()
	# latitude = models.FloatField()
	# longitude = models.FloatField()
	def __str__(self):
		return '<Name: {}, State: {}>'.format(self.name, self.state)

class College(models.Model):
	name = models.CharField(max_length=40)	
	conference = models.CharField(max_length=20)
	city = models.CharField(max_length=40)
	state = models.CharField(max_length=2)
	latitude = models.FloatField()
	longitude = models.FloatField()
	stadium_year_construction = models.IntegerField()
	stadium_capacity = models.IntegerField()
#	zip_code = models.IntegerField(max_length=9)
#	fbs = models.BooleanField() 

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)	

class Player(models.Model):
	name = models.CharField(max_length=60)
	prospect_id = models.IntegerField()
	position = models.CharField(max_length=10)
	city = models.CharField(max_length=40)
	state = models.CharField(max_length=2)
	rivals_rating = models.FloatField()
	height = models.FloatField()
	weight = models.FloatField()
	date_added = models.DateTimeField(default=timezone.now)
	recruit_year = models.IntegerField()
	committed = models.BooleanField(default=False)
	scraped =models.BooleanField(default=False)
	high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
	# secondary_position = models.CharField(max_length=10)
	# forty_dash = models.FloatField()
	# twitter_handle = models.CharField(max_length=40)
	# committed_school = models.ForeignKey(College, on_delete=models.CASCADE)
	# fname = models.CharField(max_length=40)
	# lname = models.CharField(max_length=40)
	# prefix = models.CharField(max_length=5)
	# suffix = models.CharField(max_length=5)
	def __str__(self):
		return '<Name: {}, Position: {}, State: {}>'.format(self.name, self.position, self.state)

class Offer(models.Model):
	offer_date = models.DateField()
	scholarship_offer = models.BooleanField()
	active =  models.BooleanField()
	college_offering = models.ForeignKey(College, on_delete=models.CASCADE)
	player_offered = models.ForeignKey(Player, on_delete=models.CASCADE)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	college = models.ForeignKey(College, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
