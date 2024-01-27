from typing import Any
from django.db import models
import random
import os
from django.db.models import Q

from django.db.models.query import QuerySet
from django.urls import reverse


# Create your models here.


def get_filename_ext(filename):
    baseName = os.path.basename(filename)
    name, ext = os.path.splitext(baseName)
    return name, ext


def upload_image_path(instance, fileName):
    newFileName = random.randint(1, 500000000)
    name, ext = get_filename_ext(fileName)
    finalFileName = '{newFileName}{ext}'.format(
        newFileName=newFileName, ext=ext)
    return "products/{newFileName}/{finalFileName}".format(newFileName=newFileName, finalFileName=finalFileName)


class ProductQuery(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        lookups = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tag__title__icontains=query)
        )
        # Q(tag__name__icontains = query)tshirt,t-shirt,t shirt
        return self.filter(lookups).distinct()



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuery(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    img = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()

    def get_absolute_url(self):
       # return "/products/{slug}/".format(slug=self.slug)
       return reverse("products:ProductSlug", kwargs={"slug": self.slug})


    def __str__(self) -> str:
        return self.title

    def __unicode__(self):
        return self.title
