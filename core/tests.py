from django.test import TestCase
import subprocess
from .models import Video
import os
from django.core.files import File
class ffmpegTest(TestCase):

    def test_ffmpeg_cmd(self):
        cmd = subprocess.call(["ffmpeg"] , shell=True)
        result =  subprocess.call("echo $?" , shell=True)
        self.assertEqual(result , 0 )

    def test_redis_available(self):
        cmd = subprocess.check_output("redis-cli ping" , shell=True)
        self.assertEqual(cmd , b'PONG\n')
       
    def test_video_compression(self):
        with open('./media/changed/240/test.mp4' , "rb") as f:
            v = Video(video =  File(f))
            v.save()
            
        self.assertTrue(v.video_360)
        self.assertTrue(v.video_240)