from typing import Any
from django.db import models
import random
import os

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


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    img = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def __unicode__(self):
        return self.title
