from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
from .tasks import VideoUploaded


@receiver(post_save, sender=Video)
def transcode_video(sender,instance, **kwargs):
    if instance.is_done == False :
        VideoUploaded.delay(instance.id)