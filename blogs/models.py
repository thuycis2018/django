from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title