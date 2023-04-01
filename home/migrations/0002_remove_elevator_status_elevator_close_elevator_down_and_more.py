# Generated by Django 4.1.7 on 2023-04-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elevator',
            name='status',
        ),
        migrations.AddField(
            model_name='elevator',
            name='close',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='elevator',
            name='down',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='elevator',
            name='open',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='elevator',
            name='running',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='elevator',
            name='stop',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='elevator',
            name='up',
            field=models.BooleanField(default=False),
        ),
    ]