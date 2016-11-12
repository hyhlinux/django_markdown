from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=60)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
