# _*_ coding: utf-8 _*_
# @Time     : 10:53
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import SiteOptions, SiteInformations, SiteContact, Message, PromoSection, PresentationSection
from .models import HeroSection, ArticlesSection, EventsSection, ContactSection


class SiteOptionsAdmin(object):
    list_diplay = ['carousel_auto_scroll', 'carousel_auto_scroll_speed']


class SiteInformationsAdmin(object):
    list_display = ['name', 'name_add', 'oppening', 'adress', 'city', 'post_code', 'phone', 'mail']


class SiteContactAdmin(object):
    list_display = ['facebook', 'tripadvisor', 'google', 'twitter', 'instagram', 'linkedin', 'snapchat']


class MessageAdmin(object):
    list_display = ['name', 'email', 'message', 'date', 'is_new']


class PromoSectionAdmin(object):
    list_display = ['name', 'title', 'text', 'label']


class PresentationSectionAdmin(object):
    list_display = ['name', 'title', 'sub_title', 'text1', 'text2']


class HeroSectionAdmin(object):
    list_display = ['name', 'icon1', 'icon2', 'icon3', 'title1', 'title2', 'title3', 'text1', 'text2', 'text3']


class ArticlesSectionAdmin(object):
    list_display = ['name', 'header', 'title', 'sub_title']


class EventsSectionAdmin(object):
    list_display = ['name', 'header', 'title', 'sub_title']


class ContactSectionAdmin(object):
    list_display = ['name', 'header', 'title', 'sub_title', 'sub_title2', 'sub_title3']


xadmin.site.register(SiteOptions, SiteOptionsAdmin)
xadmin.site.register(SiteInformations, SiteInformationsAdmin)
xadmin.site.register(SiteContact, SiteContactAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(PromoSection, PromoSectionAdmin)
xadmin.site.register(HeroSection, HeroSectionAdmin)
xadmin.site.register(ArticlesSection, ArticlesSectionAdmin)
xadmin.site.register(EventsSection, EventsSectionAdmin)
xadmin.site.register(ContactSection, ContactSectionAdmin)