# Generated by Django 4.0.4 on 2022-06-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveytable',
            old_name='frome_date',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='surveytable',
            name='from_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='surveytable',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
