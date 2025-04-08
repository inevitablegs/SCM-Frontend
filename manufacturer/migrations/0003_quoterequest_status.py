# Generated by Django 5.1.7 on 2025-03-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0002_quoterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoterequest',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('awarded', 'Awarded'), ('expired', 'Expired')], default='open', max_length=10),
        ),
    ]
