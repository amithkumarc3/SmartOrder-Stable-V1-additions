# Generated by Django 2.0 on 2019-02-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_menu_itemdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='itemDesc',
            field=models.CharField(default='A dish consisting of 2 pieces usually from broiler chickens which have been floured or battered.', max_length=96),
        ),
    ]
