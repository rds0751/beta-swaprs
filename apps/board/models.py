from django.db import models
from django.db.models import Q
from django.urls import reverse

from django_extensions.db.models import (ActivatorModel,
                                         TimeStampedModel)
from tagulous.models import TagField

from apps.core.models import (RandomSlugModel,
                                     UserProfile)


class PostManager(models.Manager):
    def search(self, **kwargs):
        qs = super().get_queryset()

        # TODO:
        # Split query into words, case insensitive search each field:
        # owner name, title, body, tags, location

        if 'query' in kwargs:
            query = kwargs['query']
            qs = qs.filter(Q(title__icontains=query) | Q(body__icontains=query))

        if 'tags' in kwargs:
            tags = kwargs['tags']
            # Filter to posts with tags in the provided set
            qs = qs.filter(tags__name__in=tags)

        return qs


# Posts submitted by users on the site.
class Post(RandomSlugModel, TimeStampedModel):
    # todo: custom queryset to get active posts
    objects = PostManager()

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # todo: Remove activatormodel?
    image1 = models.FileField(upload_to='products/', blank=True, null=True)
    image2 = models.FileField(upload_to='products/', blank=True, null=True)
    image3 = models.FileField(upload_to='products/', blank=True, null=True)
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=5000)

    # TODO: Use autocomplete_initial=True and specify preset tags?
    unit_type = models.CharField(max_length=80,blank=True, null=True)
    location = models.CharField(max_length=80,blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # location = models.CharField(max_length=5)

    def get_absolute_url(self):
        return reverse('board:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=80)