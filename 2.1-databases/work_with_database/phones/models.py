from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=300)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")    
