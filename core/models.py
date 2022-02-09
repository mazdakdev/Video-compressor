from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Video(models.Model):
    video = models.FileField(upload_to="Videos/original/%Y/%m/%d")
    video_240 = models.FileField(upload_to="Videos/240p/%Y/%m/%d" , blank=True , null=True)
    video_360 = models.FileField(upload_to="Videos/360p/%Y/%m/%d" , blank=True , null=True)
    time = models.PositiveBigIntegerField(blank=True , null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    