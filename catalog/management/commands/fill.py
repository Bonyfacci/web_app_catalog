import json

from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    filename = f'{BASE_DIR}\data.json'

    @staticmethod
    def read_json():
        with open(Command.filename, 'r', encoding='utf-8') as file:
            product_list = json.load(file)
        return product_list

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        product_for_create = []
        for product in Command.read_json():
            # Product.objects.create(name=product['fields']['name'],
            #                        description=product['fields']['description'],
            #                        category=Category.objects.get(pk=product['fields']['category']),
            #                        price=product['fields']['price'])
            product_for_create.append(
                Product(name=product['fields']['name'],
                                           description=product['fields']['description'],
                                           category=Category.objects.get(pk=product['fields']['category']),
                                           price=product['fields']['price'])
            )
        Product.objects.bulk_create(product_for_create)
