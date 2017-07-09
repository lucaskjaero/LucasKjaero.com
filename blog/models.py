from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True, db_index=True)
    content = models.TextField()
    image = models.CharField(max_length=300,
                             default="/static/blog/images/default-post-bg.jpg")
    published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
