# Generated by Django 2.1.2 on 2018-11-20 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0012_file_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
