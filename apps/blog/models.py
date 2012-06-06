import datetime
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User)
    tags = TaggableManager()
    pic = models.URLField(max_length=300, blank=True)

    def __unicode__(self):
        return self.title
