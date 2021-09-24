# Generated by Django 3.2.7 on 2021-09-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=90)),
                ('precio', models.CharField(max_length=85)),
                ('iva', models.CharField(max_length=90)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('tipo', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
    ]
