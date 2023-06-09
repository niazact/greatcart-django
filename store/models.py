from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=50,null=True)
    description = models.TextField(max_length=255,blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    images = models.ImageField(upload_to='photos/products/',blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self ):
        return self.product_name
