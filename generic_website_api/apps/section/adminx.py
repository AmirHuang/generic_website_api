# _*_ coding: utf-8 _*_
# @Time     : 11:09
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Section


class SectionAdmin(object):
    list_display = ['slug', 'name', 'title', 'sub_title', 'text1', 'text2', 'gallery']


xadmin.site.register(Section, SectionAdmin)
