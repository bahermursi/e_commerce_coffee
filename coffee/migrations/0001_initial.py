# Generated by Django 3.1.5 on 2021-02-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(blank=True, choices=[('COFFEE_MACHINE_LARGE', 'COFFEE_MACHINE_LARGE'), ('COFFEE_MACHINE_SMALL', 'COFFEE_MACHINE_SMALL'), ('ESPRESSO_MACHINE', 'ESPRESSO_MACHINE')], default='COFFEE_MACHINE_LARGE', max_length=100)),
                ('description', models.TextField(default='', max_length=254)),
                ('water_line_compatible', models.BooleanField(default=False)),
                ('code', models.TextField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(blank=True, choices=[('COFFEE_POD_LARGE', 'COFFEE_POD_LARGE'), ('COFFEE_POD_SMALL', 'COFFEE_POD_SMALL'), ('ESPRESSO_POD', 'ESPRESSO_POD')], default='COFFEE_POD_LARGE', max_length=100)),
                ('coffee_flavor', models.CharField(blank=True, choices=[('COFFEE_FLAVOR_VANILLA', 'COFFEE_FLAVOR_VANILLA'), ('COFFEE_FLAVOR_CARAMEL', 'COFFEE_FLAVOR_CARAMEL'), ('COFFEE_FLAVOR_PSL', 'COFFEE_FLAVOR_PSL'), ('COFFEE_FLAVOR_MOCHA', 'COFFEE_FLAVOR_MOCHA'), ('COFFEE_FLAVOR_HAZELNUT', 'COFFEE_FLAVOR_HAZELNUT')], default='COFFEE_FLAVOR_VANILLA', max_length=100)),
                ('pack_size', models.CharField(blank=True, choices=[('1_dozen', '1_dozen'), ('3 dozen ', '3 dozen '), ('5_dozen', '5_dozen'), ('7_dozen', '7_dozen')], default='1_dozen', max_length=100)),
                ('description', models.TextField(default='', max_length=254)),
                ('code', models.TextField(default='', max_length=254)),
            ],
        ),
    ]
