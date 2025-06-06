# Generated by Django 5.2.1 on 2025-05-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reeds', '0005_remove_reed_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reed',
            old_name='gauge_thickness',
            new_name='cane_gauge_thickness',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='overall_length',
            new_name='descr_length',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='character_resistance',
            new_name='descr_resistance',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='chararacter_response',
            new_name='descr_response',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='character_sound',
            new_name='descr_sound',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='creator',
            new_name='item_creator',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='title',
            new_name='item_title',
        ),
        migrations.RenameField(
            model_name='reed',
            old_name='instrument',
            new_name='item_type',
        ),
        migrations.RemoveField(
            model_name='reed',
            name='description',
        ),
        migrations.RemoveField(
            model_name='reed',
            name='visibility',
        ),
        migrations.AddField(
            model_name='reed',
            name='item_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='reed',
            name='item_id',
            field=models.CharField(default='nn'),
        ),
        migrations.AddField(
            model_name='reed',
            name='item_rating',
            field=models.IntegerField(choices=[(0, 'Useless'), (1, 'Practice'), (2, 'Performance'), (3, 'Premium')], default=1),
        ),
        migrations.AddField(
            model_name='reed',
            name='item_visibility',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reed',
            name='staple_material',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reed',
            name='cane_shaper_form',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reed',
            name='cane_supplier',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='reed',
            name='staple_model',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
