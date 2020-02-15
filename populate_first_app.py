#!/usr/bin/env python3

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
import sys

from faker import Faker
from pathlib import Path

from first_app.models import AccessRecord, Topic, Webpage


fakegen = Faker()
topics = ['Search', 'Social', 'Retail', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(name = random_topic())[0]
    t.save()
    return t

def random_topic():
    return random.choice(topics)

def populate(quantity = 5):
    for entry in range(quantity):
        topic = add_topic()
        url = fakegen.url()
        date = fakegen.date()
        company = fakegen.company()

        webpage = Webpage.objects.get_or_create(
            topic = topic,
            url = url,
            name = company,
        )[0]

        acc_rec = AccessRecord.objects.get_or_create(
            name = webpage,
            date = date,
        )[0]

if __name__ == '__main__':
    quantity = int(sys.argv[1])
    if quantity < 0:
        raise ValueError('Cannot populate a negative number of entries.')

    print(f'Populating first_app database with {quantity} entries.')
    populate(quantity)
    print('Finished populating the database.')
