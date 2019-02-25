# _*_ coding: utf-8 _*_
# @Time     : 8:58
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from xadmin import views

from .models import Category, Article


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "Amir"
    site_footer = "http://www.cnblogs.com/derek1184405959/"
    # 菜单收缩
    menu_style = "accordion"


class CategoryAdmin(object):
    list_display = ['slug', 'name', 'description', 'position']


class ArticleAdmin(object):
    list_display = ['name', 'price', 'description', 'category', 'image', 'position', 'date']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
