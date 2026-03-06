from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Article(models.Model):
    title=models.CharField(max_length=50)
    images=models.ImageField(upload_to='blog',blank=True)
    description=models.TextField()
    slug=models.SlugField(null=True)


    def __str__(self) ->str:
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"pk": self.pk})
    