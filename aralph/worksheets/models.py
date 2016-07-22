from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Asset(models.Model):
	
	LESSON = 1
	WORKSHEET = 2
	GUIDE = 3
	
	ASSET_TYPES = (
        (LESSON, 'Lesson'),
        (WORKSHEET, 'Worksheet'),
        (GUIDE, 'Guide'),
    )
	
	SCIENCE = 1
	MATH = 2
	LANGUAGE = 3
	READING = 4
	FILIPINO = 5
	ARALING_PANLIPUNAN = 6
	
	SUBJECTS = (
        (SCIENCE, 'Science'),
        (MATH, 'Math'),
        (LANGUAGE, 'Language'),
        (READING, 'Reading'),
        (FILIPINO, 'Filipino'),
        (ARALING_PANLIPUNAN, 'Araling Panlipunan'),
    )
	
	
	title = models.CharField(
        max_length=100,
        )
	
	description = models.CharField(
        max_length=254,
        )
	
	link = models.SlugField(
        max_length=50,
        unique=True,
        )
	
	type = models.IntegerField(
        choices=ASSET_TYPES,
        default=LESSON,
        )
	
	level = models.IntegerField(
		default=0,
		)
	
	subject = models.IntegerField(
		choices=SUBJECTS,
		default=SCIENCE,
		)
	
	thumbnail = models.ImageField()
	
	created = models.DateTimeField(auto_now_add=True)
	
	updated = models.DateTimeField(auto_now=True)
	
	hits = models.IntegerField(
		default=0,
		)