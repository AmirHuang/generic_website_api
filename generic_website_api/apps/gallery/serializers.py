# _*_ coding: utf-8 _*_
# @Time     : 15:14
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm


from rest_framework import serializers
from .models import Gallery, Image
from articles.serializers import ArticleSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    gallery = serializers.SlugRelatedField(slug_field='slug', queryset=Gallery.objects.all())
    article = ArticleSerializer(many=False, read_only=True)

    class Meta:
        model = Image
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = "__all__"
