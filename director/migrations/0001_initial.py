# Generated by Django 4.0.5 on 2022-06-09 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=30, unique=True, verbose_name='director name')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6, verbose_name='gender')),
                ('age', models.IntegerField(default=0)),
                ('create_time', models.TimeField(auto_now=True, verbose_name='Created at')),
                ('update_time', models.TimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
    ]
