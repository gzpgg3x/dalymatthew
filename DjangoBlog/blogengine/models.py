# from django.db import models

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.DateTimeField()
#     text = models.TextField()
#     slug = models.SlugField(max_length=40, unique=True)

#     def __unicode__(self):
#         return self.title

#     def get_absolute_url(self):
#         return "%s/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.pub_date.day, self.slug)




from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)