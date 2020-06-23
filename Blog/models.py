from django.db import models

# Create your models here.

class BlogInformation(models.Model):
    Title = models.CharField(max_length=200)
    Description= models.TextField(max_length=500)
    BlogDate = models.DateField()

    def __str__(self):
        return self.Title