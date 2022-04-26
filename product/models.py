from django.db import models
from helper.models import CommonBase
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel, CommonBase):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class ProductAttr(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class ProductAttrValue(models.Model):
    prod_attr = models.ForeignKey(ProductAttr, on_delete=models.CASCADE)
    attr_value = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.prod_attr} -> {self.attr_value}"


class ProductType(models.Model):
    name = models.CharField(max_length=200)
    prod_attr = models.ManyToManyField(ProductAttr)


class Product(CommonBase):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(max_length=300)
    attr_values =  models.ManyToManyField(ProductAttrValue)
    prod_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
class ProdMedia(CommonBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return f'{self.product}'


class EcomPlatform(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class EcomProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    platform = models.ForeignKey(EcomPlatform, on_delete=models.CASCADE)
    link = models.URLField(max_length=300)
    
    def __str__(self):
        return f"{self.platform}: {self.product}"
    
    
class Banner(CommonBase):
    landscape_img = models.ImageField()
    seq_no = models.IntegerField()
    slug = models.SlugField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.seq_no} - {self.category.name}"