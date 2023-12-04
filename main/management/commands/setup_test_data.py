import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Proizvod_bezIndeksa, Proizvod_SIndeksom, Proizvod_KriviIndeks, Proizvod_DioIndeksa
from main.factory import *

NUM_PROIZVODBEZINDEKSA = 10000
NUM_PROIZVODSINDEKSOM = 10000
NUM_PROIZVODDIOINDEKSA = 10000
NUM_PROIZVODKRIVIINDEKS = 10000

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Proizvod_bezIndeksa, Proizvod_SIndeksom, Proizvod_KriviIndeks, Proizvod_DioIndeksa]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PROIZVODBEZINDEKSA):
            proizvod_bezIndeksa = Proizvod_BezIndeksaFactory()

        for _ in range(NUM_PROIZVODSINDEKSOM):
            proizvod_sIndeksom = Proizvod_SIndeksomFactory()

        for _ in range(NUM_PROIZVODDIOINDEKSA):
            proizvod_DioIndeksa = Proizvod_DioIndeksaFactory()

        for _ in range(NUM_PROIZVODKRIVIINDEKS):
            proizvod_KriviIndeks = Proizvod_KriviIndeksFactory()