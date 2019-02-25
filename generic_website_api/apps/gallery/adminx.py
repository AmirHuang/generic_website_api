# _*_ coding: utf-8 _*_
# @Time     : 10:41
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin

from .models import Gallery, Image


class GalleryAdmin(object):
    list_display = ['slug', 'name', 'description', 'limit']


class ImageAdmin(object):
    list_display = ['name', 'image', 'description', 'date', 'gallery', 'position']


xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Image, ImageAdmin)
