# Generated by Django 4.2.7 on 2024-01-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='availabletime',
        ),
        migrations.AddField(
            model_name='doctor',
            name='availabletime',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
