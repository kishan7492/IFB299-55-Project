from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title

class Placeinformation(models.Model):
    placeID = models.AutoField
    Placename = models.CharField(max_length = 300, unique= True)
    address = models.CharField(max_length = 400)
    description = models.CharField(max_length = 400)
    long = models.CharField(max_length=15)
    lat = models.CharField(max_length=15)
    typeOfPlace = models.CharField(max_length=15)
    def __unicode__(self):
        return self.Placename



class users(models.Model):
    ID = models.AutoField
    Username = models.CharField(max_length = 400)
    Email = models.EmailField
    name = models.CharField(max_length=30)
    typwOfUser = models.CharField(max_length=15)
    PASSWO = models.CharField(max_length=9, null=False)
    def __unicode__(self):
        return self.Username

def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Placeinformation, self).save(*args, **kwargs)