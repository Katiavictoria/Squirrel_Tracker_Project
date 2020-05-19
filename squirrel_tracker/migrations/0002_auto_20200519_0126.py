# Generated by Django 3.0.6 on 2020-05-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Other_Activities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Primary_Fur_Color',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Shift',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Specific_Location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Unique_Squirrel_ID',
            field=models.CharField(max_length=50),
        ),
    ]