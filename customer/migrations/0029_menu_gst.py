# Generated by Django 2.0 on 2019-02-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0028_remove_menu_gst'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='gst',
            field=models.FloatField(default=7),
        ),
    ]
