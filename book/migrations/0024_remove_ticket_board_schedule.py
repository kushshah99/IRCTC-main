# Generated by Django 2.2.7 on 2019-11-13 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0023_auto_20191113_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='board_schedule',
        ),
    ]