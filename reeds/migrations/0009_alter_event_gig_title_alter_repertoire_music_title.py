# Generated by Django 5.2.1 on 2025-05-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reeds', '0008_remove_reed_item_title_alter_reed_item_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='gig_title',
            field=models.CharField(default='add a title', max_length=100),
        ),
        migrations.AlterField(
            model_name='repertoire',
            name='music_title',
            field=models.CharField(default='add a title', max_length=100),
        ),
    ]
