# Generated by Django 4.0.3 on 2022-04-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_alter_eight_admission_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eight',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eight',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eight',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eight',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fifth',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fifth',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fifth',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fifth',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='first',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='first',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='first',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='first',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fourth',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fourth',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fourth',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fourth',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nineth',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nineth',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nineth',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nineth',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='second',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='second',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='second',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='second',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seventh',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seventh',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seventh',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seventh',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sixth',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sixth',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sixth',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sixth',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenth',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenth',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenth',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenth',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='third',
            name='birth_date',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='third',
            name='birth_place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='third',
            name='father_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='third',
            name='mother_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eight',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='eight',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='eight',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='eight',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='eight',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fifth',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fifth',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fifth',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fifth',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='fifth',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='first',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='first',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='first',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='first',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='first',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fourth',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fourth',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fourth',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='fourth',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='fourth',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='nineth',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='nineth',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='nineth',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='nineth',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='nineth',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='second',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='second',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='second',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='second',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='second',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='seventh',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='seventh',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='seventh',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='seventh',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='seventh',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='sixth',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='sixth',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='sixth',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='sixth',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='sixth',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='tenth',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='tenth',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='tenth',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='tenth',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='tenth',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='third',
            name='aadhar_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='third',
            name='master_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='third',
            name='register_no',
            field=models.CharField(max_length=27),
        ),
        migrations.AlterField(
            model_name='third',
            name='rollno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='third',
            name='udise_no',
            field=models.CharField(max_length=27),
        ),
    ]
