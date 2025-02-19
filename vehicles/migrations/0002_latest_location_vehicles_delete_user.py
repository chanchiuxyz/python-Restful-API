# Generated by Django 5.0.3 on 2024-03-09 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='latest_location',
            fields=[
                ('vehicle_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('couse', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('altitude', models.IntegerField()),
                ('create_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=30)),
                ('body_type', models.CharField(max_length=30)),
                ('engine', models.CharField(max_length=10)),
                ('passengers', models.IntegerField()),
                ('doors', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
