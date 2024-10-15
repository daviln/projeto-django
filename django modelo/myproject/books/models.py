from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(6)], default=0) #Rating from 0 to 5

    def __str__(self):
        return self.title
    
    def get_stars(self):
        return '⭐' * self.rating
    
