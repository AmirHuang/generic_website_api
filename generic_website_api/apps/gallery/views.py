import os, shutil
from pathlib import Path

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from .models import Gallery, Image
from .serializers import ImageSerializer, GallerySerializer

static = settings.STATIC_ROOT
media = settings.MEDIA_ROOT


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['post'], detail=False)
    def get_placeholder(self, request, pk=None):
        gallery = Gallery.objects.get(name=request.data['gallery'])
        return Response(ImageSerializer(gallery.set_placeholder()).data)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
