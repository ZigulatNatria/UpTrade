from django.db import models

# Create your models here.
from django.urls import reverse


class MenuName(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_id': self.pk})