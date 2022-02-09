from celery import shared_task
from .models import Video
import subprocess
from django.core.files import File
import os
import uuid 
from datetime import datetime

URL_240 = "./media/changed/240/"
URL_360 = "./media/changed/360/"

@shared_task
def VideoUploaded(video_id):
    start_time = datetime.now()
    video = Video.objects.get(id=video_id)
    random_name = str(uuid.uuid4().hex[:6].upper())+".mp4"

    subprocess.call(["ffmpeg" ,"-i" , "media/"+str(video.video) , "-s" , "640x360", URL_240+random_name])
    subprocess.call(["ffmpeg" ,"-i" , "media/"+str(video.video) , "-s" , "426x240",URL_360+random_name])

    new_random_name = str(uuid.uuid4().hex[:6].upper())+".mp4"

    with open(URL_240+random_name , "rb") as f:
        video.video_240.save(new_random_name, File(f))

    with open(URL_360+random_name , "rb") as f:
        video.video_360.save(new_random_name, File(f))

    video.is_done = True
    end_time = datetime.now()
    video.time = (end_time-start_time).total_seconds()
    video.save()




    






