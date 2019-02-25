"""generic_website_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path, include, re_path
from django.views.static import serve
from generic_website_api.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from articles.views import CategoryViewSet, ArticleViewSet
from gallery.views import GalleryViewSet, ImageViewSet

from main.views import PresentationViewSet, HeroViewSet, ArticlesViewSet
from main.views import EventsViewSet, ContactViewSet, PromoViewSet, MessageViewSet
from main.views import SiteInformationsViewSet, SiteContactViewSet, SiteOptionsViewSet

from section.views import SectionViewSet

from timeapp.views import DayViewSet, SlotViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet, base_name='category')
router.register('article', ArticleViewSet, base_name='article')

router.register('images', ImageViewSet, base_name='images')
router.register('galleries', GalleryViewSet, base_name='galleries')

router.register('presentation', PresentationViewSet)
router.register('hero', HeroViewSet)
router.register('main_article', ArticlesViewSet)
router.register('events', EventsViewSet)
router.register('contact', ContactViewSet)
router.register('promo', PromoViewSet)
router.register('message', MessageViewSet)
router.register('siteInfo', SiteInformationsViewSet)
router.register('siteContact', SiteContactViewSet)
router.register('siteOptions', SiteOptionsViewSet)

router.register('sections', SectionViewSet)

router.register('day', DayViewSet)
router.register('slot', SlotViewSet)


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf 文档 title自定义
    path('docs', include_docs_urls(title='Amir')),

    # Api入口
    path('api-auth/', include('rest_framework.urls')),
    re_path('', include(router.urls)),
]
