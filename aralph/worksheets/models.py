from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Material(models.Model):
	
	WORKSHEET = 1
	VIDEO = 2
	QUIZ = 3
	
	ASSET_TYPES = (
        (WORKSHEET, 'Worksheet'),
        (VIDEO, 'Video Tutorial'),
        (QUIZ, 'Quiz'),
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
	
	LEVELS = (
        (0, 'K'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    )
	
	
	title = models.CharField(
        max_length=100,
        )
	
	description = models.CharField(
        max_length=254,
        )
	
	link = models.SlugField(
        max_length=50,
        )
	
	type = models.IntegerField(
        choices=ASSET_TYPES,
        default=WORKSHEET,
        )
	
	level = models.IntegerField(
		choices=LEVELS,
		default=0,
		)
	
	subject = models.IntegerField(
		choices=SUBJECTS,
		default=SCIENCE,
		)
	
	thumbnail = models.ImageField(
		blank=True,
        null=True,
        default=None,
		)
	
	created = models.DateTimeField(
		auto_now_add=True
		)
	
	updated = models.DateTimeField(auto_now=True)
	
	hits = models.IntegerField(
		default=0,
		)