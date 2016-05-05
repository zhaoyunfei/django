from __future__ import unicode_literals

from django.db import models

# # Create your models here.
# class Mysite(models.Model):
#     title=models.CharField(max_length=100)
#     url=models.URLField()
#     author=models.CharField(max_length=100)
#     num=models.IntegerField()
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         ordering=['num']

class Author(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    counter=models.IntegerField(default=0)
    pubDate=models.DateField(auto_now_add=True)
    author=models.ForeignKey(Author)

    def __unicode__(self):
        return self.title


class User(models.Model):
    name=models.CharField(max_length=20)
    headImg=models.FileField(upload_to='upload/')

    def __unicode__(self):
        return self.name