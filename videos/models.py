from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class videosModel(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	url = EmbedVideoField()