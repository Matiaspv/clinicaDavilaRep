# Generated by Django 3.0.2 on 2020-01-23 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['nombre', 'apellido']},
        ),
    ]
