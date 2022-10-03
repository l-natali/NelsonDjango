from django.db import models
import uuid
import os.path


class Category(models.Model):

    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class Product(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(unique=True, max_length=100, db_index=True)
    description_short = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.SmallIntegerField(max_length=2, blank=True)
    new_arrival = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        index_together = (('id', 'slug'), )


class ProductPhoto(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('products/', new_filename)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.product}'


class HomeBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('homebanner/', new_filename)

    title = models.CharField(unique=True, max_length=100, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)

