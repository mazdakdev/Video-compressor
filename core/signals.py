from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
from .tasks import VideoUploaded
from django.conf import settings


@receiver(post_save, sender=Video)
def transcode_video(sender,instance, **kwargs):
    if instance.is_done == False :
        if not settings.TESTING:
            VideoUploaded.delay(instance.id)
        if settings.TESTING:
            VideoUploaded(instance.id)
