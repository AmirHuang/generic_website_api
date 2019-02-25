# _*_ coding: utf-8 _*_
# @Time     : 15:12
# @Author   : Amir
# @Site     : 
# @File     : signals.py
# @Software : PyCharm

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category, Article


@receiver(post_save, sender=Article)
def set_item_position(sender, instance=None, created=False, **kwargs):
    if created:
        count = Category.objects.get(name=instance.category.name).articles.all().count()
        instance.position = count

