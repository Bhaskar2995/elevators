# Generated by Django 4.1.7 on 2023-04-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('up', 'False'), ('down', 'False'), ('running', 'False'), ('stop', 'False'), ('open', 'False'), ('close', 'False')], max_length=300)),
            ],
        ),
    ]
