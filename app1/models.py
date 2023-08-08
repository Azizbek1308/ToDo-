from django.db import models

# Create your models here.
class Smartphone(models.Model):
    model = models.CharField(max_length=30, blank=True)
    year = models.DateField()
    cost = models.IntegerField()
    status = models.TextField()
    def __str__(self):
        return self.model