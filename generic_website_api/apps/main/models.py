import forgery_py
from random import randint

from django.db import models
from django.conf import settings


def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()


def words(n):
    w = forgery_py.lorem_ipsum.words(n).capitalize()
    return w if n <= 2 else w + '.'


class SiteOptions(models.Model):
    carousel_auto_scroll = models.BooleanField(default=False)
    carousel_auto_scroll_speed = models.IntegerField(default=5000, null=False)

    show_articles_price = models.BooleanField(default=True)


class SiteInformations(models.Model):
    name = models.CharField(max_length=25, null=False, default='')
    name_add = models.CharField(max_length=15, null=False, default='')
    oppening = models.CharField(max_length=4, null=False, default='')
    adress = models.CharField(max_length=30, null=False, default='')
    city = models.CharField(max_length=30, null=False, default='')
    post_code = models.CharField(max_length=8, null=False, default='')
    phone = models.CharField(max_length=30, null=True, default='', blank=True)
    mail = models.EmailField(max_length=30, null=True, default='', blank=True)


class SiteContact(models.Model):
    facebook = models.CharField(max_length=1000, null=True, default='', blank=True)
    tripadvisor = models.CharField(max_length=1000, null=True, default='', blank=True)
    google = models.CharField(max_length=1000, null=True, default='', blank=True)
    twitter = models.CharField(max_length=1000, null=True, default='', blank=True)
    instagram = models.CharField(max_length=1000, null=True, default='', blank=True)
    linkedin = models.CharField(max_length=1000, null=True, default='', blank=True)
    snapchat = models.CharField(max_length=1000, null=True, default='', blank=True)


class Message(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    message = models.TextField(max_length=3000, null=False)
    date = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']


class PromoSection(models.Model):
    name = models.CharField(default='Promo', max_length=15)
    title = models.CharField(max_length=35, null=False, default=sentences(1))
    text = models.CharField(max_length=800, null=False, default=sentences(4))
    label = models.CharField(max_length=18, default='Action spéciale !')


class PresentationSection(models.Model):
    name = models.CharField(default='Presentation', max_length=15)
    title = models.CharField(max_length=35, null=False, default=sentences(1))
    sub_title = models.TextField(max_length=200, null=False, default=sentences(randint(1, 3)))
    text1 = models.TextField(max_length=800, default=sentences(8))
    text2 = models.TextField(max_length=800, default=sentences(9))


class HeroSection(models.Model):
    name = models.CharField(default='Hero', max_length=15)
    icon1 = models.CharField(max_length=20, null=False, default="fab fa-cloudversify")
    icon2 = models.CharField(max_length=20, null=False, default="far fa-paint-brush")
    icon3 = models.CharField(max_length=20, null=False, default="far fa-compass")
    title1 = models.CharField(max_length=20, null=False, default=words(2))
    title2 = models.CharField(max_length=20, null=False, default=words(2))
    title3 = models.CharField(max_length=20, null=False, default=words(2))
    text1 = models.CharField(max_length=200, null=False, default=sentences(2))
    text2 = models.CharField(max_length=200, null=False, default=sentences(2))
    text3 = models.CharField(max_length=200, null=False, default=sentences(2))


class ArticlesSection(models.Model):
    name = models.CharField(default='Articles', max_length=15)
    header = models.CharField(max_length=30, null=False, default='Articles')
    title = models.CharField(max_length=35, null=False, default='Articles')
    sub_title = models.TextField(max_length=200, null=False, default=sentences(randint(1, 3)))


class EventsSection(models.Model):
    name = models.CharField(default='Events', max_length=15)
    header = models.CharField(max_length=30, null=False, default='Galerie')
    title = models.CharField(max_length=35, null=False, default='Derniers événements')
    sub_title = models.TextField(max_length=200, null=False, default=sentences(randint(1, 3)))


class ContactSection(models.Model):
    name = models.CharField(default='Contact', max_length=15)
    header = models.CharField(max_length=30, null=False, default='Contact')
    title = models.CharField(max_length=35, null=False, default='Où nous trouver')
    sub_title = models.TextField(max_length=200, null=False, default="N'hésitez pas à nous contacter...")
    sub_title2 = models.TextField(max_length=200, null=False, default='... en nous laissant un message...')
    sub_title3 = models.TextField(max_length=200, null=False, default='... ou en passant directement nous voir:')
