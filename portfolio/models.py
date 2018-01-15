from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    description = models.TextField()
    what_i_learned = models.TextField(blank=True)

    difficulty = models.IntegerField()
    visible = models.BooleanField(default=True)
    finished = models.BooleanField(default=True)

    source_open = models.BooleanField(default=True)
    source_available = models.BooleanField(default=True)
    product_visible = models.BooleanField(default=False)

    view_link = models.CharField(max_length=300, blank=True)

    technologies = models.ManyToManyField(Technology)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
