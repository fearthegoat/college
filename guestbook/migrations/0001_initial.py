# Generated by Django 2.0.5 on 2018-06-05 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('conference', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=2)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('stadium_year_construction', models.IntegerField()),
                ('stadium_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('NCES_ID', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_date', models.DateField()),
                ('scholarship_offer', models.BooleanField()),
                ('active', models.BooleanField()),
                ('college_offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestbook.College')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('prospect_id', models.IntegerField()),
                ('position', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=2)),
                ('rivals_rating', models.FloatField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('recruit_year', models.IntegerField()),
                ('committed', models.BooleanField(default=False)),
                ('scraped', models.BooleanField(default=False)),
                ('high_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestbook.HighSchool')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestbook.College')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
