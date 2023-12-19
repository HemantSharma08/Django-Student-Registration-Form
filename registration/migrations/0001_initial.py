# Generated by Django 4.2.7 on 2023-12-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]
