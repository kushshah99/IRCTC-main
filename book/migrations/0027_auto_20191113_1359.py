# Generated by Django 2.2.7 on 2019-11-13 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0026_auto_20191113_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='board_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_schedule_tickets', to='book.Schedule'),
        ),
    ]
