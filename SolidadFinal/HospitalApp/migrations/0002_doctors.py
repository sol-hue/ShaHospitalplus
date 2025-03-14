# Generated by Django 5.1.6 on 2025-02-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]
