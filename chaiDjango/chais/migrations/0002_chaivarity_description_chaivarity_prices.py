# Generated by Django 5.1.4 on 2025-01-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chaivarity',
            name='prices',
            field=models.IntegerField(default=10),
        ),
    ]
