from django.db import models

# Create your models here.

class MenuName(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)

    def __str__(self):
        return self.name