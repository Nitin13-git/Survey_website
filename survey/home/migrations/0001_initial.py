# Generated by Django 4.0.4 on 2022-06-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('frome_date', models.CharField(default='', max_length=100)),
                ('to_date', models.CharField(default='', max_length=100)),
            ],
        ),
    ]