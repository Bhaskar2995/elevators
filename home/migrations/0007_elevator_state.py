# Generated by Django 4.1.7 on 2023-04-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_elevator_next_destination_alter_elevator_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevator',
            name='state',
            field=models.CharField(default='closed', max_length=300),
        ),
    ]
