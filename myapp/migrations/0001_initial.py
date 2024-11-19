# Generated by Django 5.1.3 on 2024-11-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
