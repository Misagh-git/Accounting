# Generated by Django 4.0.5 on 2022-06-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_name', models.CharField(max_length=30)),
                ('inventory_location', models.CharField(max_length=100)),
                ('inventory_Description', models.TextField()),
            ],
        ),
    ]