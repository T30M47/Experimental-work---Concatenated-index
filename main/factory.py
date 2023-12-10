## factories.py
import factory
import factory.fuzzy
import random
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory

class ProizvodFactory(DjangoModelFactory):
    class Meta:
        abstract = True
    
    naziv = factory.Iterator(["bread", "eggs", "milk"])
    naziv_random = factory.Faker("word")
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Iterator([1.99, 9.99, 2.99])
    cijena_random = factory.Faker("pydecimal", left_digits=random.choice([1, 2, 3]), right_digits=2, positive = True)
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_BezIndeksaFactory(ProizvodFactory):
    class Meta:
        model = Proizvod_bezIndeksa

class Proizvod_SIndeksomFactory(ProizvodFactory):
    class Meta:
        model = Proizvod_SIndeksom

class Proizvod_DioIndeksaFactory(ProizvodFactory):
    class Meta:
        model = Proizvod_DioIndeksa

class Proizvod_KriviIndeksFactory(ProizvodFactory):
    class Meta:
        model = Proizvod_KriviIndeks
