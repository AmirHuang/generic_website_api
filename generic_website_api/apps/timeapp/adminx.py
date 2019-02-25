# _*_ coding: utf-8 _*_
# @Time     : 11:20
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Day, Slot


class DayAdmin(object):
    list_display = ['name', 'slug']


class SlotAdmin(object):
    list_display = ['start', 'end', 'day']


xadmin.site.register(Day, DayAdmin)
xadmin.site.register(Slot, SlotAdmin)
