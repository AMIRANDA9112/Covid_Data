# Generated by Django 3.1.6 on 2021-02-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.TextField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='deaths',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='infected',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='lastUpdate',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='recovered',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]