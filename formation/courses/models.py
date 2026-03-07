from django.db import models
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self)->str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"pk": self.pk})
    
class language(models.Model):
    name=models.CharField(max_length=20)


class Framework(models.Model):
    name=models.CharField(max_length=20)
    language=models.ForeignKey(language, on_delete=models.CASCADE)


"""
CASCADE:lorsqu'on supprime le language la classe framework ne sert plus a rien
PROTECT:le contraire lorqu'on supprime la classe language la classe framework fonctionne
SET_NULL: lorsque je supprime la classe language, dans la classe framework je met NULL au niveau du langage
SET_DEFAULT: on donne une valeur par defaut apres supression
DO_NOTHING:lorsque je supprime je laisse la table comme elle est
"""