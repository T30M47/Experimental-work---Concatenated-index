# Generated by Django 4.2.7 on 2023-12-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_proizvod_bezindeksa_datum_azuriranja_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proizvod_bezindeksa',
            name='cijena_random',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='proizvod_bezindeksa',
            name='naziv_random',
            field=models.CharField(default='Name', max_length=200),
        ),
        migrations.AddField(
            model_name='proizvod_dioindeksa',
            name='cijena_random',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='proizvod_dioindeksa',
            name='naziv_random',
            field=models.CharField(default='Name', max_length=200),
        ),
        migrations.AddField(
            model_name='proizvod_kriviindeks',
            name='cijena_random',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='proizvod_kriviindeks',
            name='naziv_random',
            field=models.CharField(default='Name', max_length=200),
        ),
        migrations.AddField(
            model_name='proizvod_sindeksom',
            name='cijena_random',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='proizvod_sindeksom',
            name='naziv_random',
            field=models.CharField(default='Name', max_length=200),
        ),
    ]