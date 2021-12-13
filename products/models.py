from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'


class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'products'


class Allergy_product(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'


class Nutrition(models.Model):
    size_ml = models.IntegerField()
    size_oz = models.IntegerField()
    kcal = models.DecimalField(max_digits=5, decimal_places=1)
    natrium_mg = models.DecimalField(max_digits=5, decimal_places=1)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=1)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=1)
    protein_g = models.DecimalField(max_digits=5, decimal_places=1)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=1)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'


class Image(models.Model):
    image_url = models.URLField(max_length=200)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


class Allergy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'allergies'


