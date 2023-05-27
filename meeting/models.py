from django.db import models
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=20, db_index=True, unique=True, null=True)
    flag_pic = models.ImageField(upload_to='flag_pic/')

    class Meta:
        ordering = ['name', ]

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/%d/')
    time = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=100)
    location_link = models.CharField(max_length=1000)
    contacts = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return self.title




























# class Schedule(models.Model):
#     WEEKDAYS = (
#         ('Mon', 'Monday'),
#         ('Tu', 'Tuesday'),
#         ('Wed', 'Wednesday'),
#         ('Th', 'Thursday'),
#         ('Fri', 'Friday'),
#         ('Sat', 'Saturday'),
#         ('Sun', 'Sunday')
#     )

# LANGUAGES_DICT = {
#         ('en', 'English'),
#         ('pl', 'Polish'),
#         ('fr', 'French'),
#         ('de', 'German'),
#         ('it', 'Italian'),
#         ('es', 'Spanish'),
#     }
#     name = models.CharField(max_length=2, choices=LANGUAGES_DICT)
