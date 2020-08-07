from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='img')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=False, null=True, blank=True, default='')

    class Meta:
        db_table = 'phones'


