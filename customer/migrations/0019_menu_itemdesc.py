# Generated by Django 2.0 on 2019-02-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_remove_menu_itemdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='itemDesc',
            field=models.CharField(default='A dish consisting of 2 pieces usually from broiler chickens which have been floured or battered and then pan-fried,', max_length=10),
        ),
    ]
