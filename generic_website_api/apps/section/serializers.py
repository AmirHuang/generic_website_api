# _*_ coding: utf-8 _*_
# @Time     : 10:47
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers

from .models import Section, Gallery


class SectionSerializer(serializers.ModelSerializer):
    gallery = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    def create(self, validated_data):
        gallery = Gallery.objects.create(
            slug=validated_data['slug'].capitalize(),
            name=validated_data['name'].capitalize(),
            description='',
            limit=1
        )
        validated_data['gallery'] = gallery
        gallery.set_placeholder()
        return super().create(validated_data)

    class Meta:
        model = Section
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = '__all__'
