# Generated by Django 3.1.3 on 2020-11-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwierkacz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
