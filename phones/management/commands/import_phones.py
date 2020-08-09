import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                phone_data = Phone()
                phone_data.name = line[1]
                phone_data.image = line[2]
                phone_data.price = line[3]
                phone_data.release_date = line[4]
                phone_data.lte_exists = line[5]
                phone_data.slug = slugify(line[1])
                phone_data.save()
        return phone_data
