from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField()

    def __unicode__(self):
        return self.title
