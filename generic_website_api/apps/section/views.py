from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from gallery.models import Gallery
from .serializers import SectionSerializer
from .models import Section


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        name = ''.join([i.capitalize() for i in request.data['title'].split()])
        gallery = Gallery.objects.get(slug=instance.slug.capitalize())
        print('------------gallery', gallery)
        gallery.name = name
        gallery.slug = name
        gallery.save()
        request.data['name'] = name
        request.data['slug'] = name
        return super().update(request, *args, **kwargs)