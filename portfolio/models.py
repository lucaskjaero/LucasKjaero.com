from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    completed_on = models.DateField(auto_now_add=True, editable=True)
    image = models.CharField(max_length=300, blank=True)
    source_available = models.BooleanField(default=True)

    download_link = models.CharField(max_length=300, blank=True)
    repository_link = models.CharField(max_length=300, blank=True)
    view_link = models.CharField(max_length=300, blank=True)

    technologies = models.ManyToManyField(Technology)
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.name
