# Generated by Django 4.0.3 on 2022-04-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_alter_first_admission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='admission_date',
            field=models.DateField(null=True),
        ),
    ]
