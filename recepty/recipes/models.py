from django.db import models
from django.utils import timezone


class Categories(models.Model):
    CAT_NAME = ['Snídaně a svačiny', 'Obědy a večeře',
                'Saláty a přílohy', 'Zdravé dezerty',
                'Polévky', 'Vegetariánské', 'Veganské',
                'Bezlepkové', 'Bezlaktózové']
    cat_name = models.CharField(
        choices = CAT_NAME
    )


# Create your models here.
class Recipe(models.Model):
    #Recipe_Id =
    Recipe_Author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Recipe_Title = models.CharField(max_length=60)
    Recipe_Ingredients = models.TextField()
    Recipe_Description = models.TextField()
    Recipe_Info = models.TextField()
    Recipe_Img = models.ImageField(upload_to='../recepty/img')
    Recipe_Category = models.IntegerField
    Recipe_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Recipe_Title
        return self.cat_Name

 #class Calc(models.Model):
    #Height
    #Weight