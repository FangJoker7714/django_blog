# Generated by Django 2.1.5 on 2019-01-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.TextField(blank=True, max_length=4000),
        ),
    ]
