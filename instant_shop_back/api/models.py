from django.db import models
import json, jsonfield
class City(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Shop(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='shop')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'city': self.city
        }

    def __str__(self):
        return f'{self.id}: {self.name} | {self.description}'


class Category(models.Model):
    name = models.CharField(max_length=250)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='category')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def to_json(self):
        return {
            'name': self.name
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    price = models.FloatField(max_length=250)
    filename = models.TextField(max_length=1000)
    height = models.IntegerField(default=300)
    width = models.IntegerField(default=300)
    rating = models.FloatField(default=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='product')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'filename': self.filename,
            'height':self.height,
            'width':self.width,
            'rating':self.rating,
            'category':self.category,
            'shop_id':self.shop_id
        }

    def __str__(self):
        return f'{self.id}: {self.name} | {self.description} | {self.price}'


class Order(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField(max_length=1000)
    prod = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'filename': self.filename,
            'height':self.height,
            'width':self.width,
            'rating':self.rating,
            'category':self.category,
            'shop_id':self.shop_id
        }

    def __str__(self):
        return f'{self.id}: {self.name}'
