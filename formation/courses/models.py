from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    
class Language(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name=models.CharField(max_length=20)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
CASCADE:lorsqu'on supprime le language la classe framework ne sert plus a rien
PROTECT:le contraire lorqu'on supprime la classe language la classe framework fonctionne
SET_NULL: lorsque je supprime la classe language, dans la classe framework je met NULL au niveau du langage
SET_DEFAULT: on donne une valeur par defaut apres supression
DO_NOTHING:lorsque je supprime je laisse la table comme elle est
"""

class School(models.Model):
    name=models.CharField(max_length=100)


class Student(models.Model):
    name=models.CharField(max_length=30)
    school=models.ManyToManyField(School)

class Profile(models.Model):
    school=models.CharField(max_length=30)
    user=models.OneToOneField(User, on_delete=models.CASCADE)