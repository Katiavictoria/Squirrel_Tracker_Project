# Generated by Django 3.0.6 on 2020-05-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(null=True)),
                ('Longitude', models.FloatField(null=True)),
                ('Unique_Squirrel_ID', models.CharField(max_length=100)),
                ('Shift', models.CharField(max_length=20)),
                ('Date', models.DateField(null=True)),
                ('Age', models.CharField(max_length=20)),
                ('Primary_Fur_Color', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('Specific_Location', models.CharField(max_length=200)),
                ('Running', models.BooleanField(null=True)),
                ('Chasing', models.BooleanField(null=True)),
                ('Climbing', models.BooleanField(null=True)),
                ('Eating', models.BooleanField(null=True)),
                ('Foraging', models.BooleanField(null=True)),
                ('Other_Activities', models.CharField(max_length=200)),
                ('Kuks', models.BooleanField(null=True)),
                ('Quaas', models.BooleanField(null=True)),
                ('Moans', models.BooleanField(null=True)),
                ('Tail_Flags', models.BooleanField(null=True)),
                ('Tail_Twitches', models.BooleanField(null=True)),
                ('Approaches', models.BooleanField(null=True)),
                ('Indifferent', models.BooleanField(null=True)),
                ('Runs_From', models.BooleanField(null=True)),
            ],
        ),
    ]
