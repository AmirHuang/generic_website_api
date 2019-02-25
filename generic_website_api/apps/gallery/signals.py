# _*_ coding: utf-8 _*_
# @Time     : 15:56
# @Author   : Amir
# @Site     : 
# @File     : signals.py
# @Software : PyCharm

import os
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from .models import Image, Gallery


@receiver(post_save, sender=Image)
def set_position(sender, instance=None, created=False, **kwargs):
    if created:
        print('-----kwargs:', kwargs)
        g = Gallery.objects.get(name=instance.gallery.name)
        instance.position = g.images.all().count()


@receiver(pre_delete, sender=Image)
def delete_physical_image(sender, instance=None, created=False, **kwargs):
    try:
        os.remove(instance.image.path)
    except:
        pass
