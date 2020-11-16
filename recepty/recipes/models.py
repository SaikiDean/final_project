from django.db import models
from django.utils import timezone


# Create your models here.
class Recipe(models.Model):
    Recipe_Author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Recipe_Title = models.CharField(max_length=60)
    Recipe_Ingredients = models.TextField()
    Recipe_Description = models.TextField()
    Recipe_Info = models.TextField()
    Recipe_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Recipe_Title
