# Generated by Django 4.1.1 on 2022-10-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Telefon'),
        ),
    ]