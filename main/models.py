from django.db import models

# Create your models here.


class Proizvod_bezIndeksa(models.Model):
    naziv = models.CharField(max_length=200)
    naziv_random = models.CharField(max_length=200, default="Name")
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    cijena_random = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_SIndeksom(models.Model):
    naziv = models.CharField(max_length=200)
    naziv_random = models.CharField(max_length=200, default="Name")
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    cijena_random = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena', 'datum_kreiranja'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_DioIndeksa(models.Model):
    naziv = models.CharField(max_length=200)
    naziv_random = models.CharField(max_length=200, default="Name")
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    cijena_random = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_KriviIndeks(models.Model):
    naziv = models.CharField(max_length=200)
    naziv_random = models.CharField(max_length=200, default="Name")
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    cijena_random = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['datum_kreiranja', 'naziv', 'cijena'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"