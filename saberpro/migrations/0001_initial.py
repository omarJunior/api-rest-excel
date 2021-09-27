# Generated by Django 3.2.7 on 2021-09-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaberPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=90)),
                ('apellidos', models.CharField(max_length=90)),
                ('genero', models.CharField(max_length=80)),
                ('ciudad', models.CharField(max_length=80)),
                ('matematicas', models.IntegerField()),
                ('lenguaje', models.IntegerField()),
                ('ciencias', models.IntegerField()),
                ('ingles', models.IntegerField()),
                ('ciudadanas', models.IntegerField()),
                ('fisca', models.IntegerField()),
            ],
            options={
                'db_table': 'saberpros',
            },
        ),
    ]