# Generated by Django 4.0.3 on 2022-04-23 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0009_alter_first_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='birth_date',
            field=models.CharField(max_length=17),
        ),
    ]
