from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Video(models.Model):
    
    video = models.FileField(upload_to="Videos/original/%Y/%m/%d")
    video_240 = models.FileField(upload_to="Videos/240p/%Y/%m/%d")
    video_360 = models.FileField(upload_to="Videos/360p/%Y/%m/%d")

    percent = models.PositiveIntegerField(
           validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Functions to calculate the progress
    
    def update_progress(self, percent, commit=True):
        if 0 > percent > 100:
            raise ValueError("Invalid percent value.")

        self.progress = percent
        if commit:
            self.save()

    def reset_progress(self, commit=True):
        self.percent = 0
        if commit:
            self.save()




    