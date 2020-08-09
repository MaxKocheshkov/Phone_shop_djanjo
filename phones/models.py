from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='img')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, blank=True, allow_unicode=True)

    class Meta:
        db_table = 'phones'
