from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=350)
    image = models.ImageField(upload_to='images')
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Create your models here.
