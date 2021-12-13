# Generated by Django 4.0 on 2021-12-12 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_nutrition_size_ml_alter_nutrition_size_oz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergy_product',
            old_name='allergy_id',
            new_name='allergy',
        ),
        migrations.RenameField(
            model_name='allergy_product',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='caffeine',
            new_name='caffeine_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='natrium',
            new_name='natrium_mg',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='protein',
            new_name='protein_g',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='saturated_fat',
            new_name='saturated_fat_g',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='sugars',
            new_name='sugars_g',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
